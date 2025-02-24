import pandas as pd
from sqlalchemy import create_engine

def load_data_to_mysql(salesorderdetail_df, purchaseorderdetail_df):
    user = "Ads507"
    password = "Gabrielleo24"
    host = "team-shared-mysql.cjwa24wuisi8.us-east-1.rds.amazonaws.com"
    port = 3306
    database = "AdventureSales"

    connection_url = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"
    engine = create_engine(connection_url, echo=False)

    # Load data into existing tables
    salesorderdetail_df.to_sql("SalesOrderDetail", con=engine, if_exists="append", index=False)
    purchaseorderdetail_df.to_sql("PurchaseOrderDetail", con=engine, if_exists="append", index=False)

def main():
    # If the files are tab-delimited:
    salesorderdetail_df = pd.read_csv(
        "https://raw.githubusercontent.com/dnguyen-1/AdventureWorks507/main/data/SalesOrderDetail.csv",
        sep="\t"
    )
    purchaseorderdetail_df = pd.read_csv(
        "https://raw.githubusercontent.com/dnguyen-1/AdventureWorks507/main/data/PurchaseOrderDetail.csv",
        sep="\t"
    )

    # Check the first few rows and columns
    print(salesorderdetail_df.head())
    print(salesorderdetail_df.columns)

    # Call the loading function
    load_data_to_mysql(salesorderdetail_df, purchaseorderdetail_df)

if __name__ == "__main__":
    main()