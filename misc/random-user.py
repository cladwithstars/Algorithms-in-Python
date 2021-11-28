import json
import requests

response = requests.get('https://randomuser.me/api/?results=10')

data = response.json()

for user in data['results']:
    print(user['name']['first'])

items = json.loads('[{"id":1, "text": "Item 1"}, {"id":2, "text": "Item 2"}]')

