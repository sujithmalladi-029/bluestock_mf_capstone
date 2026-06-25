import pandas as pd

df = pd.read_csv("data/raw/08_investor_transactions.csv")

df["transaction_date"] = pd.to_datetime(df["transaction_date"])

df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

valid_types = ["Sip", "Lumpsum", "Redemption"]

invalid_types = df[
    ~df["transaction_type"].isin(valid_types)
]

print("Invalid Transaction Types:")
print(invalid_types["transaction_type"].unique())

df = df[df["amount_inr"] > 0]

print("\nKYC Status Values:")
print(df["kyc_status"].unique())

df.to_csv("data/processed/clean_transactions.csv", index=False)

print("Saved clean_transactions.csv")