import pandas as pd

# Load the dataset
df = pd.read_excel("Online Retail.xlsx")

# Basic inspection
print("Shape:", df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:", df.duplicated().sum())


print("\nFirst 5 rows:")
print(df.head())

#Remove duplicate file
df=df.drop_duplicates()
print("\n After removing duplicates:",df.shape)

#Remove rows with missing product description
df=df.dropna(subset=["Description"])
print("After removing missing description:", df.shape)

#Check for negative quantities and prices
print("\nNegative quantities:",(df["Quantity"] < 0).sum())
print("zero or negative prices:",(df["UnitPrice"] <=0).sum())

#Removing invalid sales records
df=df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]
print("After removing invalid records:", df.shape)

#Checking missing customer vlues
print("\nMising CustomerID retained:",df["CustomerID"].isna().sum())

#Save the clean dataset
df.to_csv("cleaned_online_retail.csv", index=False)
print("\nCleaned dataset saved successfully!")