# 🟢 Level 1 — Easy (just getting started)
# =======================================

# Q1. You have this JSON string:
# json_str = '{"name": "Sara", "age": 20, "city": "Karachi"}'
# Convert it to a Python dictionary and print the city value.

import json

json_str = '{"name": "Sara", "age": 20, "city": "Karachi"}'

data = json.loads(json_str)
print(data["city"])

# Q2. You have this Python dictionary:
# person = {"name": "Hamza", "age": 30, "is_student": False}
# Convert it to a JSON string and print it.
import json

person = {"name": "Hamza", "age": 30, "is_student": False}

data = json.dumps(person, indent=4)
print(data)


# 🟡 Level 2 — Mid (thinking required 🧠)
# =======================================

# Q3. You have this nested JSON string:
# json_str = '{"student": {"name": "Ali", "grades": {"math": 90, "english": 85}}}'
# Parse it and print the math grade.
import json

json_str = '{"student": {"name": "Ali", "grades": {"math": 90, "english": 85}}}'

data = json.loads(json_str)
print(data["student"]["grades"]["math"])

# Q4. Convert this list of dictionaries to a pretty-printed JSON string with indent=4 and sort_keys=True:
# employees = [
#     {"name": "Zara", "dept": "HR", "salary": 50000},
#     {"name": "Emily", "dept": "IT", "salary": 80000},
#     {"name": "Nadia", "dept": "Finance", "salary": 60000}
# ]
import json

employees = [
    {"name": "Zara", "dept": "HR", "salary": 50000},
    {"name": "Emily", "dept": "IT", "salary": 80000},
    {"name": "Nadia", "dept": "Finance", "salary": 60000}
]

data = json.dumps(employees, indent=4, sort_keys=True)
print(data)


# 🔴 Level 3 — Hard (big brain mode 💀)
# =======================================

# Q5. Handle this broken JSON safely without crashing the program, and print a friendly error message:
# broken = '{"name": "Ali", "age": 25, city: "Lahore"}'

import json

broken = '{"name": "Ali", "age": 25, city: "Lahore"}'

try:
    data = json.loads(broken)
    print(data)
except json.JSONDecodeError:
    print("Invalid JSON format. Please check your data.")


# Q6. You have this JSON file products.json:
# [
#   {"id": 1, "name": "Laptop", "price": 150000, "in_stock": true},
#   {"id": 2, "name": "Mouse", "price": 2000, "in_stock": false},
#   {"id": 3, "name": "Keyboard", "price": 5000, "in_stock": true},
#   {"id": 4, "name": "Monitor", "price": 80000, "in_stock": true}
# ]
# Write a program that:

# Loads the file
# Prints only items that are in_stock
# Prints the total price of all in-stock items

import json

with open("products.json", "r", encoding="utf-8") as f:
    products =json.load(f)

total_price = 0

for item in products:
    if item["in_stock"]:
        print(item)
        total_price += item["price"]

print("Total price of in-stock items:", total_price)

