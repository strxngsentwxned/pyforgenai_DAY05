import csv

data = [
    {"name": "apple", "price": 3, "quantity": 2, "category":"fruits"},
    {"name": "carrot", "price": 5, "quantity": 3, "category":"vegetables"},
    {"name": "banana", "price": 2, "quantity": 4, "category":"fruits"},
]

with open("output.csv", "w", newline="") as file:
    fieldnames = ["name", "price", "quantity","category"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader() 
    writer.writerows(data)

with open("output.csv", "r") as file:
    reader = csv.DictReader(file)

    total_products = 0
    total_price = 0
    total_quantity = 0
    total_value = 0

    for row in reader:
        price = int(row["price"])
        quantity = int(row["quantity"])

        total_price += price 
        total_quantity += quantity
        total_value += price * quantity

    average_price = total_value / total_quantity if total_quantity else 0

    print("total_quantity:", total_quantity)
    print("total_value:", total_value)
    print("average_price (per product):", average_price)
    print("average_price (weighted):", average_price)



    
