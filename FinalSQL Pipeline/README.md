# AdventureWorks507 ETL Pipeline

This repository provides a fully functional Extract → Transform → Load (ETL) pipeline for AdventureWorks data. It downloads CSV files from GitHub, transforms them using Python and pandas, and then loads the data into a MySQL database (local or AWS RDS).

---

## Table of Contents
- [AdventureWorks507 ETL Pipeline](#adventureworks507-etl-pipeline)
  - [Table of Contents](#table-of-contents)
  - [Project Structure](#project-structure)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Environment Variables](#environment-variables)
  - [Running the Pipeline](#running-the-pipeline)
  - [ETL Steps](#etl-steps)
    - [Extract Step](#extract-step)
    - [Transform Step](#transform-step)
    - [Load Step](#load-step)
  - [Automation via GitHub Actions](#automation-via-github-actions)
  - [Troubleshooting](#troubleshooting)
  - [License](#license)

---

## Project Structure

```
AdventureWorks507/
├── .vscode/
│   └── settings.json
├── data/
│   ├── PurchaseOrderHeader.csv
│   ├── PurchaseOrderDetail.csv
│   ├── ShipMethod.csv
│   ├── Customers.csv
│   ├── SalesOrderDetail.csv
│   ├── SalesTerritory.csv
│   ├── Employee.csv
│   └── ... 
├── Team Presentations/
├── sql/
│   ├── Ads507.session.sql
│   ├── transformations.sql
│   └── ...
├── scripts/
│   └── run_pipeline.py       # Main script orchestrating the ETL process
├── src/
│   ├── __init__.py
│   ├── extract/
│   │   ├── __init__.py
│   │   └── extract.py        # Functions: fetch_csv_from_github(), extract_all_data()
│   ├── transform/
│   │   ├── __init__.py
│   │   └── transform.py      # Clean and transform functions for DataFrames
│   └── load/
│       ├── __init__.py
│       └── load.py         # Function: load_data_to_mysql() to push data into MySQL
├── requirements.txt          # Dependency list
└── README.md 
```

> **Note:** Ensure every folder under `src/` includes an `__init__.py` file (even if empty) so they are treated as Python packages.

---

## Prerequisites

- **Python:** Version 3.11 or compatible.
- **Database:** MySQL (local or AWS RDS) with proper host/port configuration.
- **Git:** To clone the repository.

---

## Installation

1. **Clone the Repository:**
   ```
   git clone https://github.com/dnguyen-1/AdventureWorks507.git
   cd AdventureWorks507
   ```

2. **Install Dependencies:**
   ```
   pip install -r requirements.txt
   ```
   This command installs necessary packages such as pandas, requests, sqlalchemy, and pymysql.

---

## Environment Variables

Configure your database credentials by setting the following environment variables:

```bash
export RDS_USER="your_username"
export RDS_PASS="your_password"
export RDS_HOST="your_host"
export RDS_DBNAME="your_database"
```

Alternatively, you can use a `.env` file along with python-dotenv.

---

## Running the Pipeline

Execute the following command from the project root:

```bash
python scripts/run_pipeline.py
```

The script will:

1. **Extract:** Retrieve CSV files from GitHub.
2. **Transform:** Clean and modify DataFrames (e.g., renaming columns, handling missing values).
3. **Load:** Import the DataFrames into the MySQL database using SQLAlchemy.

Console logs will display progress messages similar to:
```
Extracted Customer.csv: shape = (1000, 7)
Extracted Employee.csv: shape = (290, 16)
...
Loaded 'Customer' into database 'AdventureSales' successfully.
...
ETL pipeline completed successfully.
```

---

## ETL Steps

### Extract Step
Located in `src/extract/extract.py`, this step:
- Fetches CSV files from GitHub.
- Reads the content into pandas DataFrames.
- Provides a dictionary of DataFrames, e.g., 

```python
{
  "Customer.csv": <DataFrame>,
  "Employee.csv": <DataFrame>,
  ...
}
```

### Transform Step
Contained in `src/transform/transform.py`, the transformation process:
- Cleans DataFrames by renaming columns and filling missing values.
- Uses specific functions like `transform_purchaseorderdetail(df)` for targeted updates.
- Returns a new dictionary of cleaned DataFrames.

### Load Step
Found in `src/load/load.py`, this step:
- Reads configuration from environment variables.
- Creates a SQLAlchemy engine.
- Uses `df.to_sql(table_name, if_exists="replace", index=False)` to load data into MySQL.
- Logs success messages upon completion.

---

## Automation via GitHub Actions

To run the ETL pipeline automatically on pushes or on a scheduled basis, create a workflow file at `.github/workflows/etl.yml`:

```yaml
name: ETL Pipeline
on:
  push:
    branches: [ "main" ]
  schedule:
    - cron: '0 0 * * *'  # daily at midnight UTC

jobs:
  run-etl:
    runs-on: ubuntu-latest
    steps:
      - name: Check out code
        uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.11"

      - name: Install dependencies
        run: |
          pip install -r requirements.txt

      - name: Run pipeline
        env:
          RDS_USER: ${{ secrets.RDS_USER }}
          RDS_PASS: ${{ secrets.RDS_PASS }}
          RDS_HOST: ${{ secrets.RDS_HOST }}
          RDS_DBNAME: ${{ secrets.RDS_DBNAME }}
        run: |
          python scripts/run_pipeline.py
```

Store your database credentials securely under GitHub secrets.

---

## Troubleshooting

- **ModuleNotFoundError (`src`):**
  - Ensure each folder (e.g., `src`, `extract`, `transform`, `load`) contains an `__init__.py` file.
  - Run the script from the project root directory.

- **NameError (e.g., `PurchaseOrderDetail` not defined):**
  - Avoid any global DataFrame references.
  - Use functions that receive DataFrame arguments.

- **HTTPError 404 Not Found:**
  - Verify that CSV filenames exactly match those on GitHub.
  - Check the delimiter used (tab vs comma).

- **MySQL Connection/Timeout Issues:**
  - Validate your MySQL security settings (AWS RDS or local).
  - Confirm the environment variable `RDS_HOST` points to the correct endpoint.

---

## License

This project is licensed under the MIT License. For more details, see the LICENSE file.

Happy ETLing!