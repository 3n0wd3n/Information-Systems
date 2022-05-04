import requests
import json

url = "http://127.0.0.1:5000/holidays"
response = requests.get(url)
print(response.json())

data = {"day":24, "month":12, "name":"Stedry den"}
response = requests.post(url, json=data)
print(response.json())


for i in range(0,11):
    url = "http://127.0.0.1:5000/holidays/" + str(i)
    response = requests.get(url)
    print(response.json())


url = "http://127.0.0.1:5000/holidays/5"
response = requests.delete(url)
print(response.json())
