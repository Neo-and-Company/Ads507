-- Create database
CREATE DATABASE IF NOT EXISTS business_db;
USE business_db;

-- Create Employee table
CREATE TABLE `Employee` (
  `EmployeeID` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `FirstName`  VARCHAR(50) NOT NULL,
  `LastName`   VARCHAR(50) NOT NULL,
  `JobTitle`   VARCHAR(50) NOT NULL,
  `HireDate`   DATE NOT NULL,
  `ModifiedDate` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`EmployeeID`)
) ENGINE=InnoDB;

-- Create Product table
CREATE TABLE `Product` (
  `ProductID`   INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `Name`        VARCHAR(100) NOT NULL,
  `ProductNumber` VARCHAR(25) NOT NULL,
  `ListPrice`   DECIMAL(10,2) NOT NULL,
  `ModifiedDate` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`ProductID`),
  UNIQUE KEY `UQ_Product_ProductNumber` (`ProductNumber`)
) ENGINE=InnoDB;

-- Create Vendor table
CREATE TABLE `Vendor` (
  `VendorID`    INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `AccountNumber` VARCHAR(15) NOT NULL,
  `Name`        VARCHAR(50) NOT NULL,
  `CreditRating` TINYINT UNSIGNED NOT NULL,
  `PreferredVendorStatus` TINYINT(1) NOT NULL DEFAULT 1,
  `ActiveFlag`  TINYINT(1) NOT NULL DEFAULT 1,
  `PurchasingWebServiceURL` VARCHAR(255) DEFAULT NULL,
  `ModifiedDate` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`VendorID`),
  UNIQUE KEY `UQ_Vendor_AccountNumber` (`AccountNumber`)
) ENGINE=InnoDB;

-- Create ShipMethod table
CREATE TABLE `ShipMethod` (
  `ShipMethodID` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `Name`       VARCHAR(50) NOT NULL,
  `ShipBase`   DECIMAL(10,2) NOT NULL,
  `ShipRate`   DECIMAL(10,2) NOT NULL,
  `ModifiedDate` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`ShipMethodID`),
  UNIQUE KEY `UQ_ShipMethod_Name` (`Name`)
) ENGINE=InnoDB;

-- Create PurchaseOrderHeader table
CREATE TABLE `PurchaseOrderHeader` (
  `PurchaseOrderID` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `RevisionNumber` TINYINT UNSIGNED NOT NULL DEFAULT 0,
  `Status`       TINYINT UNSIGNED NOT NULL,
  `EmployeeID`   INT UNSIGNED NOT NULL,
  `VendorID`     INT UNSIGNED NOT NULL,
  `ShipMethodID` INT UNSIGNED NOT NULL,
  `OrderDate`    DATE NOT NULL,
  `ShipDate`     DATE DEFAULT NULL,
  `SubTotal`     DECIMAL(10,2) NOT NULL DEFAULT 0.00,
  `TaxAmt`       DECIMAL(10,2) NOT NULL DEFAULT 0.00,
  `Freight`      DECIMAL(10,2) NOT NULL DEFAULT 0.00,
  `TotalDue`     DECIMAL(10,2) NOT NULL DEFAULT 0.00,
  `ModifiedDate` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`PurchaseOrderID`),
  KEY `IX_PurchaseOrderHeader_EmployeeID` (`EmployeeID`),
  KEY `IX_PurchaseOrderHeader_VendorID` (`VendorID`),
  KEY `IX_PurchaseOrderHeader_ShipMethodID` (`ShipMethodID`),
  CONSTRAINT `FK_POHeader_Employee` 
    FOREIGN KEY (`EmployeeID`) REFERENCES `Employee`(`EmployeeID`),
  CONSTRAINT `FK_POHeader_Vendor` 
    FOREIGN KEY (`VendorID`) REFERENCES `Vendor`(`VendorID`),
  CONSTRAINT `FK_POHeader_ShipMethod` 
    FOREIGN KEY (`ShipMethodID`) REFERENCES `ShipMethod`(`ShipMethodID`)
) ENGINE=InnoDB;

-- Create ProductVendor junction table
CREATE TABLE `ProductVendor` (
  `ProductID`        INT UNSIGNED NOT NULL,
  `VendorID`         INT UNSIGNED NOT NULL,
  `AverageLeadTime`  INT NOT NULL,
  `StandardPrice`    DECIMAL(10,2) NOT NULL,
  `LastReceiptCost`  DECIMAL(10,2) DEFAULT NULL,
  `LastReceiptDate`  DATETIME DEFAULT NULL,
  `MinOrderQty`      INT NOT NULL,
  `MaxOrderQty`      INT NOT NULL,
  `OnOrderQty`       INT NOT NULL,
  `UnitMeasureCode`  CHAR(3) NOT NULL,
  `ModifiedDate`     DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`ProductID`, `VendorID`),
  KEY `IX_ProductVendor_VendorID` (`VendorID`),
  CONSTRAINT `FK_ProductVendor_Product` 
    FOREIGN KEY (`ProductID`) REFERENCES `Product`(`ProductID`),
  CONSTRAINT `FK_ProductVendor_Vendor` 
    FOREIGN KEY (`VendorID`) REFERENCES `Vendor`(`VendorID`)
) ENGINE=InnoDB;

-- Create PurchaseOrderDetail table
CREATE TABLE `PurchaseOrderDetail` (
  `PurchaseOrderID`      INT UNSIGNED NOT NULL,
  `PurchaseOrderDetailID` INT UNSIGNED NOT NULL,
  `ProductID`           INT UNSIGNED NOT NULL,
  `OrderQty`            INT NOT NULL,
  `UnitPrice`           DECIMAL(10,2) NOT NULL,
  `LineTotal`           DECIMAL(10,2) NOT NULL,
  `ReceivedQty`         INT NOT NULL DEFAULT 0,
  `RejectedQty`         INT NOT NULL DEFAULT 0,
  `StockedQty`          INT NOT NULL DEFAULT 0,
  `DueDate`             DATE NOT NULL,
  `ModifiedDate`        DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`PurchaseOrderID`, `PurchaseOrderDetailID`),
  KEY `IX_PurchaseOrderDetail_ProductID` (`ProductID`),
  CONSTRAINT `FK_PODetail_PurchaseOrder` 
    FOREIGN KEY (`PurchaseOrderID`) REFERENCES `PurchaseOrderHeader`(`PurchaseOrderID`),
  CONSTRAINT `FK_PODetail_Product` 
    FOREIGN KEY (`ProductID`) REFERENCES `Product`(`ProductID`)
) ENGINE=InnoDB;