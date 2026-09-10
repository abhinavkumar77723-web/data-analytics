# Task 3 - Dataset Selection & Data Preparation
## Dataset

I selected the **Online Retail Dataset** from the UCI Machine Learning Repository. It is a sales/e-commerce dataset with 524800 rows and 8 columns.

## Data Inspection

I used Python and Pandas to check:
- Rows and columns
- Column names and data types
- Missing values
- Duplicate records
- Invalid values

## Data Cleaning

- Removed **5268 duplicate rows**.
- Removed **1454 rows** with missing Description.
- Removed records where Quantity or UnitPrice was not greater than 0.
- Kept missing CustomerID values because the transaction data is still useful for sales analysis.

## Final Result

After cleaning:

- **Rows:** 524379
- **Columns:** 8
- **Missing CustomerID:** 132186

The cleaned data was saved as:

`cleaned_online_retail.csv`
