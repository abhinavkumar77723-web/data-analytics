import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("cleaned_online_retail.csv")
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# 1. Monthly quantity sold
monthly = df.groupby(df["InvoiceDate"].dt.to_period("M"))["Quantity"].sum()
monthly.plot(kind="line", marker="o")
plt.title("Monthly Quantity Sold")
plt.xlabel("Month")
plt.ylabel("Quantity")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.show()

# 2. Top 10 products
products = df.groupby("Description")["Quantity"].sum().sort_values(ascending=False).head(10)
products.plot(kind="bar")
plt.title("Top 10 Products by Quantity Sold")
plt.xlabel("Product")
plt.ylabel("Quantity")
plt.xticks(rotation=75)
plt.tight_layout()
plt.savefig("top_products.png")
plt.show()

# 3. Top 10 countries
countries = df["Country"].value_counts().head(10)
countries.plot(kind="bar")
plt.title("Top 10 Countries by Transactions")
plt.xlabel("Country")
plt.ylabel("Transactions")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top_countries.png")
plt.show()

# 4. Quantity distribution
df["Quantity"].plot(kind="hist", bins=30)
plt.title("Quantity Distribution")
plt.xlabel("Quantity")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("quantity_distribution.png")
plt.show()

# 5. Quantity vs UnitPrice
sample = df.sample(5000, random_state=1)
sample.plot.scatter(x="UnitPrice", y="Quantity")
plt.title("Quantity vs Unit Price")
plt.xlabel("Unit Price")
plt.ylabel("Quantity")
plt.tight_layout()
plt.savefig("quantity_price.png")
plt.show()