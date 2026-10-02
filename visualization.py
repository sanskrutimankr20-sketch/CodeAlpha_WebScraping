import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("books_data.csv")

# Clean price
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

df["Rating"] = df["Rating"].map(rating_map)

print("Dataset loaded successfully!")
print(f"Total books: {len(df)}")

# --------------------------------------------------
# Visualization 1: Price Distribution
# --------------------------------------------------

plt.figure(figsize=(10, 6))

plt.hist(df["Price"], bins=10, edgecolor="black")

plt.title("Distribution of Book Prices")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")

plt.tight_layout()
plt.savefig("visual_price_distribution.png")
plt.show()


# --------------------------------------------------
# Visualization 2: Rating Distribution
# --------------------------------------------------

plt.figure(figsize=(8, 5))

rating_counts = df["Rating"].value_counts().sort_index()

plt.bar(
    rating_counts.index,
    rating_counts.values,
    edgecolor="black"
)

plt.title("Distribution of Book Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Books")

plt.xticks([1, 2, 3, 4, 5])

plt.tight_layout()
plt.savefig("visual_rating_distribution.png")
plt.show()


# --------------------------------------------------
# Visualization 3: Average Price by Rating
# --------------------------------------------------

plt.figure(figsize=(8, 5))

average_price = df.groupby("Rating")["Price"].mean()

plt.bar(
    average_price.index,
    average_price.values,
    edgecolor="black"
)

plt.title("Average Book Price by Rating")
plt.xlabel("Rating")
plt.ylabel("Average Price (£)")

plt.xticks([1, 2, 3, 4, 5])

plt.tight_layout()
plt.savefig("visual_average_price_by_rating.png")
plt.show()


# --------------------------------------------------
# Visualization 4: Price vs Rating
# --------------------------------------------------

plt.figure(figsize=(8, 5))

plt.scatter(
    df["Rating"],
    df["Price"],
    alpha=0.7
)

plt.title("Price vs Book Rating")
plt.xlabel("Book Rating")
plt.ylabel("Price (£)")

plt.xticks([1, 2, 3, 4, 5])

plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("visual_price_vs_rating.png")
plt.show()


print("\n" + "=" * 60)
print("TASK 3 DATA VISUALIZATION COMPLETED SUCCESSFULLY")
print("=" * 60)

print("\nGenerated visualizations:")
print("1. visual_price_distribution.png")
print("2. visual_rating_distribution.png")
print("3. visual_average_price_by_rating.png")
print("4. visual_price_vs_rating.png")