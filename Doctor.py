import requests
import json

url = 'https://api.catalogopolis.xyz/v1/actors'
response = requests.get(url)
print(response.json())

