-- 1. Top 5 Fund Houses by AUM
SELECT fund_house, aum_crore
FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV per Month
SELECT
    strftime('%Y-%m', nav_date) AS month,
    AVG(nav) AS average_nav
FROM fact_nav
GROUP BY month
ORDER BY month;

-- 3. SIP Year-over-Year Growth
SELECT
    year,
    total_sip_inflow_crore
FROM monthly_sip_inflows
ORDER BY year;

-- 4. Transactions by State
SELECT
    state,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 5. Funds with Expense Ratio below 1%
SELECT
    scheme_name,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 6. Top 10 Schemes by 5-Year Return
SELECT
    scheme_name,
    return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;

-- 7. Average Expense Ratio by Category
SELECT
    category,
    AVG(expense_ratio_pct) AS avg_expense
FROM dim_fund
GROUP BY category;

-- 8. Count of Funds by Risk Category
SELECT
    risk_category,
    COUNT(*) AS total_funds
FROM dim_fund
GROUP BY risk_category;

-- 9. Total Transaction Amount by Transaction Type
SELECT
    transaction_type,
    SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY transaction_type;

-- 10. Number of Schemes by Fund House
SELECT
    fund_house,
    COUNT(*) AS total_schemes
FROM dim_fund
GROUP BY fund_house
ORDER BY total_schemes DESC;