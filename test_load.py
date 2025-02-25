#!/usr/bin/env python3

import pandas as pd
from src.load.load import load_data_to_mysql
from sqlalchemy import create_engine, text
import os

def test_load_product():
    """
    Creates a small DataFrame and uses load_data_to_mysql to upload it
    to the 'Product' table.
    Then optionally queries the table to verify the data was inserted.
    """

    # 1) Create a small in-memory DataFrame for Product
    df = pd.DataFrame({
        'ProductID': [1001, 1002, 1003],
        'Name': ['Widget A', 'Widget B', 'Widget C'],
        'ProductNumber': ['WA-1234', 'WB-5678', 'WC-9012'],
        'ListPrice': [12.99, 24.50, 19.75],
        'ModifiedDate': ['2023-04-10', '2023-05-15', '2023-06-01']
    })

    print("Loading test DataFrame into 'Product' table...")
    # 2) Call load_data_to_mysql, specifying the 'Product' table
    load_data_to_mysql(df, "Product")  # if_exists="replace" by default

    # 3) (Optional) Query the table to confirm
    user = os.environ.get("RDS_USER", "Ads507")
    password = os.environ.get("RDS_PASS", "Gabrielleo24")
    host = os.environ.get("RDS_HOST", "team-shared-mysql.cjwa24wuisi8.us-east-1.rds.amazonaws.com")
    dbname = os.environ.get("RDS_DBNAME", "business_db")

    engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{dbname}")

    with engine.connect() as conn:
        result = conn.execute(text("SELECT COUNT(*) as cnt FROM Product"))
        row = result.fetchone()
        print(f"Number of rows now in Product table: {row['cnt']}")

def main():
    test_load_product()

if __name__ == "__main__":
    main()