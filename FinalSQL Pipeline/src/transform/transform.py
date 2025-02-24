def transform_all_data(all_data):
    """
    Applies cleaning, renaming, or type conversion to each DataFrame as needed.
    """
    transformed = {}
    for filename, df in all_data.items():
        print(f"[TRANSFORM] Processing {filename}")
        # Example transformations:
        # df.columns = [col.strip() for col in df.columns]
        transformed[filename] = df
    return transformed