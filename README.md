## Task 2: Exploratory Data Analysis

### Objective

The objective of this task is to analyze the book dataset collected through web scraping and identify useful patterns, distributions, and relationships in the data.

### Dataset

The dataset contains 100 book records collected from the Books to Scrape website.

The dataset includes information such as:
- Book Title
- Price
- Rating
- Availability
- Product URL
- Image URL

### Data Analysis Performed

The following analysis was performed using Python, Pandas and Matplotlib:

1. Dataset structure and dimensions were examined.
2. Data types and missing values were checked.
3. Book prices were converted into numerical values.
4. Book ratings were converted into numerical values.
5. Price statistics were calculated.
6. Rating distribution was analyzed.
7. Availability distribution was analyzed.
8. The 10 most expensive and cheapest books were identified.
9. Average price was calculated for each rating.
10. Visualizations were created to understand the dataset.

### Visualizations

The following charts were generated:

- Price Distribution
- Book Rating Distribution
- Average Price by Rating
- Price vs Book Rating

### Findings

The analysis shows that book prices are distributed across a wide range, approximately from £10 to £59.

The average price by rating was calculated as follows:

- Three-star books: £36.84
- Two-star books: £35.91
- One-star books: £35.52
- Four-star books: £33.98
- Five-star books: £30.01

In this dataset, five-star books have the lowest average price, while three-star books have the highest average price. Therefore, the dataset does not show a simple pattern where higher ratings always correspond to higher prices.

### Conclusion

The Exploratory Data Analysis helped in understanding the structure and characteristics of the scraped book dataset. Statistical analysis and visualizations made it easier to identify price patterns, rating distributions and the relationship between book ratings and prices.

The analysis demonstrates how Python, Pandas and Matplotlib can be used to transform raw web-scraped data into meaningful information.