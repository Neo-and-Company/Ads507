# src/extract/extract.py

import requests
import pandas as pd
from io import StringIO

def fetch_csv_from_github(filename: str) -> pd.DataFrame:
    """
    Fetches a tab-delimited CSV from your GitHub AdventureWorks507 data folder
    and returns a pandas DataFrame.
    """
    base_url = "https://github.com/Neo-and-Company/Ads507/tree/main/FinalSQL%20Pipeline/data/"
    url = base_url + filename
    response = requests.get(url)
    response.raise_for_status()  # raises an error if the download fails

    # If your CSVs are actually comma-delimited, remove delimiter='\t'
    df = pd.read_csv(StringIO(response.text), delimiter='\t')
    return df

# List all the CSV filenames you want to extract
CSV_FILES = [
    "Customer.csv",
    "Vendor.csv",
    "Product.csv",
    "PurchaseOrderHeader.csv",
    "PurchaseOrderDetail.csv"
]

def extract_all_data() -> dict:
    """
    Fetches each CSV from GitHub and stores them in a dictionary of DataFrames.
    Returns a dict: { 'Customer.csv': DataFrame, 'Employee.csv': DataFrame, ... }
    """
    dataframes = {}
    for file_name in CSV_FILES:
        df = fetch_csv_from_github(file_name)
        dataframes[file_name] = df
        print(f"Extracted {file_name}: shape = {df.shape}")
    return dataframes