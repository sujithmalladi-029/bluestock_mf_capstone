import pandas as pd

df = pd.read_csv("data/raw/01_fund_master.csv")

print("\n========== FUND MASTER ANALYSIS ==========\n")

print("Unique Fund Houses:")
print(df["fund_house"].unique())

print("\nCategories:")
print(df["category"].unique())

print("\nSub Categories:")
print(df["sub_category"].unique())

print("\nRisk Categories:")
print(df["risk_category"].unique())

print("\nTotal Schemes:")
print(df["amfi_code"].nunique())

print("\nSample Data:")
print(df.head())