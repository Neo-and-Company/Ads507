DROP DATABASE IF EXISTS AdventureSales1;
CREATE DATABASE AdventureSales1;
USE AdventureSales1;

CREATE TABLE Product (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    ProductNumber VARCHAR(25),
    StandardCost DECIMAL(19,4),
    ListPrice DECIMAL(19,4)
);

CREATE TABLE Vendor (
    VendorID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    AccountNumber VARCHAR(50),
    PreferredVendorStatus TINYINT,
    ModifiedDate DATETIME
);

CREATE TABLE ShipMethod (
    ShipMethodID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(50),
    ShipBase DECIMAL(19,4),
    ShipRate DECIMAL(19,4)
);

CREATE TABLE PurchaseOrderHeader (
    PurchaseOrderID INT AUTO_INCREMENT PRIMARY KEY,
    VendorID INT,
    ShipMethodID INT,
    OrderDate DATETIME,
    SubTotal DECIMAL(19,4),
    TaxAmt DECIMAL(19,4),
    Freight DECIMAL(19,4),
    TotalDue DECIMAL(19,4),
    FOREIGN KEY (VendorID) REFERENCES Vendor(VendorID),
    FOREIGN KEY (ShipMethodID) REFERENCES ShipMethod(ShipMethodID)
);

CREATE TABLE PurchaseOrderDetail (
    PurchaseOrderDetailID INT AUTO_INCREMENT PRIMARY KEY,
    PurchaseOrderID INT,
    ProductID INT,
    OrderQty INT,
    UnitPrice DECIMAL(19,4),
    LineTotal DECIMAL(19,4),
    FOREIGN KEY (PurchaseOrderID) REFERENCES PurchaseOrderHeader(PurchaseOrderID),
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
);