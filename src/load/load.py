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

    with engine.begin() as connection:
        # Disable foreign key checks to allow dropping of referenced tables
        connection.execute(text("SET FOREIGN_KEY_CHECKS=0"))
        # "replace" overwrites existing table. Use "append" if you want to keep old data.
        df.to_sql(table_name, con=connection, if_exists="replace", index=False)
        # Re-enable foreign key checks after the table has been replaced
        connection.execute(text("SET FOREIGN_KEY_CHECKS=1"))
    
    print(f"Loaded '{table_name}' into database '{dbname}' successfully.")