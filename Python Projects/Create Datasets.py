import pandas as pd
import numpy as np
import os
from faker import Faker
import random

fake = Faker()
np.random.seed(42)

# -----------------------------
# 1. REGIONS (100 rows)
# -----------------------------
regions = []
countries = ["USA", "Canada", "UK", "Germany", "India"]
for i in range(100):
    regions.append({
        "region_id": f"R{i+1:03}",
        "country": random.choice(countries),
        "state": fake.state(),
        "city": fake.city()
    })

regions_df = pd.DataFrame(regions)

# -----------------------------
# 2. CUSTOMERS (100 rows)
# -----------------------------
customers = []
for i in range(100):
    customers.append({
        "customer_id": f"C{i+1:03}",
        "customer_name": fake.name(),
        "gender": random.choice(["M", "F"]),
        "age": random.randint(18, 70),
        "region_id": random.choice(regions_df["region_id"]),
        "signup_date": fake.date_between(start_date="-5y", end_date="today")
    })

customers_df = pd.DataFrame(customers)

# -----------------------------
# 3. PRODUCTS (100 rows)
# -----------------------------
categories = {
    "Electronics": ["Mobile", "Computers", "Accessories"],
    "Furniture": ["Office", "Home"],
    "Clothing": ["Men", "Women"],
    "Appliances": ["Kitchen", "Home"]
}

products = []
for i in range(100):
    category = random.choice(list(categories.keys()))
    products.append({
        "product_id": f"P{i+1:03}",
        "product_name": fake.word().capitalize(),
        "category": category,
        "sub_category": random.choice(categories[category]),
        "price": round(random.uniform(20, 2000), 2)
    })

products_df = pd.DataFrame(products)

# -----------------------------
# 4. ORDERS (100 rows)
# -----------------------------
orders = []
for i in range(100):
    orders.append({
        "order_id": f"O{i+1:04}",
        "customer_id": random.choice(customers_df["customer_id"]),
        "order_date": fake.date_between(start_date="-2y", end_date="today"),
        "order_status": random.choice(["Completed", "Cancelled", "Pending"])
    })

orders_df = pd.DataFrame(orders)


# -----------------------------
# 5. ORDER ITEMS (100 rows)
# -----------------------------
order_items = []
for i in range(100):
    order_items.append({
        "order_item_id": f"OI{i+1:04}",
        "order_id": random.choice(orders_df["order_id"]),
        "product_id": random.choice(products_df["product_id"]),
        "quantity": random.randint(1, 5),
        "discount": round(random.choice([0, 0.05, 0.10, 0.15, 0.20]), 2)
    })

order_items_df = pd.DataFrame(order_items)

# -----------------------------
# 6. PAYMENTS (100 rows)
# -----------------------------
payments = []
for i in range(100):
    payments.append({
        "payment_id": f"PM{i+1:04}",
        "order_id": random.choice(orders_df["order_id"]),
        "payment_method": random.choice(
            ["Credit Card", "Debit Card", "PayPal", "Bank Transfer"]
        ),
        "amount_paid": round(random.uniform(50, 5000), 2),
        "payment_date": fake.date_between(start_date="-2y", end_date="today")
    })

payments_df = pd.DataFrame(payments)

# -----------------------------
# SAVE TO CSV
# -----------------------------

main_folder = os.path.dirname(__file__)
datasets_path = os.path.join(main_folder, "Datasets")

regions_df.to_excel(rf"{datasets_path}\regions.xlsx", sheet_name = 'Regions', index=False)
customers_df.to_excel(rf"{datasets_path}\customers.xlsx", sheet_name = 'Customers', index=False)
products_df.to_excel(rf"{datasets_path}\products.xlsx", sheet_name = 'Products', index=False)
orders_df.to_excel(rf"{datasets_path}\orders.xlsx", sheet_name = 'Orders', index=False)
order_items_df.to_excel(rf"{datasets_path}\order_items.xlsx", sheet_name = 'Order_Items', index=False)
payments_df.to_excel(rf"{datasets_path}\payments.xlsx", sheet_name = 'Payments', index=False)

print("All datasets generated successfully")
