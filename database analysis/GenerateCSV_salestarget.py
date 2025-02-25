import random
import csv

def generate_sales_target_csv(filename, start_year=2021, end_year=2024):
    """
    Generates a SalesTarget.csv file for 200 employees over multiple years (start_year to end_year).
    Each employee gets monthly targets for each month of each year in that range.
    """
    # We want 200 employees
    num_employees = 200

    # Prepare column headers
    headers = ["EmployeeID", "Year", "Month", "TargetSales", "AchievedSales"]

    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)

        for emp_id in range(1, num_employees + 1):
            # For each year in [start_year..end_year]
            for year in range(start_year, end_year + 1):
                # For each month in [1..12]
                for month in range(1, 13):
                    # Generate random sales target, achieved sales
                    target_sales = random.randint(5000, 20000)
                    achieved_sales = random.randint(4000, 21000)

                    # Write the row
                    row = [emp_id, year, month, target_sales, achieved_sales]
                    writer.writerow(row)

    print(f"Generated {filename} with sales targets for {num_employees} employees, {start_year}–{end_year}.")

# Usage example
if __name__ == "__main__":
    generate_sales_target_csv("SalesTarget.csv", 2021, 2024)