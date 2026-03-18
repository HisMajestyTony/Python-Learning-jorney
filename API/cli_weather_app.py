from os import name
import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()
api_key = os.getenv("API_KEY")

url  = "http://api.weatherapi.com/v1/current.json"

params = {
    "key": api_key,
    "q": "Sofia"
}

response = requests.get(url, params=params)

data = response.json()

city = data["location"]["name"]
temperature =  data["current"]["temp_c"]
condition = data["current"]["condition"]["text"]

print(city)
print(temperature)
print(condition)
