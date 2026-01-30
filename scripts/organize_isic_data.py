"""
Organize ISIC 2018 dataset for training
Creates binary labels (melanoma vs benign) and organized directory structure
"""

import pandas as pd
import os
from pathlib import Path
import shutil

print("=" * 70)
print("ORGANIZING ISIC 2018 DATASET")
print("=" * 70)

# Paths
raw_dir = Path("data/raw")
processed_dir = Path("data/processed")
processed_dir.mkdir(exist_ok=True, parents=True)

# 1. Load labels
print("\n1. Loading ground truth labels...")

train_labels_path = raw_dir / "labels" / "ISIC2018_Task3_Training_GroundTruth" / "ISIC2018_Task3_Training_GroundTruth.csv"
val_labels_path = raw_dir / "labels" / "ISIC2018_Task3_Validation_GroundTruth" / "ISIC2018_Task3_Validation_GroundTruth.csv"

if not train_labels_path.exists():
    print(f"ERROR: Training labels not found at {train_labels_path}")
    print("Please download the dataset first using download_isic.sh")
    exit(1)

# Load training labels
df_train = pd.read_csv(train_labels_path)
print(f"Training samples: {len(df_train)}")

# Load validation labels (if available)
if val_labels_path.exists():
    df_val = pd.read_csv(val_labels_path)
    print(f"Validation samples: {len(df_val)}")
else:
    print("Validation labels not found (this is OK, we'll create our own splits)")
    df_val = None

# 2. Understand label structure
print("\n2. Analyzing label structure...")
print(f"\nColumns: {list(df_train.columns)}")

# ISIC 2018 has 7 classes:
# MEL: Melanoma
# NV: Melanocytic nevus
# BCC: Basal cell carcinoma
# AKIEC: Actinic keratosis / Bowen's disease (intraepithelial carcinoma)
# BKL: Benign keratosis
# DF: Dermatofibroma
# VASC: Vascular lesion

# Get class counts
print("\nClass distribution:")
for col in df_train.columns[1:]:  # Skip 'image' column
    count = df_train[col].sum()
    print(f"  {col}: {count}")

# 3. Create binary labels (Melanoma vs Benign)
print("\n3. Creating binary labels (Melanoma vs Benign)...")

# Binary classification: MEL (class 1) vs all others (class 0)
df_train['binary_label'] = df_train['MEL'].astype(int)

if df_val is not None:
    df_val['binary_label'] = df_val['MEL'].astype(int)

print(f"\nBinary distribution (training):")
print(f"  Benign (0): {(df_train['binary_label'] == 0).sum()}")
print(f"  Melanoma (1): {(df_train['binary_label'] == 1).sum()}")
print(f"  Ratio: {(df_train['binary_label'] == 0).sum() / (df_train['binary_label'] == 1).sum():.1f}:1")

# 4. Create file path mapping
print("\n4. Creating file path mapping...")

# Images are in subdirectories now
images_dir = raw_dir / "images" / "ISIC2018_Task3_Training_Input"

# Create DataFrame with image paths and labels
data_list = []

for idx, row in df_train.iterrows():
    image_id = row['image']
    image_path = images_dir / f"{image_id}.jpg"
    
    if image_path.exists():
        data_list.append({
            'image_id': image_id,
            'image_path': str(image_path),
            'binary_label': row['binary_label'],
            'split': 'train'
        })
    else:
        # Try without .jpg extension (some might have different extensions)
        for ext in ['.jpg', '.jpeg', '.JPG', '.JPEG']:
            image_path_alt = images_dir / f"{image_id}{ext}"
            if image_path_alt.exists():
                data_list.append({
                    'image_id': image_id,
                    'image_path': str(image_path_alt),
                    'binary_label': row['binary_label'],
                    'split': 'train'
                })
                break

# Save to processed directory
labels_binary_path = processed_dir / "labels_binary.csv"
df_binary = pd.DataFrame(data_list)

if len(df_binary) == 0:
    print("\n✗ ERROR: No images found!")
    print(f"   Checked directory: {images_dir}")
    print(f"   Directory exists: {images_dir.exists()}")
    if images_dir.exists():
        print(f"   Files in directory: {len(list(images_dir.glob('*')))}")
        print(f"   First few files: {list(images_dir.glob('*'))[:5]}")
    exit(1)

df_binary.to_csv(labels_binary_path, index=False)

print(f"✓ Saved binary labels to: {labels_binary_path}")
print(f"  Total images: {len(df_binary)}")
print(f"  Images with existing files: {df_binary['image_path'].apply(os.path.exists).sum()}")
print(f"  Missing images: {len(df_binary) - df_binary['image_path'].apply(os.path.exists).sum()}")

# 5. Create documentation
print("\n5. Creating dataset documentation...")

docs_content = f"""# ISIC 2018 Dataset

## Overview
International Skin Imaging Collaboration (ISIC) 2018 Challenge Dataset for melanoma detection.

## Dataset Statistics
- **Training samples**: {len(df_train)}
- **Task**: Multi-class classification (7 diagnostic categories)
- **Our use**: Binary classification (Melanoma vs Benign)

## Classes (Original)
1. MEL: Melanoma
2. NV: Melanocytic nevus
3. BCC: Basal cell carcinoma
4. AKIEC: Actinic keratosis / Bowen's disease
5. BKL: Benign keratosis
6. DF: Dermatofibroma
7. VASC: Vascular lesion

## Binary Classification
- **Class 0 (Benign)**: All classes except MEL
- **Class 1 (Melanoma)**: MEL only

## Class Distribution (Binary)
- Benign: {(df_train['binary_label'] == 0).sum()} samples
- Melanoma: {(df_train['binary_label'] == 1).sum()} samples
- **Imbalance ratio**: {(df_train['binary_label'] == 0).sum() / (df_train['binary_label'] == 1).sum():.1f}:1

## Image Properties
- **Format**: JPEG
- **Color**: RGB
- **Size**: Variable (will resize to 224x224 for EfficientNet)

## Files Created
- `data/processed/labels_binary.csv`: Binary labels with file paths
- `data/processed/splits/`: Train/val/test splits (created in Phase 1)

## Usage
```python
import pandas as pd

# Load binary labels
df = pd.read_csv('data/processed/labels_binary.csv')
```

## Citation
Codella N, Gutman D, Celebi ME, et al.
Skin Lesion Analysis Toward Melanoma Detection 2018: 
A Challenge Hosted by the International Skin Imaging Collaboration (ISIC).
arXiv:1902.03368, 2019.

## Links
- Challenge website: https://challenge.isic-archive.com/landing/2018/
- Paper: https://arxiv.org/abs/1902.03368
"""

docs_path = processed_dir / "DATASET_INFO.md"
with open(docs_path, 'w') as f:
    f.write(docs_content)

print(f"✓ Created dataset documentation: {docs_path}")

print("\n" + "=" * 70)
print("DATASET ORGANIZATION COMPLETE")
print("=" * 70)
print(f"\nBinary labels saved to: {labels_binary_path}")
print(f"Documentation saved to: {docs_path}")
print(f"\nNext steps:")
print("  1. Read ISIC dataset paper (Task 0.4.2)")
print("  2. Explore dataset structure (Task 0.4.3)")
print("  3. Perform detailed EDA (Task 0.4.4)")