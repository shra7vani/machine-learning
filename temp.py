import json
import requests
city_name=input("enter city name:")
api_key='2a15dc6a09a1bac0a2d9778f0750a4df'
api_url=f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&metric'
get_server_info=requests.get(api_url)
print(get_server_info.json())