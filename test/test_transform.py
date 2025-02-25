#!/usr/bin/env python3

import os
import pandas as pd
from src.transform.transform import transform_all_data

def test_transform_all():
    """
    Reads each CSV, stores them in a dict, calls transform_all_data(),
    and prints shapes/column info for both original and transformed DataFrames.
    """
    # List the CSV files you want to test
    csv_files = [
        "Product.csv",
        "Vendor.csv",
        "ShipMethod.csv",
        "PurchaseOrderHeader.csv",
        "PurchaseOrderDetail.csv"
    ]

    data_dir = "data"  # The folder where your CSV files are
    dataframes = {}

    # 1) Read each CSV into a DataFrame
    for file_name in csv_files:
        path = os.path.join(data_dir, file_name)
        # Adjust delimiter if needed (e.g., sep="," or sep="\t")
        df = pd.read_csv(path, sep=",", header=0)
        print(f"Original {file_name}: shape={df.shape}, columns={list(df.columns)}")
        dataframes[file_name] = df

    # 2) Transform all DataFrames
    transformed_data = transform_all_data(dataframes)

    # 3) Print results
    for file_name, df in transformed_data.items():
        print(f"Transformed {file_name}: shape={df.shape}, columns={list(df.columns)}")
        print(df.head(3))  # show first few rows

def main():
    test_transform_all()

if __name__ == "__main__":
    main()