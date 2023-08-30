import requests

api_key = "9b5cf919e87ea734278768c5d3adf1bf"

url =f"http://api.openweathermap.org/data/2.5/weather?q=London&APPID={api_key}"

get_requests = requests.get(url)
print(get_requests.json()['sys']['type'])
