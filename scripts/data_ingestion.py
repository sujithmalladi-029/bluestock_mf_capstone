import pandas as pd
from pathlib import Path

raw_path = Path("../data/raw")

csv_files = sorted(raw_path.glob("*.csv"))

print(f"Found {len(csv_files)} datasets")

for file in csv_files:

    print("\n" + "="*80)
    print(f"Dataset: {file.name}")

    df = pd.read_csv(file)

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nHead:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print("="*80)