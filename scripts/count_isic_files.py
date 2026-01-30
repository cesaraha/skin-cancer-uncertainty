from pathlib import Path

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