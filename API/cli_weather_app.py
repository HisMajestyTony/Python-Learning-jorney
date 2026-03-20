
import os
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
        data = response.json()

        if "error" in data:
            return {
                "error": {
                    "type": "api",
                    "message": data["error"]["message"]
                }
            }

        return data

    except requests.exceptions.RequestException:
        return {
            "error": {
                "type": "network",
                "message": "Network error. Please try again."
            }
        }

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

def add_to_history(history, city_name):
    if city_name in history["history"]:
        history["history"].remove(city_name)

    history["history"].insert(0, city_name)

    history["history"] = history["history"][:3]

def c_or_f(unit):
    if unit not in ["C", "F"]:
        unit = "C"
    return unit


def show_history(history):
    print("---HISTORY---")

    for i, city in enumerate(history["history"], 1):
         print(f"{i}) {city}")
    print("---------------")

def is_history_empty(history):
    if not history["history"]:
        return True
    return False

def index_validation(index, history):

    try:
        index = int(index)

    except ValueError:
        return False

    if index < 1 or index > len(history["history"]):
        return False

    return True





def main():
    history = load_history()

    if "history" not in history:
        history["history"] = []

    if  history["history"]:
        show_history(history)

    while True:



        print("1. Enter city name: ")
        print("2. History")
        print("3. Clear history")
        print("0. Exit")


        option = input("Please select an option: ")

        if option == "1":
            city_name = input("Please enter city name: ").strip()

            cancelled = False

            while True:
                data = get_weather(city_name)

                if "error" not in data:
                    break

                print("Error:", data["error"]["message"])

                if data["error"]["type"] == "network":
                    retry = input("Retry request? (y / n): ").strip().lower()
                    if retry == "y":
                        continue

                if data["error"]["type"] == "api":
                    city_name = input("Please enter city name: ").strip()
                    continue

                cancelled = True
                break

            if cancelled:
                continue

            unit = input("Choose unit (C/F): ").strip().upper()
            unit = c_or_f(unit)

            choice = input("Do you wish to save to history? (y / n)").strip().lower()

            if choice == "y":
                add_to_history(history, city_name)
                save_history(history)
                print("History saved")
            elif choice != "n":
                print("Invalid input")

            display_weather(data, unit)
            display_forecast(data, unit)

        elif option == "2":
            if is_history_empty(history):
                print("History is empty")
                continue

            show_history(history)

            index = input("Please select city: ").strip()
            validation = index_validation(index, history)

            if validation:
                city_name = history["history"][int(index) - 1]

            else :
                print("Invalid input")
                continue
            data = get_weather(city_name)

            unit = input("Choose unit (C/F): ").strip().upper()
            unit = c_or_f(unit)

            display_weather(data,unit)
            display_forecast(data,unit)

        elif option == "3":
            if not history["history"]:
                print("History is empty")
                continue

            confirmation = input("Are you sure that you want to delete history? (y / n)").strip().lower()
            if confirmation == "y":
                history["history"] = []
                save_history(history)
                print("History deleted")
            elif confirmation == "n":
                continue
            else:
                print("Invalid input")



        elif option == "0":
            break

        else:
            print("Invalid input")







if __name__ == "__main__":
    main()