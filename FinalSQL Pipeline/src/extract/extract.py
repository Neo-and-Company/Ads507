import os
import pandas as pd

def extract_all_data():
    """
    Reads CSV files from 'data/' and returns a dict of DataFrames keyed by filename.
    """
    data_folder = "data"
    csv_files = [
        "Product.csv",
        "Vendor.csv",
        "ShipMethod.csv",
        "PurchaseOrderHeader.csv",
        "PurchaseOrderDetail.csv"
    ]

    all_data = {}
    for csv_file in csv_files:
        path = os.path.join(data_folder, csv_file)
        df = pd.read_csv(path)
        all_data[csv_file] = df
        print(f"[EXTRACT] {csv_file} -> {len(df)} rows")
    return all_data