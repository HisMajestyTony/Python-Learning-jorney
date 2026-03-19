
import os
from json import JSONDecodeError
from traceback import print_tb

from dotenv import load_dotenv
import requests
import json

HISTORY = "history.json"

load_dotenv()
api_key = os.getenv("API_KEY")

if not api_key:
    raise SystemExit("API key not found.")


def save_history(history):
    with open(HISTORY, "w") as file:
        json.dump(history, file, indent=4)

def load_history():
    try:
        with open(HISTORY, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def get_weather(city_name):
    url = "http://api.weatherapi.com/v1/forecast.json"

    params = {
        "key": api_key,
        "q": city_name,
        "days": 3
    }

    try:
        response = requests.get(url, params=params)
        return response.json()

    except requests.exceptions.RequestException:
        return {"error": {"message": "Network error. Please try again."}}

def display_weather(data, unit="C"):
    city = data["location"]["name"]
    country = data["location"]["country"]

    if unit == "F":
        temperature = data["current"]["temp_f"]
        feels_like = data["current"]["feelslike_f"]
        symbol = "°F"
    else:
        temperature = data["current"]["temp_c"]
        feels_like = data["current"]["feelslike_c"]
        symbol = "°C"

    condition = data["current"]["condition"]["text"]

    print("\n--- Weather ---")
    print(f"Location: {city}, {country}")
    print(f"Temperature: {temperature}{symbol}")
    print(f"Feels like: {feels_like}{symbol}")
    print(f"Condition: {condition}")
    print("----------------\n")

def display_forecast(data, unit="C"):

    forecast_days = data["forecast"]["forecastday"]

    if unit == "F":
        temp_key = "avgtemp_f"
        symbol = "°F"
        temp_max_key = "maxtemp_f"
        temp_min_key = "mintemp_f"
    else:
        temp_key = "avgtemp_c"
        symbol = "°C"
        temp_max_key = "maxtemp_c"
        temp_min_key = "mintemp_c"

    print("\n--- 3 Day Forecast ---")
    for day in forecast_days[1:]:

        print(f"Date: {day['date']}")
        print(f"Temperature: {day['day'][temp_key]}{symbol}")
        print(f"Maximum temperature: {day['day'][temp_max_key]}{symbol}")
        print(f"Minimum temperature: {day['day'][temp_min_key]}{symbol}")
        print(f"Condition: {day['day']['condition']['text']}")







def main():
    history = load_history()

    if "history" not in history:
        history["history"] = []



    while True:


        print("1. Enter city name")
        print("2. TODO")
        print("0. Exit")


        options = input("Please select an option")

        choice = input("Do you wish to save to history? (y / n)").strip().lower()
        if choice == "y":
            save_history(history)
            print("History saved")
        elif choice == "n":
            continue
        else:
            print("Invalid input")

        if options == "1":
            city_name = input("Please enter city name: ").strip()
            if city_name in history["history"]:
                history["history"].remove(city_name)
                history["history"].insert(0, city_name)
            else:
                history["history"].insert(0 ,city_name)

            if len(history["history"]) > 3:
                history["history"].pop()

            data = get_weather(city_name)

            if "error" in data:
                print("Error:", data["error"]["message"])
                continue

            unit = input("Choose unit (C/F): ").strip().upper()

            if unit not in ["C", "F"]:
                unit = "C"

            display_weather(data, unit)
            display_forecast(data,unit)





        elif options == "0":
            break

        else:
            print("Invalid input")







if __name__ == "__main__":
    main()





