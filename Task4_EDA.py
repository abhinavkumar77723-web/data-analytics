import pandas as pd

# Load cleaned dataset
df = pd.read_csv("cleaned_online_retail.csv")

# Basic inspection
print("Dataset shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isna().sum())

print("\nDescriptive statistics:")
print(df.describe())

print("\nFirst 5 rows:")
print(df.head())

#Correlation
print("\nCorrelation matrix:")
print(df[["Quantity","UnitPrice"]].corr())

# Outlier detection using IQR

Q1_quantity = df["Quantity"].quantile(0.25)
Q3_quantity = df["Quantity"].quantile(0.75)
IQR_quantity = Q3_quantity - Q1_quantity

quantity_outliers = df[
    (df["Quantity"] < Q1_quantity - 1.5 * IQR_quantity) |
    (df["Quantity"] > Q3_quantity + 1.5 * IQR_quantity)
]

Q1_price = df["UnitPrice"].quantile(0.25)
Q3_price = df["UnitPrice"].quantile(0.75)
IQR_price = Q3_price - Q1_price

price_outliers = df[
    (df["UnitPrice"] < Q1_price - 1.5 * IQR_price) |
    (df["UnitPrice"] > Q3_price + 1.5 * IQR_price)
]

print("\nQuantity outliers:", len(quantity_outliers))
print("UnitPrice outliers:", len(price_outliers))

# Important patterns

print("\nTop 10 countries by number of transactions:")
print(df["Country"].value_counts().head(10))

print("\nTop 10 products by quantity sold:")
print(df.groupby("Description")["Quantity"].sum().sort_values(ascending=False).head(10))

# Sales trend by month

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

monthly_sales = df.groupby(
    df["InvoiceDate"].dt.to_period("M")
)["Quantity"].sum()

print("\nMonthly quantity sold:")
print(monthly_sales)