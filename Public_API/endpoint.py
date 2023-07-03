
import requests

requests = requests.get("") # Add website URL here... :)
data = requests.json()

print(data)
