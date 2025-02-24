# src/transform/transform.py
import pandas as pd

def transform_vendor(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = [
        "VendorID", "BusinessEntityID", "AccountNumber", "Name",
        "CreditRating", "PreferredVendorStatus", "ActiveFlag",
        "PurchasingWebServiceURL", "ModifiedDate"
    ]
    df.fillna(0, inplace=True)
    print("Vendor transformed successfully.")
    return df

def transform_shipmethod(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = [
        "ShipMethodID", "Name", "ShipBase", "ShipRate", "rowguid", "ModifiedDate"
    ]
    df.fillna(0, inplace=True)
    print("ShipMethod transformed successfully.")
    return df

def transform_product(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = [
        "ProductID", "Name", "ProductNumber", "StandardCost",
        "ListPrice", "ModifiedDate"
    ]
    df.fillna(0, inplace=True)
    print("Product transformed successfully.")
    return df

def transform_purchaseorderheader(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = [
        "PurchaseOrderID", "RevisionNumber", "Status", "EmployeeID",
        "VendorID", "ShipMethodID", "OrderDate", "ShipDate", "SubTotal",
        "TaxAmt", "Freight", "TotalDue", "ModifiedDate"
    ]
    df.fillna(0, inplace=True)
    print("PurchaseOrderHeader transformed successfully.")
    return df

def transform_purchaseorderdetail(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = [
        "PurchaseOrderID", "PurchaseOrderDetailID", "DueDate", "OrderQty",
        "ProductID", "UnitPrice", "LineTotal", "ReceivedQty",
        "RejectedQty", "StockedQty", "ModifiedDate"
    ]
    df.fillna(0, inplace=True)
    print("PurchaseOrderDetail transformed successfully.")
    return df

def transform_all_data(dataframes: dict) -> dict:
    """
    Loops through the dictionary of DataFrames, calling the correct
    transform function for each CSV. Returns a dict of transformed DataFrames.
    """
    transformed = {}

    for filename, df in dataframes.items():
        if filename == "Vendor.csv":
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
            # If you have additional tables/CSVs, add more elif blocks
            # or just leave as-is to skip specialized transforms.
            print(f"No transform function for {filename}, leaving as-is.")
            transformed[filename] = df

    return transformed