# Data Dictionary

## 1. 01_fund_master.csv

| Column             | Data Type | Business Definition                 |
| ------------------ | --------- | ----------------------------------- |
| amfi_code          | Integer   | Unique AMFI scheme identifier       |
| fund_house         | String    | Mutual fund company (AMC)           |
| scheme_name        | String    | Name of the mutual fund scheme      |
| category           | String    | Mutual fund category                |
| sub_category       | String    | Specific sub-category of the scheme |
| plan               | String    | Direct or Regular plan              |
| launch_date        | Date      | Scheme launch date                  |
| benchmark          | String    | Benchmark index                     |
| expense_ratio_pct  | Float     | Annual expense ratio (%)            |
| exit_load_pct      | Float     | Exit load percentage                |
| min_sip_amount     | Float     | Minimum SIP investment amount       |
| min_lumpsum_amount | Float     | Minimum lump sum investment         |
| fund_manager       | String    | Fund manager name                   |
| risk_category      | String    | Risk classification                 |
| sebi_category_code | String    | SEBI category code                  |

---

## 2. 02_nav_history.csv

| Column    | Data Type | Business Definition    |
| --------- | --------- | ---------------------- |
| amfi_code | Integer   | AMFI scheme identifier |
| date      | Date      | NAV date               |
| nav       | Float     | Net Asset Value        |

---

## 3. 03_aum_by_fund_house.csv

Contains quarterly Assets Under Management (AUM) of each fund house.

---

## 4. 04_monthly_sip_inflows.csv

Contains monthly SIP inflows across the mutual fund industry.

---

## 5. 05_category_inflows.csv

Contains inflow and outflow values by mutual fund category.

---

## 6. 06_industry_folio_count.csv

Contains investor folio counts for the mutual fund industry.

---

## 7. 07_scheme_performance.csv

Contains historical performance metrics such as 1-year, 3-year, and 5-year returns, Sharpe Ratio, Alpha, Beta, Expense Ratio, and AUM.

---

## 8. 08_investor_transactions.csv

Contains investor transaction records including transaction type, amount, state, city, KYC status, and transaction date.

---

## 9. 09_portfolio_holdings.csv

Contains portfolio holdings of each mutual fund scheme.

---

## 10. 10_benchmark_indices.csv

Contains benchmark index values used to compare mutual fund performance.

---

## Data Source

* AMFI (Association of Mutual Funds in India)
* MFAPI
* Bluestock Capstone Dataset

---

## Database

SQLite Database: **db/bluestock_mf.db**
