from src.extract.extract import extract_all_data
from src.transform.transform import transform_all_data
from src.load.load import load_data_to_mysql

def run_etl():
    # 1) Extract
    all_data = extract_all_data()

    # 2) Transform
    transformed_data = transform_all_data(all_data)

    # 3) Load
    for filename, df in transformed_data.items():
        table_name = filename.replace(".csv", "")  # e.g. "Product.csv" -> "Product"
        load_data_to_mysql(df, table_name)

    print("ETL pipeline completed successfully.")

if __name__ == "__main__":
    run_etl()