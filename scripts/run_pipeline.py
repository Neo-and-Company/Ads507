import sys
import os

# Add the project root directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.extract.extract import extract_all_data
from src.transform.transform import transform_all_data
from src.load.load import load_data_to_mysql

def run_etl():
    # 1) Extract
    dataframes = extract_all_data()
    print("Extraction complete. DataFrames keys:", dataframes.keys())

    # 2) Transform
    transformed_data = transform_all_data(dataframes)

    # 3) Load
    for filename, df in transformed_data.items():
        # For example: "Product.csv" -> "Product"
        table_name = filename.replace(".csv", "")
        print(f"Loading {filename} into table '{table_name}'...")
        load_data_to_mysql(df, table_name)

    print("ETL pipeline completed successfully.")

if __name__ == "__main__":
    run_etl()