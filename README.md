# Superstore Sales Analysis – Future Interns Data Science Task 1 (2026)

## Overview
This project analyzes the Sample Superstore Sales dataset to uncover business insights around revenue trends, profitability, product performance, and regional growth opportunities — the kind of analysis real data analysts do for companies and startups.

## Dataset
- **Source:** [Sample Superstore – Kaggle](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
- **Records:** 9,994 rows × 21 columns
- **Period:** 2014 – 2017
- **Fields:** Order ID, Order Date, Region, Category, Sub-Category, Product Name, Sales, Quantity, Discount, Profit

## Tools Used
- **Microsoft Excel** – Data cleaning, pivot analysis, charts, dashboard
- **Python (openpyxl)** – Automated report generation

## Key Business Questions Answered
1. Which categories and sub-categories generate the most revenue and profit?
2. How has revenue grown year over year?
3. Which regions perform best?
4. Which products are most profitable — and which lose money?
5. How do discounts affect profitability?

## Key Findings

| Insight | Detail |
|---|---|
| Technology leads in profit margin | Highest margin of all 3 categories |
| Furniture drags profit | Tables & Bookcases are top loss-makers |
| West region dominates | Highest revenue and profit |
| Discounts above 30% = losses | Nearly all high-discount rows are unprofitable |
| Revenue grew every year | Consistent YoY growth from 2014–2017 |
| Consumer segment is largest | ~51% of total revenue |

## Business Recommendations
1. **Invest in Technology** – highest ROI category; expand inventory and marketing
2. **Fix Furniture pricing** – reduce or eliminate discounts on Tables and Bookcases
3. **Expand West strategy to other regions** – replicate what works in West/East
4. **Cap discounts at 20%** – anything above destroys margin
5. **Focus on Copiers, Phones, Accessories** – top profitable sub-categories
6. **Build Consumer loyalty programs** – biggest segment, high retention value

## Project Structure
```
superstore-sales-analysis/
│
├── Sample - Superstore.csv               # Raw dataset
├── Superstore_Analysis_FutureInterns.xlsx # Full analysis & dashboard (6 sheets)
└── README.md
```

## Excel Report Sheets
| Sheet | Contents |
|---|---|
| Executive Summary | KPIs + Year-on-Year revenue/profit + bar chart |
| Category & Region | Revenue by category (pie) + region (bar chart) |
| Sub-Category Deep Dive | Top 10 profitable + Bottom 5 loss-makers |
| Top Products | Top 10 products by revenue with profit flag |
| Insights & Recommendations | 6 color-coded business insights |
| Raw Data | Full cleaned dataset |

## Internship
**Future Interns – Data Science & Analytics Track, 2026**
