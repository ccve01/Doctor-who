import requests
import json

url = 'https://api.catalogopolis.xyz/v1/doctors'
response = requests.get(url)
# print(response.json())
# print(response.json()[0].get('id'))
url2 = 'https://api.catalogopolis.xyz/v1/doctors/'+str(response.json()[0].get('id'))+'/actors'
response2 = requests.get(url2)
# print(response2.json())
# print(url2)
print(response.json()[0].get('incarnation'))
print(response2.json()[0].get('name'))