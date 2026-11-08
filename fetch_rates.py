import requests
import json
import os

url = "https://api.frankfurter.dev/v1/latest?base=GBP&symbols=EUR,USD"

response = requests.get(url)
data = response.json()

os.makedirs("data/raw", exist_ok=True)
file_path = "data/raw/rates_" + data["date"] + ".json"

with open(file_path, "w") as f:
    json.dump(data, f)

print("Saved to", file_path)