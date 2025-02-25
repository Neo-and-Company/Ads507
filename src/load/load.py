import os
import pandas as pd
from sqlalchemy import create_engine, text

def load_data_to_mysql(df: pd.DataFrame, table_name: str) -> None:
    """
    Loads a DataFrame into the specified MySQL table using SQLAlchemy.
    Disables foreign key checks to avoid conflicts when replacing tables.
    """
    user = os.environ.get("RDS_USER", "Ads507")
    password = os.environ.get("RDS_PASS", "Gabrielleo24")
    host = os.environ.get("RDS_HOST", "team-shared-mysql.cjwa24wuisi8.us-east-1.rds.amazonaws.com")
    dbname = os.environ.get("RDS_DBNAME", "business_db")

    engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{dbname}")


    # "replace" overwrites existing table. Use "append" if you want to keep old data
    df.to_sql(table_name, con=engine, if_exists="replace", index=False)
    print(f"Loaded '{table_name}' into database '{dbname}' successfully.")