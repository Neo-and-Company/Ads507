# src/extract/extract.py

import requests
import pandas as pd
from io import StringIO

def fetch_csv_from_github(filename: str) -> pd.DataFrame:
    """
    Fetches a tab-delimited CSV from your GitHub repository's 'raw' URL
    and returns a pandas DataFrame.

    :param filename: The name of the CSV file (e.g., "Product.csv").
    :return: A DataFrame containing the CSV data.
    """
    # Adjust 'base_url' if your data folder is in a different path
    # e.g. "https://raw.githubusercontent.com/YourUsername/YourRepo/main/data/"
    base_url = "https://raw.githubusercontent.com/Neo-and-Company/Ads507/main/data/"
    url = base_url + filename

    response = requests.get(url)
    response.raise_for_status()  # raise an error if the request failed

    # If your CSV is comma-delimited, remove sep="\t" or replace with sep=","
    df = pd.read_csv(StringIO(response.text), sep="\t")
    return df

# Update this list to your ACTUAL CSV filenames in the 'data' folder
CSV_FILES = [
    "Product.csv",
    "Vendor.csv",
    "ShipMethod.csv",
    "PurchaseOrderHeader.csv",
    "PurchaseOrderDetail.csv"
]

def extract_all_data() -> dict:
    """
    Fetches each CSV from GitHub and stores them in a dictionary of DataFrames.
    Returns a dict: { 'Product.csv': DataFrame, 'Vendor.csv': DataFrame, ... }
    """
    dataframes = {}
    for file_name in CSV_FILES:
        df = fetch_csv_from_github(file_name)
        dataframes[file_name] = df
        print(f"Extracted {file_name}: shape = {df.shape}")
    return dataframes