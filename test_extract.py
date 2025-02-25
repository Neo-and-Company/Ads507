from src.extract.extract import extract_all_data

def main():
    dataframes = extract_all_data()
    print("Extracted DataFrames:", dataframes.keys())
    for k, df in dataframes.items():
        print(f"{k}: {df.shape}")

if __name__ == "__main__":
    main()