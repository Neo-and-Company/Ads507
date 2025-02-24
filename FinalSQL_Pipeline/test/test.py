from src.extract.extract import extract_all_data

dataframes = extract_all_data()
for filename, df in dataframes.items():
    print(filename, df.shape)