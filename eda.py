import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("books_data.csv")

print("=" * 60)
print("EXPLORATORY DATA ANALYSIS - BOOK DATASET")
print("=" * 60)

# Dataset information
print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nFirst 5 Records:")
print(df.head())

# Data types
print("\nData Types:")
print(df.dtypes)

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Convert price to numeric
df["Price"] = (
    df["Price"]
    .str.extract(r"(\d+\.\d+)")[0]
    .astype(float)
)

# Convert ratings to numbers
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["Rating Number"] = df["Rating"].map(rating_map)

# Statistical summary
print("\nPrice Statistics:")
print(df["Price"].describe())

print("\nRating Statistics:")
print(df["Rating Number"].describe())

# Most expensive books
print("\nTop 10 Most Expensive Books:")
print(
    df[["Book Title", "Price"]]
    .sort_values(by="Price", ascending=False)
    .head(10)
)

# Cheapest books
print("\nTop 10 Cheapest Books:")
print(
    df[["Book Title", "Price"]]
    .sort_values(by="Price")
    .head(10)
)

# Rating distribution
print("\nRating Distribution:")
print(df["Rating"].value_counts())

# Availability
print("\nAvailability Distribution:")
print(df["Availability"].value_counts())

# Average price by rating
print("\nAverage Price by Rating:")
print(
    df.groupby("Rating")["Price"]
    .mean()
    .sort_values(ascending=False)
)

# Price distribution chart
plt.figure(figsize=(8, 5))
plt.hist(df["Price"], bins=10, edgecolor="black")
plt.title("Distribution of Book Prices")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.savefig("price_distribution.png")
plt.show()

# Rating distribution chart
rating_counts = df["Rating"].value_counts()

plt.figure(figsize=(8, 5))
rating_counts.plot(kind="bar")
plt.title("Book Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Books")
plt.tight_layout()
plt.savefig("rating_distribution.png")
plt.show()

# Average price by rating chart
average_price = (
    df.groupby("Rating")["Price"]
    .mean()
    .reindex(["One", "Two", "Three", "Four", "Five"])
)

plt.figure(figsize=(8, 5))
average_price.plot(kind="bar")
plt.title("Average Book Price by Rating")
plt.xlabel("Rating")
plt.ylabel("Average Price (£)")
plt.tight_layout()
plt.savefig("average_price_by_rating.png")
plt.show()

# Price vs Rating
plt.figure(figsize=(8, 5))
plt.scatter(
    df["Rating Number"],
    df["Price"],
    alpha=0.7
)
plt.title("Price vs Book Rating")
plt.xlabel("Rating")
plt.ylabel("Price (£)")
plt.tight_layout()
plt.savefig("price_vs_rating.png")
plt.show()

print("\n" + "=" * 60)
print("EDA COMPLETED SUCCESSFULLY")
print("=" * 60)