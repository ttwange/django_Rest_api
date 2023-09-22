#Use this file as a consumer api file

import requests, json

url_drink = "http://127.0.0.1:8000/drinks/api/"
url_todos = "http://127.0.0.1:8000/todos/api/"

data = requests.get(url_drink)

data_drink = data.json()
    
print(json.dumps(data_drink, indent=4))  # Pretty-print for readability
