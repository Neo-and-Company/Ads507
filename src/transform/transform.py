# src/transform/transform.py

import pandas as pd

def transform_employee(df: pd.DataFrame) -> pd.DataFrame:
    """
    Employee.csv -> Employee table
    Columns match the MySQL schema: EmployeeID, FirstName, LastName, etc.
    """
    df.columns = [
        "EmployeeID", "FirstName", "LastName", "JobTitle",
        "HireDate", "ModifiedDate"
    ]
    df.fillna(0, inplace=True)
    print("Employee transformed successfully.")
    return df

def transform_vendor(df: pd.DataFrame) -> pd.DataFrame:
    """
    Vendor.csv -> Vendor table
    """
    df.columns = [
        "VendorID", "Name", "AccountNumber", "PreferredVendorStatus",
        "ModifiedDate"
    ]
    df.fillna(0, inplace=True)
    print("Vendor transformed successfully.")
    return df

def transform_shipmethod(df: pd.DataFrame) -> pd.DataFrame:
    """
    ShipMethod.csv -> ShipMethod table
    """
    df.columns = [
        "ShipMethodID", "Name", "ShipBase", "ShipRate", "ModifiedDate"
    ]
    df.fillna(0, inplace=True)
    print("ShipMethod transformed successfully.")
    return df

def transform_product(df: pd.DataFrame) -> pd.DataFrame:
    """
    Product.csv -> Product table
    """
    df.columns = [
        "ProductID", "Name", "ProductNumber", "StandardCost",
        "ListPrice", "ModifiedDate"
    ]
    df.fillna(0, inplace=True)
    print("Product transformed successfully.")
    return df

def transform_purchaseorderheader(df: pd.DataFrame) -> pd.DataFrame:
    """
    PurchaseOrderHeader.csv -> PurchaseOrderHeader table
    """
    df.columns = [
        "PurchaseOrderID", "EmployeeID", "VendorID", "ShipMethodID",
        "OrderDate", "ShipDate", "SubTotal", "TaxAmt", "Freight",
        "TotalDue", "ModifiedDate"
    ]
    df.fillna(0, inplace=True)
    print("PurchaseOrderHeader transformed successfully.")
    return df

def transform_purchaseorderdetail(df: pd.DataFrame) -> pd.DataFrame:
    """
    PurchaseOrderDetail.csv -> PurchaseOrderDetail table
    """
    df.columns = [
        "PurchaseOrderDetailID", "PurchaseOrderID", "ProductID", "OrderQty",
        "UnitPrice", "LineTotal", "ReceivedQty", "RejectedQty",
        "StockedQty", "ModifiedDate"
    ]
    df.fillna(0, inplace=True)
    print("PurchaseOrderDetail transformed successfully.")
    return df

def transform_all_data(dataframes: dict) -> dict:
    """
    Loops through the dictionary of DataFrames (keyed by CSV filename),
    calling the correct transform function for each CSV.
    Returns a dict of transformed DataFrames.
    """
    transformed = {}

    for filename, df in dataframes.items():
        if filename == "Employee.csv":
            transformed[filename] = transform_employee(df)
        elif filename == "Vendor.csv":
            transformed[filename] = transform_vendor(df)
        elif filename == "ShipMethod.csv":
            transformed[filename] = transform_shipmethod(df)
        elif filename == "Product.csv":
            transformed[filename] = transform_product(df)
        elif filename == "PurchaseOrderHeader.csv":
            transformed[filename] = transform_purchaseorderheader(df)
        elif filename == "PurchaseOrderDetail.csv":
            transformed[filename] = transform_purchaseorderdetail(df)
        else:
            print(f"No transform function for {filename}, leaving as-is.")
            transformed[filename] = df

    return transformed