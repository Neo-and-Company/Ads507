# src/transform/transform.py

import pandas as pd

def transform_product(df: pd.DataFrame) -> pd.DataFrame:
    """
    Product.csv -> product table
    Columns: ProductID, Name, ProductNumber, ListPrice, ModifiedDate
    """
    df.columns = [
        "ProductID", "Name", "ProductNumber", "ListPrice", "ModifiedDate"
    ]
    df.fillna(0, inplace=True)
    print("Product transformed successfully.")
    return df

def transform_vendor(df: pd.DataFrame) -> pd.DataFrame:
    """
    Vendor.csv -> Vendor table
    Columns: VendorID, AccountNumber, Name, CreditRating,
             PreferredVendorStatus, ActiveFlag, PurchasingWebServiceURL,
             ModifiedDate
    """
    df.columns = [
        "VendorID", "AccountNumber", "Name", "CreditRating",
        "PreferredVendorStatus", "ActiveFlag", "PurchasingWebServiceURL",
        "ModifiedDate"
    ]
    df.fillna(0, inplace=True)
    print("Vendor transformed successfully.")
    return df

def transform_shipmethod(df: pd.DataFrame) -> pd.DataFrame:
    """
    ShipMethod.csv -> ShipMethod table
    Columns: ShipMethodID, Name, ShipBase, ShipRate, ModifiedDate
    """
    df.columns = [
        "ShipMethodID", "Name", "ShipBase", "ShipRate", "ModifiedDate"
    ]
    df.fillna(0, inplace=True)
    print("ShipMethod transformed successfully.")
    return df

def transform_purchaseorderheader(df: pd.DataFrame) -> pd.DataFrame:
    """
    PurchaseOrderHeader.csv -> PurchaseOrderHeader table
    Columns: PurchaseOrderID, RevisionNumber, Status, EmployeeID,
             VendorID, ShipMethodID, OrderDate, ShipDate, SubTotal,
             TaxAmt, Freight, TotalDue, ModifiedDate
    """
    df.columns = [
        "PurchaseOrderID", "RevisionNumber", "Status", "EmployeeID",
        "VendorID", "ShipMethodID", "OrderDate", "ShipDate",
        "SubTotal", "TaxAmt", "Freight", "TotalDue", "ModifiedDate"
    ]
    df.fillna(0, inplace=True)
    print("PurchaseOrderHeader transformed successfully.")
    return df

def transform_purchaseorderdetail(df: pd.DataFrame) -> pd.DataFrame:
    """
    PurchaseOrderDetail.csv -> PurchaseOrderDetail table
    Columns: PurchaseOrderID, PurchaseOrderDetailID, ProductID, OrderQty,
             UnitPrice, LineTotal, ReceivedQty, RejectedQty, StockedQty,
             DueDate, ModifiedDate
    """
    df.columns = [
        "PurchaseOrderID", "PurchaseOrderDetailID", "ProductID", "OrderQty",
        "UnitPrice", "LineTotal", "ReceivedQty", "RejectedQty", "StockedQty",
        "DueDate", "ModifiedDate"
    ]
    df.fillna(0, inplace=True)
    print("PurchaseOrderDetail transformed successfully.")
    return df

def transform_all_data(dataframes: dict) -> dict:
    """
    Loops through the dictionary of DataFrames keyed by CSV filename,
    calling the correct transform function for each. Returns a dict of
    transformed DataFrames, still keyed by the CSV filename.
    """
    transformed = {}

    for filename, df in dataframes.items():
        fname_lower = filename.lower()

        if fname_lower == "product.csv":
            transformed[filename] = transform_product(df)
        elif fname_lower == "vendor.csv":
            transformed[filename] = transform_vendor(df)
        elif fname_lower == "shipmethod.csv":
            transformed[filename] = transform_shipmethod(df)
        elif fname_lower == "purchaseorderheader.csv":
            transformed[filename] = transform_purchaseorderheader(df)
        elif fname_lower == "purchaseorderdetail.csv":
            transformed[filename] = transform_purchaseorderdetail(df)
        else:
            print(f"No specific transform function for {filename}, leaving as-is.")
            transformed[filename] = df

    return transformed