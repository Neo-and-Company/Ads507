-- Drop the old DB if it exists (optional)
DROP DATABASE IF EXISTS AdventureSales1;

-- Create a fresh database
CREATE DATABASE AdventureSales1;
USE AdventureSales1;

-- 1) Vendor
CREATE TABLE Vendor (
    VendorID INT NOT NULL,
    BusinessEntityID INT,
    AccountNumber VARCHAR(15) NOT NULL,
    Name VARCHAR(50) NOT NULL,
    CreditRating TINYINT NOT NULL,
    PreferredVendorStatus BIT NOT NULL,
    ActiveFlag BIT NOT NULL,
    PurchasingWebServiceURL VARCHAR(1024),
    ModifiedDate DATETIME NOT NULL,
    PRIMARY KEY (VendorID)
);

-- 2) ShipMethod
CREATE TABLE ShipMethod (
    ShipMethodID INT NOT NULL,
    Name VARCHAR(50) NOT NULL,
    ShipBase DECIMAL(19,4) NOT NULL,
    ShipRate DECIMAL(19,4) NOT NULL,
    rowguid CHAR(36) NOT NULL,
    ModifiedDate DATETIME NOT NULL,
    PRIMARY KEY (ShipMethodID)
);

-- 3) Product
CREATE TABLE Product (
    ProductID INT NOT NULL,
    Name VARCHAR(50) NOT NULL,
    ProductNumber VARCHAR(25) NOT NULL,
    StandardCost DECIMAL(19,4) NOT NULL,
    ListPrice DECIMAL(19,4) NOT NULL,
    ModifiedDate DATETIME NOT NULL,
    PRIMARY KEY (ProductID)
);

-- 4) PurchaseOrderHeader
CREATE TABLE PurchaseOrderHeader (
    PurchaseOrderID INT NOT NULL,
    RevisionNumber TINYINT NOT NULL,
    Status TINYINT NOT NULL,
    EmployeeID INT NOT NULL,
    VendorID INT NOT NULL,
    ShipMethodID INT NOT NULL,
    OrderDate DATETIME NOT NULL,
    ShipDate DATETIME,
    SubTotal DECIMAL(19,4) NOT NULL,
    TaxAmt DECIMAL(19,4) NOT NULL,
    Freight DECIMAL(19,4) NOT NULL,
    TotalDue DECIMAL(19,4),
    ModifiedDate DATETIME NOT NULL,
    PRIMARY KEY (PurchaseOrderID),
    FOREIGN KEY (VendorID) REFERENCES Vendor(VendorID),
    FOREIGN KEY (ShipMethodID) REFERENCES ShipMethod(ShipMethodID)
);

-- 5) PurchaseOrderDetail
CREATE TABLE PurchaseOrderDetail (
    PurchaseOrderID INT NOT NULL,
    PurchaseOrderDetailID INT NOT NULL,
    DueDate DATETIME NOT NULL,
    OrderQty SMALLINT NOT NULL,
    ProductID INT NOT NULL,
    UnitPrice DECIMAL(19,4) NOT NULL,
    LineTotal DECIMAL(19,4),
    ReceivedQty DECIMAL(8,2) NOT NULL,
    RejectedQty DECIMAL(8,2) NOT NULL,
    StockedQty DECIMAL(8,2) NOT NULL,
    ModifiedDate DATETIME NOT NULL,
    PRIMARY KEY (PurchaseOrderID, PurchaseOrderDetailID),
    FOREIGN KEY (PurchaseOrderID) REFERENCES PurchaseOrderHeader(PurchaseOrderID),
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
);