import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/02_nav_history.csv")

# Convert date column to datetime
df["date"] = pd.to_datetime(df["date"])

# Sort by AMFI code and date
df = df.sort_values(["amfi_code", "date"])

# Remove duplicate rows
df = df.drop_duplicates()

# Forward fill missing NAV values within each scheme
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

# Validate NAV > 0
invalid_nav = df[df["nav"] <= 0]

print(f"Invalid NAV Records: {len(invalid_nav)}")

# Keep only valid NAV values
df = df[df["nav"] > 0]

# Save cleaned dataset
df.to_csv("data/processed/clean_nav.csv", index=False)

print("✅ Saved: data/processed/clean_nav.csv")