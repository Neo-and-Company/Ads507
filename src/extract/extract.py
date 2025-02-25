# src/extract/extract.py

import requests
import pandas as pd
from io import StringIO

def fetch_csv_from_github(filename: str) -> pd.DataFrame:
    """
    Fetches a tab-delimited CSV from your GitHub Ads507 data folder
    and returns a pandas DataFrame.

    If your CSV files are actually comma-delimited, you can remove
    the 'delimiter="\\t"' or replace it with the appropriate delimiter.
    """
    base_url = "https://media.githubusercontent.com/media/Neo-and-Company/Ads507/refs/heads/main/data/"
    url = base_url + filename
    response = requests.get(url)
    response.raise_for_status()  # raises an error if the download fails

    # If your CSVs are actually comma-delimited, remove delimiter='\t'
    df = pd.read_csv(StringIO(response.text), delimiter='\t')
    return df

# List of CSV filenames to extract from the GitHub data folder
CSV_FILES = [
    "PurchaseOrderDetail.csv",
    "PurchaseOrderHeader.csv",
    "ShipMethod.csv",
    "Product.csv",
    "ProductVendor.csv",
    "Vendor.csv"
]

def extract_all_data() -> dict:
    """
    Fetches each CSV file from GitHub (based on CSV_FILES)
    and returns a dictionary of DataFrames keyed by filename.

    Example return:
    {
      "PurchaseOrderDetail.csv": <DataFrame>,
      "PurchaseOrderHeader.csv": <DataFrame>,
      ...
    }
    """
    dataframes = {}
    for file_name in CSV_FILES:
        df = fetch_csv_from_github(file_name)
        dataframes[file_name] = df
        print(f"Extracted {file_name}: shape = {df.shape}")
    return dataframes