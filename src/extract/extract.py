# src/extract/extract.py

import requests
import pandas as pd
from io import StringIO

def get_csv_from_github(filename: str) -> pd.DataFrame:
    """
    Downloads a tab-delimited CSV from your GitHub repository's 'raw' URL
    and returns a pandas DataFrame.

    :param filename: The name of the CSV file (e.g., "Customer.csv").
    :return: A DataFrame containing the CSV data.
    """
    base_url = "https://raw.githubusercontent.com/Neo-and-Company/Ads507/main/FinalSQL%20Pipeline/data/"
    url = base_url + filename

    # Perform an HTTP GET request
    response = requests.get(url)
    response.raise_for_status()  # raise an error if the request failed

    # Parse the response text as a tab-delimited CSV
    df = pd.read_csv(StringIO(response.text), sep="\t")
    return df

# List of CSV files to extract
CSV_FILES = [
    "Customer.csv",
    "Vendor.csv",
    "Product.csv",
    "PurchaseOrderHeader.csv",
    "PurchaseOrderDetail.csv"
]

def extract_all_data() -> dict:
    """
    Fetches each CSV file from GitHub (based on CSV_FILES)
    and returns a dictionary of DataFrames keyed by filename.
    """
    dataframes = {}
    for file_name in CSV_FILES:
        df = get_csv_from_github(file_name)
        dataframes[file_name] = df
        print(f"Extracted {file_name}: shape={df.shape}")
    return dataframes