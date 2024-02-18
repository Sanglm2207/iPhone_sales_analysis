import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("apple_products.csv")
# print(data.head())
# print(data.isnull().sum())
# print(data.describe())

"""
    Analyzes iPhone sales data and prints the top 10 highest rated products.

    Reads the data from "apple_products.csv" file and performs the following steps:
    1. Sorts the data by "Star Rating" in descending order.
    2. Selects the top 10 highest rated products.
    3. Prints the names of the highest rated products.

"""
highest_rated = data.sort_values(by=["Star Rating"], ascending=False)
highest_rated = highest_rated.head(10)
print(highest_rated['Product Name'])