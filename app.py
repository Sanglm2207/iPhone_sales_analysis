# Import necessary libraries
import pandas as pd  # Pandas for data manipulation
import numpy as np   # NumPy for numerical operations
import plotly.express as px  # Plotly Express for easy plotting
import plotly.graph_objects as go  # Plotly Graph Objects for more customization

# Read data from CSV file into a Pandas DataFrame
data = pd.read_csv("apple_products.csv")
# Uncomment the following lines if you want to inspect the data
# print(data.head())      # Display the first few rows of the DataFrame
# print(data.isnull().sum())  # Display the count of missing values in each column
# print(data.describe())   # Display summary statistics of the numerical columns

"""
    Analyzes iPhone sales data and prints the top 10 highest rated products.

    Reads the data from "apple_products.csv" file and performs the following steps:
    1. Sorts the data by "Star Rating" in descending order.
    2. Selects the top 10 highest rated products.
    3. Prints the names of the highest rated products.
"""
# Sort the data by "Star Rating" in descending order
highest_rated = data.sort_values(by=["Star Rating"], ascending=False)
# Select the top 10 highest rated products
highest_rated = highest_rated.head(10)
# Print the names of the highest rated products
print(highest_rated['Product Name'])

"""
    4. Creates a bar chart showing the number of ratings for each of the highest rated iPhones.
"""
# Count the number of occurrences of each product name in the highest_rated DataFrame
iphones = highest_rated["Product Name"].value_counts()

# Extract labels and counts for plotting
label = iphones.index
counts = highest_rated["Number Of Ratings"]
# figure = px.bar(highest_rated, x=label, y = counts,title="Number of Ratings of Highest Rated iPhones")

# Create a scatter plot using Plotly Express
figure = px.scatter(data_frame = data, 
                    x="Number Of Ratings", y="Sale Price", 
                    size="Discount Percentage",  trendline="ols", 
                    title="Relationship between Sale Price and Number of Ratings of iPhones")
figure.show()