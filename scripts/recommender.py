import pandas as pd

# Load performance dataset
performance = pd.read_csv("../data/processed/clean_performance.csv")

print("=" * 50)
print(" MUTUAL FUND RECOMMENDATION SYSTEM ")
print("=" * 50)

print("\nRisk Appetite:")
print("1. Low")
print("2. Moderate")
print("3. High")

choice = input("\nEnter your choice (Low/Moderate/High): ").strip().lower()

# Map user choice to dataset values
risk_map = {
    "low": "Low",
    "moderate": "Moderate",
    "high": "High"
}

if choice not in risk_map:
    print("Invalid choice!")
    exit()

selected_risk = risk_map[choice]

# Filter funds
filtered = performance[
    performance["risk_grade"].str.lower() == selected_risk.lower()
]

# Sort by Sharpe Ratio
recommendations = filtered.sort_values(
    by="sharpe_ratio",
    ascending=False
).head(3)

print("\nTop 3 Recommended Funds\n")

print(
    recommendations[
        [
            "scheme_name",
            "fund_house",
            "category",
            "risk_grade",
            "sharpe_ratio",
            "return_3yr_pct"
        ]
    ]
)