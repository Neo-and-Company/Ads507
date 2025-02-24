import os
from sqlalchemy import create_engine

def load_data_to_mysql(df, table_name):
    """
    Appends DataFrame to the MySQL table specified by table_name.
    """
    # Adjust these as needed or pull from environment variables
    user = "Ads507"
    password = "MySecretPassword"
    host = "team-shared-mysql.cjwa24wuisi8.us-east-1.rds.amazonaws.com"
    port = 3306
    database = "AdventureSales"

    connection_url = f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}"
    engine = create_engine(connection_url, echo=False)

    df.to_sql(table_name, con=engine, if_exists="append", index=False)
    print(f"[LOAD] Inserted {len(df)} rows into {table_name}")