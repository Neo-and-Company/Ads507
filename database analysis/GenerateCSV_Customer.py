import csv
import random
import datetime
import string

def random_date(start_year=2020, end_year=2024):
    """
    Returns a random date between Jan 1 of start_year and Dec 31 of end_year.
    """
    start = datetime.date(start_year, 1, 1)
    end = datetime.date(end_year, 12, 31)
    delta = end - start
    random_days = random.randrange(delta.days + 1)
    return start + datetime.timedelta(days=random_days)

def random_email(first_name, last_name):
    """
    Generates a simple email address from first/last name + random domain.
    """
    domains = ["gmail.com", "yahoo.com", "hotmail.com", "example.org", "mail.com"]
    domain = random.choice(domains)
    # Lowercase, remove spaces, add a random number
    user_part = f"{first_name.lower()}.{last_name.lower()}{random.randint(1,999)}"
    return f"{user_part}@{domain}"

def random_phone():
    """
    Generates a 10-digit phone number in a simple random format: 3-3-4.
    Example: 123-456-7890
    """
    return f"{random.randint(100,999)}-{random.randint(100,999)}-{random.randint(1000,9999)}"

def random_name():
    """
    Picks a random first/last name from a short list. 
    Feel free to expand or change the lists.
    """
    first_names = [
        "James", "Mary", "Robert", "Patricia", "John", "Jennifer", "Michael", 
        "Linda", "William", "Elizabeth", "David", "Barbara", "Richard", 
        "Susan", "Joseph", "Jessica", "Thomas", "Sarah", "Charles", "Karen"
    ]
    last_names = [
        "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller",
        "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez",
        "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin"
    ]
    return random.choice(first_names), random.choice(last_names)

def generate_customer_csv(filename="Customer.csv", num_records=200):
    """
    Generates a CSV file for the 'Customer' table with columns:
      CustomerID, FirstName, LastName, Email, Phone, CreatedDate, ModifiedDate
    """
    headers = [
        "CustomerID", 
        "FirstName", 
        "LastName", 
        "Email", 
        "Phone", 
        "CreatedDate", 
        "ModifiedDate"
    ]

    with open(filename, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)

        for cust_id in range(1, num_records + 1):
            first_name, last_name = random_name()
            email = random_email(first_name, last_name)
            phone = random_phone()

            # CreatedDate earlier than ModifiedDate
            created_date = random_date(2018, 2022)
            modified_date = created_date + datetime.timedelta(
                days=random.randint(0, 1000)
            )
            # Convert to ISO format
            created_date_str = created_date.isoformat()
            modified_date_str = modified_date.isoformat()

            row = [
                cust_id,
                first_name,
                last_name,
                email,
                phone,
                created_date_str,
                modified_date_str
            ]
            writer.writerow(row)

    print(f"Generated {num_records} customer records in {filename}.")

# Example usage
if __name__ == "__main__":
    generate_customer_csv("Customer.csv", num_records=200)