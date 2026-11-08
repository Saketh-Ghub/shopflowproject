import csv
import os
import random
from datetime import date
prices = { "Headphones": 59.99,"Laptop": 799.99, "Mouse":19.99, "Keyboard": 49.99, "Monitor": 199.99}

currency_of = {"UK":"GBP", "Ireland": "EUR", "Germany": "EUR", "USA": "USD"}

orders =[]
for i in range(50):
    product = random.choice(list(prices))
    country = random.choice(list(currency_of))
    order = {
        "order_id":100+i,
        "order_date" : str(date.today()),
        "customer_id" :"C" + str(random.randint(100,999)),
        "country": country,
        "product" : product,
        "quantity" : random.randint(1,5),
        "unit_price" : prices[product],
        "currency" : currency_of[country],
    }
    
    if random.random() < 0.2:
        order["country"] = order["country"].lower()
    if random.random() < 0.2:
        order["unit_price"] = ""
    if random.random() <0.2:
        order["quantity"]   = -order["quantity"] 
    if random.random()<0.1:
        order["order_date"]  = date.today().strftime("%d/%m/%y")
    orders.append(order)
    if random.random()<0.1:
        orders.append(order.copy())
print(len(orders), "orders created") 

os.makedirs("data/raw",exist_ok = True)
file_path = "data/raw/orders"+str(date.today())+".csv"
with open(file_path, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=orders[0].keys())
    writer.writeheader()
    writer.writerows(orders)
print("Saved to ",file_path)    