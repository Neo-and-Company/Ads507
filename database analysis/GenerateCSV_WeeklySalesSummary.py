import random
import csv

def generate_weekly_sales_summary_csv(filename, start_year=2021, end_year=2024):
    """
    Generates a WeeklySalesSummary.csv for the given range of years.
    Each year has 52 weeks, producing (end_year - start_year + 1)*52 rows.
    Columns: Year, Week, TotalSales, TotalOrders, AvgSaleValue
    """
    headers = ["Year", "Week", "TotalSales", "TotalOrders", "AvgSaleValue"]
    
    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)

        for year in range(start_year, end_year + 1):
            for week in range(1, 53):  # weeks 1..52
                # Generate random totals
                total_sales = round(random.uniform(5000, 200000), 2)
                total_orders = random.randint(10, 2000)
                avg_sale_value = round(total_sales / total_orders, 2)
                
                row = [year, week, total_sales, total_orders, avg_sale_value]
                writer.writerow(row)

    print(f"Generated {filename} with weekly sales summaries for {start_year}–{end_year}.")

# Example usage:
if __name__ == "__main__":
    generate_weekly_sales_summary_csv("WeeklySalesSummary.csv", 2021, 2024)