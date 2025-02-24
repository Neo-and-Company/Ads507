# src/scripts/run_pipeline.py
import os
import pandas as pd
from sqlalchemy import create_engine
from src.transform.transform import transform_all_data

def main():
    # 1) Read your CSVs into DataFrames
    data_folder = "data"
    csv_files = ["Vendor.csv", "ShipMethod.csv", "Product.csv",
                 "PurchaseOrderHeader.csv", "PurchaseOrderDetail.csv"]

    dataframes = {}
    for csv_file in csv_files:
        path = os.path.join(data_folder, csv_file)
        df = pd.read_csv(path)
        dataframes[csv_file] = df

    # 2) Transform
    transformed_data = transform_all_data(dataframes)

    # 3) Load into MySQL (example)
    user = "Ads507"
    password = "MySecretPassword"
    host = "team-shared-mysql.cjwa24wuisi8.us-east-1.rds.amazonaws.com"
    port = 3306
    database = "AdventureSales1"

    engine = create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}")

    for filename, df in transformed_data.items():
        table_name = filename.replace(".csv", "")  # e.g. "Vendor.csv" -> "Vendor"
        df.to_sql(table_name, con=engine, if_exists="append", index=False)
        print(f"Loaded {len(df)} rows into '{table_name}'")

if __name__ == "__main__":
    main()