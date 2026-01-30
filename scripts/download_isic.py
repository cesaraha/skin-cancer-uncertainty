"""
ISIC 2018 Dataset Download Script
Downloads the ISIC 2018 Challenge dataset
"""

import os
import urllib.request
import zipfile
from pathlib import Path

print("=" * 70)
print("ISIC 2018 Dataset Download")
print("=" * 70)

# Create directories
os.makedirs('data/raw/images', exist_ok=True)
os.makedirs('data/raw/labels', exist_ok=True)

# Dataset URLs
files_to_download = {
    'ISIC2018_Task3_Training_Input.zip': 'https://isic-challenge-data.s3.amazonaws.com/2018/ISIC2018_Task3_Training_Input.zip',
    'ISIC2018_Task3_Training_GroundTruth.zip': 'https://isic-challenge-data.s3.amazonaws.com/2018/ISIC2018_Task3_Training_GroundTruth.zip',
    'ISIC2018_Task3_Validation_Input.zip': 'https://isic-challenge-data.s3.amazonaws.com/2018/ISIC2018_Task3_Validation_Input.zip',
    'ISIC2018_Task3_Validation_GroundTruth.zip': 'https://isic-challenge-data.s3.amazonaws.com/2018/ISIC2018_Task3_Validation_GroundTruth.zip',
    'ISIC2018_Task3_Test_Input.zip': 'https://isic-challenge-data.s3.amazonaws.com/2018/ISIC2018_Task3_Test_Input.zip',
}

# Download files
download_dir = Path('data/raw')

for filename, url in files_to_download.items():
    filepath = download_dir / filename
    
    if filepath.exists():
        print(f"\n✓ {filename} already exists, skipping...")
        continue
    
    print(f"\nDownloading {filename}...")
    print(f"  From: {url}")
    print(f"  Size: ~2-5 GB (this will take a while)")
    
    try:
        urllib.request.urlretrieve(url, filepath)
        print(f"  ✓ Downloaded successfully")
    except Exception as e:
        print(f"  ✗ Error: {e}")
        continue

# Extract files
print("\n" + "=" * 70)
print("Extracting files...")
print("=" * 70)

extraction_map = {
    'ISIC2018_Task3_Training_Input.zip': 'data/raw/images',
    'ISIC2018_Task3_Training_GroundTruth.zip': 'data/raw/labels',
    'ISIC2018_Task3_Validation_Input.zip': 'data/raw/images',
    'ISIC2018_Task3_Validation_GroundTruth.zip': 'data/raw/labels',
    'ISIC2018_Task3_Test_Input.zip': 'data/raw/images',
}

for filename, extract_to in extraction_map.items():
    filepath = download_dir / filename
    
    if not filepath.exists():
        print(f"\n⚠ {filename} not found, skipping extraction...")
        continue
    
    print(f"\nExtracting {filename}...")
    print(f"  To: {extract_to}")
    
    try:
        with zipfile.ZipFile(filepath, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
        print(f"  ✓ Extracted successfully")
    except Exception as e:
        print(f"  ✗ Error: {e}")

# Clean up zip files (optional)
print("\n" + "=" * 70)
print("Cleaning up zip files...")
print("=" * 70)

response = input("Delete zip files to save space? (y/n): ")
if response.lower() == 'y':
    for filename in files_to_download.keys():
        filepath = download_dir / filename
        if filepath.exists():
            try:
                filepath.unlink()
                print(f"  ✓ Removed {filename}")
            except Exception as e:
                print(f"  ✗ Could not remove {filename}: {e}")

print("\n" + "=" * 70)
print("Download complete!")
print("=" * 70)
print(f"\nImages location: data/raw/images/")
print(f"Labels location: data/raw/labels/")

# Count downloaded files
print("\n" + "=" * 70)
print("Dataset Statistics")
print("=" * 70)

try:
    # Count images in each split
    train_images = list(Path('data/raw/images/ISIC2018_Task3_Training_Input').glob('*.jpg'))
    val_images = list(Path('data/raw/images/ISIC2018_Task3_Validation_Input').glob('*.jpg'))
    test_images = list(Path('data/raw/images/ISIC2018_Task3_Test_Input').glob('*.jpg'))
    
    print(f"\nImages:")
    print(f"  Training:   {len(train_images):>5} images")
    print(f"  Validation: {len(val_images):>5} images")
    print(f"  Test:       {len(test_images):>5} images")
    print(f"  Total:      {len(train_images) + len(val_images) + len(test_images):>5} images")
    
    # Count labels from CSV files
    import pandas as pd
    
    train_labels_path = Path('data/raw/labels/ISIC2018_Task3_Training_GroundTruth/ISIC2018_Task3_Training_GroundTruth.csv')
    val_labels_path = Path('data/raw/labels/ISIC2018_Task3_Validation_GroundTruth/ISIC2018_Task3_Validation_GroundTruth.csv')
    
    print(f"\nLabels:")
    if train_labels_path.exists():
        df_train = pd.read_csv(train_labels_path)
        print(f"  Training:   {len(df_train):>5} labels")
    else:
        print(f"  Training:   NOT FOUND")
    
    if val_labels_path.exists():
        df_val = pd.read_csv(val_labels_path)
        print(f"  Validation: {len(df_val):>5} labels")
    else:
        print(f"  Validation: NOT FOUND")
    
    print(f"  Test:       {'N/A':>5} (no public labels)")
    
    # Class distribution
    if train_labels_path.exists():
        print(f"\nClass Distribution (Training):")
        for col in df_train.columns[1:]:  # Skip 'image' column
            count = df_train[col].sum()
            print(f"  {col:6s}: {count:>4}")
    
except Exception as e:
    print(f"\nCould not count files: {e}")