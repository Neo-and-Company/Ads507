import pandas as pd

# Extract data from CSV files
def extract_csv_data():
    try:
        customers_df = pd.read_csv('data/customers.csv')
        orders_df = pd.read_csv('data/orders.csv')
        products_df = pd.read_csv('data/products.csv')
        employees_df = pd.read_csv('data/employees.csv')
        return customers_df, orders_df, products_df, employees_df
    except Exception as e:
        logging.error(f"Data extraction failed: {e}")
        raise