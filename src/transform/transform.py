def transform_employee(df: pd.DataFrame) -> pd.DataFrame:
    """Transform Employee data to match MySQL schema (column names and data types)."""
    df = df.copy()
    df.columns = df.columns.str.strip()  # remove any whitespace in headers
    # Rename to match MySQL schema
    rename_map = {
        'BusinessEntityID': 'EmployeeID'
        # Add other renames if needed
    }
    df.rename(columns=rename_map, inplace=True)
    # Fill missing values with defaults
    if 'SalariedFlag' in df.columns:
        df['SalariedFlag'] = df['SalariedFlag'].fillna(1)
    if 'VacationHours' in df.columns:
        df['VacationHours'] = df['VacationHours'].fillna(0)
    if 'SickLeaveHours' in df.columns:
        df['SickLeaveHours'] = df['SickLeaveHours'].fillna(0)
    if 'CurrentFlag' in df.columns:
        df['CurrentFlag'] = df['CurrentFlag'].fillna(1)
    # Convert dates to datetime
    for col in ['BirthDate', 'HireDate', 'ModifiedDate']:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')
    # Cast numeric columns to int where appropriate
    for col in ['EmployeeID', 'OrganizationLevel', 'VacationHours', 'SickLeaveHours']:
        if col in df.columns:
            df[col] = df[col].fillna(0).astype(int)
    # Ensure flag/indicator columns are int (0 or 1)
    if 'SalariedFlag' in df.columns:
        df['SalariedFlag'] = df['SalariedFlag'].astype(int)
    if 'CurrentFlag' in df.columns:
        df['CurrentFlag'] = df['CurrentFlag'].astype(int)
    # Clean up string columns
    if 'Gender' in df.columns:
        df['Gender'] = df['Gender'].astype(str).str.strip()
    if 'MaritalStatus' in df.columns:
        df['MaritalStatus'] = df['MaritalStatus'].astype(str).str.strip()
    # Ensure GUID is string if present
    if 'rowguid' in df.columns:
        df['rowguid'] = df['rowguid'].astype(str)
    return df

def transform_vendor(df: pd.DataFrame) -> pd.DataFrame:
    """Transform Vendor data to match MySQL schema."""
    df = df.copy()
    df.columns = df.columns.str.strip()
    # Rename to match schema
    df.rename(columns={'BusinessEntityID': 'VendorID'}, inplace=True)
    # Fill missing defaults
    if 'PreferredVendorStatus' in df.columns:
        df['PreferredVendorStatus'] = df['PreferredVendorStatus'].fillna(1)
    if 'ActiveFlag' in df.columns:
        df['ActiveFlag'] = df['ActiveFlag'].fillna(1)
    # Convert dates
    if 'ModifiedDate' in df.columns:
        df['ModifiedDate'] = pd.to_datetime(df['ModifiedDate'], errors='coerce')
    # Cast numeric fields
    if 'VendorID' in df.columns:
        df['VendorID'] = df['VendorID'].fillna(0).astype(int)
    if 'CreditRating' in df.columns:
        df['CreditRating'] = df['CreditRating'].fillna(0).astype(int)
    # Ensure bit flags are int
    for col in ['PreferredVendorStatus', 'ActiveFlag']:
        if col in df.columns:
            df[col] = df[col].astype(int)
    return df

def transform_shipmethod(df: pd.DataFrame) -> pd.DataFrame:
    """Transform ShipMethod data to match MySQL schema."""
    df = df.copy()
    df.columns = df.columns.str.strip()
    # Rename (if needed) – assuming headers already match (ShipMethodID, Name, ShipBase, ShipRate, ModifiedDate, rowguid)
    # Fill missing defaults for numeric fields
    if 'ShipBase' in df.columns:
        # Treat empty strings as NaN, then fill with 0.0
        df['ShipBase'] = df['ShipBase'].replace(r'^\s*$', None, regex=True).fillna(0.0)
    if 'ShipRate' in df.columns:
        df['ShipRate'] = df['ShipRate'].replace(r'^\s*$', None, regex=True).fillna(0.0)
    # Convert dates to datetime
    if 'ModifiedDate' in df.columns:
        df['ModifiedDate'] = pd.to_datetime(df['ModifiedDate'], errors='coerce')
    # Convert numeric columns to proper types
    for col in ['ShipMethodID', 'ShipBase', 'ShipRate']:
        if col in df.columns:
            # Remove any non-numeric characters (commas, currency symbols) 
            if df[col].dtype == object:
                df[col] = df[col].replace(r'[^0-9\.-]', '', regex=True)
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0.0)
            if col == 'ShipMethodID':
                df[col] = df[col].astype(int)
    # Ensure GUID column is string
    if 'rowguid' in df.columns:
        df['rowguid'] = df['rowguid'].astype(str)
    return df

def transform_product(df: pd.DataFrame) -> pd.DataFrame:
    """Transform Product data to match MySQL schema."""
    df = df.copy()
    df.columns = df.columns.str.strip()
    # Rename columns if needed (assuming CSV uses same names as MySQL schema)
    # Fill missing default values for flags
    if 'MakeFlag' in df.columns:
        df['MakeFlag'] = df['MakeFlag'].fillna(1)
    if 'FinishedGoodsFlag' in df.columns:
        df['FinishedGoodsFlag'] = df['FinishedGoodsFlag'].fillna(1)
    # Fill critical numeric fields with 0 if missing
    for col in ['SafetyStockLevel', 'ReorderPoint', 'StandardCost', 'ListPrice', 'DaysToManufacture']:
        if col in df.columns:
            df[col] = df[col].fillna(0)
    # Handle Weight: treat empty as NaN (leave NaN to represent NULL if unknown weight)
    if 'Weight' in df.columns:
        df['Weight'] = df['Weight'].replace(r'^\s*$', None, regex=True)
        # If needed to fill missing weight with 0.0, uncomment:
        # df['Weight'] = df['Weight'].fillna(0.0)
    # Strip whitespace from string fields
    for col in ['Name', 'ProductNumber', 'Color', 'Size', 
                'SizeUnitMeasureCode', 'WeightUnitMeasureCode', 
                'ProductLine', 'Class', 'Style']:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip()
            # Replace 'nan' strings (from NaN conversion) with None
            df[col] = df[col].replace('nan', None)
    # Convert date fields to datetime
    for col in ['SellStartDate', 'SellEndDate', 'DiscontinuedDate', 'ModifiedDate']:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')
    # Convert numeric fields to proper types
    num_cols = ['ProductID', 'SafetyStockLevel', 'ReorderPoint', 'DaysToManufacture',
                'ProductSubcategoryID', 'ProductModelID']
    for col in num_cols:
        if col in df.columns:
            if df[col].dtype == object:
                df[col] = df[col].replace(r'[^0-9\.-]', '', regex=True)
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
            df[col] = df[col].astype(int)
    # Convert monetary/decimal fields to floats
    for col in ['StandardCost', 'ListPrice', 'Weight']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce').astype(float)
    # Cast flag fields to int
    if 'MakeFlag' in df.columns:
        df['MakeFlag'] = df['MakeFlag'].astype(int)
    if 'FinishedGoodsFlag' in df.columns:
        df['FinishedGoodsFlag'] = df['FinishedGoodsFlag'].astype(int)
    # Ensure GUID is string
    if 'rowguid' in df.columns:
        df['rowguid'] = df['rowguid'].astype(str)
    return df

def transform_purchase_order_header(df: pd.DataFrame) -> pd.DataFrame:
    """Transform PurchaseOrderHeader data to match MySQL schema."""
    df = df.copy()
    df.columns = df.columns.str.strip()
    # Rename columns if needed (assuming headers already match schema)
    # Fill missing defaults
    if 'RevisionNumber' in df.columns:
        df['RevisionNumber'] = df['RevisionNumber'].fillna(0)
    if 'Status' in df.columns:
        df['Status'] = df['Status'].fillna(1)
    if 'SubTotal' in df.columns:
        df['SubTotal'] = df['SubTotal'].fillna(0.0)
    if 'TaxAmt' in df.columns:
        df['TaxAmt'] = df['TaxAmt'].fillna(0.0)
    if 'Freight' in df.columns:
        df['Freight'] = df['Freight'].fillna(0.0)
    # Compute TotalDue if missing
    if 'TotalDue' in df.columns:
        df['TotalDue'] = df['TotalDue'].fillna(df.get('SubTotal', 0) 
                                               + df.get('TaxAmt', 0) 
                                               + df.get('Freight', 0))
    else:
        # If TotalDue not in CSV but expected in schema, create it
        if all(x in df.columns for x in ['SubTotal', 'TaxAmt', 'Freight']):
            df['TotalDue'] = df['SubTotal'] + df['TaxAmt'] + df['Freight']
    # Convert date columns to datetime
    for col in ['OrderDate', 'ShipDate', 'ModifiedDate']:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')
    # Cast ID and status fields to int
    for col in ['PurchaseOrderID', 'RevisionNumber', 'Status', 'EmployeeID', 'VendorID', 'ShipMethodID']:
        if col in df.columns:
            df[col] = df[col].fillna(0).astype(int)
    # Cast financial fields to float
    for col in ['SubTotal', 'TaxAmt', 'Freight', 'TotalDue']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0.0)
    return df

def transform_purchase_order_detail(df: pd.DataFrame) -> pd.DataFrame:
    """Transform PurchaseOrderDetail data to match MySQL schema."""
    df = df.copy()
    df.columns = df.columns.str.strip()
    # Rename columns if needed (assuming headers match schema)
    # Fill missing values with defaults/calculations
    if 'OrderQty' in df.columns:
        df['OrderQty'] = df['OrderQty'].fillna(0)
    if 'UnitPrice' in df.columns:
        df['UnitPrice'] = df['UnitPrice'].fillna(0.0)
    if 'ReceivedQty' in df.columns:
        df['ReceivedQty'] = df['ReceivedQty'].fillna(0.0)
    if 'RejectedQty' in df.columns:
        df['RejectedQty'] = df['RejectedQty'].fillna(0.0)
    if 'StockedQty' in df.columns:
        df['StockedQty'] = df['StockedQty'].fillna(df.get('ReceivedQty', 0.0) - df.get('RejectedQty', 0.0))
    else:
        # If StockedQty not in CSV but expected, compute it
        if 'ReceivedQty' in df.columns and 'RejectedQty' in df.columns:
            df['StockedQty'] = df['ReceivedQty'] - df['RejectedQty']
    if 'LineTotal' in df.columns:
        df['LineTotal'] = df['LineTotal'].fillna(df.get('OrderQty', 0) * df.get('UnitPrice', 0.0))
    else:
        # If LineTotal not in CSV, compute it
        if 'OrderQty' in df.columns and 'UnitPrice' in df.columns:
            df['LineTotal'] = df['OrderQty'] * df['UnitPrice']
    # Convert date fields to datetime
    if 'DueDate' in df.columns:
        df['DueDate'] = pd.to_datetime(df['DueDate'], errors='coerce')
    if 'ModifiedDate' in df.columns:
        df['ModifiedDate'] = pd.to_datetime(df['ModifiedDate'], errors='coerce')
    # Cast ID and quantity fields to int
    for col in ['PurchaseOrderID', 'PurchaseOrderDetailID', 'OrderQty', 'ProductID']:
        if col in df.columns:
            df[col] = df[col].fillna(0).astype(int)
    # Clean and convert numeric/money fields to float
    for col in ['UnitPrice', 'LineTotal', 'ReceivedQty', 'RejectedQty', 'StockedQty']:
        if col in df.columns:
            if df[col].dtype == object:
                df[col] = df[col].replace(r'[^0-9\.-]', '', regex=True)
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0.0)
    return df