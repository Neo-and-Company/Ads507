Below is an updated design document that meets the professor’s requirements. Feel free to copy/paste and adapt it to your preferred format (PDF, Markdown, etc.).

AdventureWorks Business DB ETL Pipeline – Design Document

1. GitHub Repository

GitHub Link: [Your GitHub Repo URL Here]
(Example: https://github.com/Neo-and-Company/Ads507 )

This repository contains all source code (Python scripts for Extract, Transform, Load), the database schema (.sql files), and documentation for deploying the pipeline.

2. Source Datasets

2.1. Dataset Origin & Rationale

We use AdventureWorks CSV files (commonly available as a sample database from Microsoft). The CSVs include realistic tables such as:
	•	Employee.csv
	•	Vendor.csv
	•	ShipMethod.csv
	•	Product.csv
	•	PurchaseOrderHeader.csv
	•	PurchaseOrderDetail.csv
	•	Sales.csv (optional if you’re simulating sales)
	•	SalesTarget.csv (for monthly/quarterly targets)
	•	Customer.csv (for customer info)
	•	WeeklySalesSummary.csv (aggregated data if needed)

Why This Dataset?
	•	Realistic Business Structure: AdventureWorks simulates a manufacturing and sales environment with employees, products, vendors, purchase orders, etc.
	•	Multiple Tables & Relationships: Perfect for practicing SQL joins, foreign keys, and typical data warehouse or reporting tasks.
	•	Widely Known: AdventureWorks is a standard example in the SQL community, making it easy to demonstrate ETL best practices.

3. Output of the Pipeline

3.1. What the Pipeline Produces

After running the ETL scripts, we load cleaned and transformed data into MySQL. Some common reports or outputs include:
	•	Weekly Sales: Summaries of total revenue, total orders, average sale value, etc.
	•	Purchase Order Analysis: Which vendors supply which products, total spending per vendor, order statuses.
	•	Employee & Sales Performance: Using SalesTarget vs. actual Sales data to see which employees meet or exceed quotas.

3.2. Why the Output is Useful
	•	Business Insights: Helps managers make decisions on inventory, vendor negotiations, and employee performance.
	•	Automation: Weekly or daily reports reduce manual effort, ensuring stakeholders always have up-to-date metrics.
	•	Scalability: The pipeline design can be extended to other tables or additional data sources if the business grows.

4. Architecture Diagram

Below is a simplified architecture showing how data flows from CSV to MySQL and how it’s used for reporting.

         ┌──────────────┐
         │ CSV Datasets  │
         │(Employee.csv, │
         │ Vendor.csv,   │
         │ etc.)         │
         └─────┬─────────┘
               │
     (Extract) │
               ▼
     ┌────────────────┐
     │Python Scripts  │
     │(extract,transform,load) │
     └─────┬───────────────────┘
           │ (Transform/Load)
           ▼
     ┌─────────────────────────┐
     │     MySQL Database      │
     │ (Cleaned, Final Tables) │
     └─────┬───────────────────┘
           │
           │ (Query for Reports)
           ▼
     ┌─────────────────────────┐
     │   Automated Reports     │
     │ (Sales, PO, Employee,   │
     │  Weekly Summaries)      │
     └─────────────────────────┘

5. Final Schema Diagram

Below is the final schema representing the core tables and their relationships. (If you have a bridging table for ShipMethod ↔ Product or any other many-to-many, include it.)

Employee (EmployeeID PK)
Vendor (VendorID PK)
ShipMethod (ShipMethodID PK)
Product (ProductID PK)

PurchaseOrderHeader (PurchaseOrderID PK)
  - EmployeeID FK → Employee(EmployeeID)
  - VendorID FK → Vendor(VendorID)
  - ShipMethodID FK → ShipMethod(ShipMethodID)

PurchaseOrderDetail (PurchaseOrderDetailID PK)
  - PurchaseOrderID FK → PurchaseOrderHeader(PurchaseOrderID)
  - ProductID FK → Product(ProductID)

Sales (SaleID PK)
  - EmployeeID FK → Employee(EmployeeID)
  - CustomerID FK → Customer(CustomerID) [optional]

SalesTarget (SalesTargetID PK or composite (EmployeeID,Year,Month))
  - EmployeeID FK → Employee(EmployeeID)

WeeklySalesSummary (Year,Week) PK [no FKs typically]

Customer (CustomerID PK)

(If your design differs slightly—e.g., bridging tables for ShipMethod↔Product—adapt accordingly.)

6. Gaps in the System

6.1. Scalability
	•	Current Approach: A single MySQL instance might handle moderate data volumes well.
	•	Potential Bottlenecks: If the dataset grows significantly (millions of rows per day), the single-node MySQL approach or the Python-based ETL may slow down.
	•	Future Improvement:
	•	Sharding or partitioning large tables.
	•	Migrating to a more distributed system (e.g., Amazon Redshift or BigQuery).
	•	Using chunk-based or incremental loading to avoid full reloads.

6.2. Security
	•	At Present:
	•	Credentials are stored (ideally) in environment variables or AWS Secrets Manager if on AWS.
	•	MySQL is behind a firewall or security group.
	•	SSL/TLS connections can be enforced.
	•	Further Hardening:
	•	Use a private subnet (if in the cloud) so the DB is not publicly accessible.
	•	Implement role-based access for the MySQL user (read-only vs. admin).
	•	Add an audit trail or logging for queries if needed.

6.3. Extensibility
	•	Add New Tables: The schema can easily be extended with new CSV inputs (e.g., more AdventureWorks tables).
	•	Adjust Transformations: Python scripts are modular; new transform functions can be plugged in for new data.
	•	Different Outputs: We can add a BI dashboard, or store final data in a data warehouse for advanced analytics.

7. Conclusion

This design document outlines a production-ready data pipeline that:
	1.	Extracts AdventureWorks CSV data.
	2.	Transforms it using Python (cleaning, standardizing).
	3.	Loads the final tables into MySQL.
	4.	Provides weekly/daily reports on sales, purchase orders, employees, etc.

Strengths: Straightforward to run, easy to replicate, minimal overhead.
Gaps: May require more robust tooling if data volume skyrockets; security must be carefully managed.

With these design choices, the pipeline meets typical business needs for automated reporting, while leaving room for future expansion and improvements.

End of Document