import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

books = []

print("Starting web scraping...\n")

for page in range(1, 6):

    url = BASE_URL.format(page)

    print(f"Scraping page {page}...")

    response = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        timeout=10
    )

    if response.status_code != 200:
        print(f"Could not access page {page}")
        continue

    soup = BeautifulSoup(response.text, "html.parser")

    book_items = soup.select("article.product_pod")

    for book in book_items:

        title = book.h3.a["title"]

        price = book.select_one(".price_color").text.strip()

        availability = book.select_one(".availability").text.strip()

        rating_class = book.select_one(".star-rating")["class"]
        rating = rating_class[1]

        product_url = book.h3.a["href"]

        image_url = book.select_one("img")["src"]

        product_url = (
            "https://books.toscrape.com/catalogue/"
            + product_url.replace("../", "")
        )

        image_url = (
            "https://books.toscrape.com/"
            + image_url.replace("../", "")
        )

        books.append({
            "Book Title": title,
            "Price": price,
            "Rating": rating,
            "Availability": availability,
            "Product URL": product_url,
            "Image URL": image_url
        })

    time.sleep(1)

print("\nScraping completed!")

df = pd.DataFrame(books)

df.to_csv("books_data.csv", index=False)

print(f"\nTotal books collected: {len(df)}")

print("Dataset saved as books_data.csv")

print("\nFirst 10 records:")
print(df.head(10))