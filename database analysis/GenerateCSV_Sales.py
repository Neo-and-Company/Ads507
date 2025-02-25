import csv
import random
import datetime

def random_date(start_year=2021, end_year=2024):
    """
    Returns a random date between Jan 1 of start_year and Dec 31 of end_year.
    """
    start = datetime.date(start_year, 1, 1)
    end = datetime.date(end_year, 12, 31)
    # Generate a random day offset
    delta = end - start
    random_days = random.randrange(delta.days + 1)
    return start + datetime.timedelta(days=random_days)

def generate_sales_csv(filename, num_records=10000, start_year=2021, end_year=2024):
    """
    Generates a Sales.csv with columns:
      SaleID, EmployeeID, SaleAmount, SaleDate
    Over a date range from start_year to end_year.
    """
    headers = ["SaleID", "EmployeeID", "SaleAmount", "SaleDate"]
    
    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)

        for sale_id in range(1, num_records + 1):
            # Random employee among 200 possible
            employee_id = random.randint(1, 200)

            # Random sale amount between $10 and $5,000
            sale_amount = round(random.uniform(10, 5000), 2)

            # Random sale date between start_year and end_year
            sale_date = random_date(start_year, end_year).isoformat()

            row = [sale_id, employee_id, sale_amount, sale_date]
            writer.writerow(row)

    print(f"Generated {filename} with {num_records} sales records for years {start_year}–{end_year}.")

# Example usage:
if __name__ == "__main__":
    generate_sales_csv("Sales.csv", num_records=10000, start_year=2021, end_year=2024)