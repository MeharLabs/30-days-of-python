import json

with open("products.json", "r", encoding="utf-8") as f:
    products = json.load(f)

total_price = 0

for item in products:
    if item["in_stock"]:
        print(item)
        total_price += item["price"]

print("Total price of in-stock items:", total_price)