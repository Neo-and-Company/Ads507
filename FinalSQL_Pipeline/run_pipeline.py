# run_pipeline.py
from src.extract.extract import extract_all_data
from src.transform.transform import transform_all_data
from src.load.load import load_data_to_mysql

def main():
    # 1) Extract
    dataframes = extract_all_data()

    # 2) Transform
    transformed_data = transform_all_data(dataframes)

    # 3) Load
    load_data_to_mysql(transformed_data)

if __name__ == "__main__":
    main()