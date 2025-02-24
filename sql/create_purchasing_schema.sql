DROP DATABASE IF EXISTS AdventurePurchasing;
CREATE DATABASE AdventurePurchasing;
USE AdventurePurchasing;

-- 1) Employee
CREATE TABLE Employee (
    EmployeeID INT AUTO_INCREMENT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    JobTitle VARCHAR(50),
    HireDate DATETIME,
    ModifiedDate DATETIME
);

-- 2) Vendor
CREATE TABLE Vendor (
    VendorID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    AccountNumber VARCHAR(50),
    PreferredVendorStatus TINYINT,
    ModifiedDate DATETIME
);

-- 3) ShipMethod
CREATE TABLE ShipMethod (
    ShipMethodID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(50),
    ShipBase DECIMAL(19,4),
    ShipRate DECIMAL(19,4),
    ModifiedDate DATETIME
);

-- 4) Product
CREATE TABLE Product (
    ProductID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(100),
    ProductNumber VARCHAR(25),
    StandardCost DECIMAL(19,4),
    ListPrice DECIMAL(19,4),
    ModifiedDate DATETIME
);

-- 5) PurchaseOrderHeader
CREATE TABLE PurchaseOrderHeader (
    PurchaseOrderID INT AUTO_INCREMENT PRIMARY KEY,
    EmployeeID INT NOT NULL,
    VendorID INT NOT NULL,
    ShipMethodID INT NOT NULL,
    OrderDate DATETIME,
    ShipDate DATETIME,
    SubTotal DECIMAL(19,4),
    TaxAmt DECIMAL(19,4),
    Freight DECIMAL(19,4),
    TotalDue DECIMAL(19,4),
    ModifiedDate DATETIME,
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID),
    FOREIGN KEY (VendorID) REFERENCES Vendor(VendorID),
    FOREIGN KEY (ShipMethodID) REFERENCES ShipMethod(ShipMethodID)
);

-- 6) PurchaseOrderDetail
CREATE TABLE PurchaseOrderDetail (
    PurchaseOrderDetailID INT AUTO_INCREMENT PRIMARY KEY,
    PurchaseOrderID INT NOT NULL,
    ProductID INT NOT NULL,
    OrderQty INT,
    UnitPrice DECIMAL(19,4),
    LineTotal DECIMAL(19,4),
    ReceivedQty DECIMAL(19,4),
    RejectedQty DECIMAL(19,4),
    StockedQty DECIMAL(19,4),
    ModifiedDate DATETIME,
    FOREIGN KEY (PurchaseOrderID) REFERENCES PurchaseOrderHeader(PurchaseOrderID),
    FOREIGN KEY (ProductID) REFERENCES Product(ProductID)
);