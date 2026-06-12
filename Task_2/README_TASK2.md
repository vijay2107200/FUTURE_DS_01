# Customer Churn & Retention Analysis – Future Interns Data Science Task 2 (2026)

## Overview
This project analyzes telecom subscription data to understand why customers churn and what drives retention. The goal is to produce actionable insights that product managers, founders, and business stakeholders can use to reduce customer loss.

## Dataset
- **Source:** Telco Customer Churn – Kaggle
- **Records:** 7,043 customers × 21 columns
- **Fields:** customerID, gender, SeniorCitizen, Partner, Dependents, tenure, PhoneService, InternetService, Contract, PaymentMethod, MonthlyCharges, TotalCharges, Churn, and more

## Tools Used
- **Microsoft Excel** – Data cleaning, cohort analysis, churn metrics, dashboard

## Key Business Questions Answered
1. What is the overall churn rate?
2. Which contract types have the highest churn?
3. Do customers churn more in early months?
4. Which internet service and payment methods correlate with higher churn?
5. Does tech support reduce churn?

## Key Findings

| Insight | Detail |
|---|---|
| Overall churn rate ~26.5% | Roughly 1 in 4 customers leaves |
| Contract type is the strongest lever | Month-to-month customers churn far more than 1- or 2-year contract customers |
| Churn concentrates early | 0–12 month tenure bucket has the highest churn rate |
| Fiber-optic customers churn above average | Possible service quality or pricing issue |
| Electronic-check users churn more | Likely due to involuntary/manual payment failures |
| No tech support = higher churn | Customers without tech support leave more often |

## Business Recommendations
1. **Migrate month-to-month customers to annual contracts** with a discount or perk
2. **Build a 90-day onboarding & engagement program** to reduce early-life churn
3. **Bundle tech support / online security into mid-tier plans** to raise stickiness
4. **Nudge electronic-check users toward auto-pay** to cut involuntary churn
5. **Investigate fiber-optic service quality and pricing** as a churn driver

## Project Structure
```
FUTURE_DS_01/
│
├── Churn_Analysis_1.xlsx     # Full churn analysis, dashboard & recommendations
├── README_TASK2.md           # This file – Task 2 documentation
│
├── Superstore_Analysis_FutureInterns.xlsx  # Task 1 analysis
├── Sample - Superstore.csv                 # Task 1 dataset
└── README.md                               # Task 1 documentation
```

## Excel Report Sheets
| Sheet | Contents |
|---|---|
| Data | Full cleaned dataset (7,043 rows) |
| Analysis | Churn rates by contract, tenure, internet service, payment, tech support |
| Dashboard | KPI summary – overall churn, total customers, avg tenure, churned count |
| Insights & Recommendations | 5 key findings + 5 actionable business recommendations |

## Internship
**Future Interns – Data Science & Analytics Track, 2026**
