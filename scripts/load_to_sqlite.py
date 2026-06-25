import pandas as pd
from sqlalchemy import create_engine

# Create SQLite database
engine = create_engine("sqlite:///db/bluestock_mf.db")

# Read cleaned datasets
fund = pd.read_csv("data/raw/01_fund_master.csv")
nav = pd.read_csv("data/processed/clean_nav.csv")
transactions = pd.read_csv("data/processed/clean_transactions.csv")
performance = pd.read_csv("data/processed/clean_performance.csv")
aum = pd.read_csv("data/raw/03_aum_by_fund_house.csv")

# Load into SQLite
fund.to_sql("dim_fund", engine, if_exists="replace", index=False)
nav.to_sql("fact_nav", engine, if_exists="replace", index=False)
transactions.to_sql("fact_transactions", engine, if_exists="replace", index=False)
performance.to_sql("fact_performance", engine, if_exists="replace", index=False)
aum.to_sql("fact_aum", engine, if_exists="replace", index=False)

print("✅ All datasets loaded into SQLite successfully.\n")

# Verify row counts
tables = {
    "dim_fund": fund,
    "fact_nav": nav,
    "fact_transactions": transactions,
    "fact_performance": performance,
    "fact_aum": aum
}

print("Row Count Verification")
print("-" * 40)

for table, df in tables.items():
    count = pd.read_sql(f"SELECT COUNT(*) AS rows FROM {table}", engine)
    print(f"{table:20} CSV: {len(df):6} | DB: {count['rows'][0]:6}")

print("\nDatabase created successfully:")
print("db/bluestock_mf.db")