import json
from collections import defaultdict
import hashlib

DATA_FILE = "passwords.json"

def create_empty_data():
    return {"master_password_hash": "", "services": {}}


def hash_text(text):
    return hashlib.sha256(text.encode()).hexdigest()

def load_data():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError as err:
        return create_empty_data()

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def setup_master_password(data):
    pass

def verify_master_password(data):
    pass

def add_service(data):
    service = input("Enter service name: ").strip().lower()
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()
    note = input("Enter note: ").strip()


    data["services"][service] = {
        "username": username,
        "password": password,
        "note": note
    }
    save_data(data)
    print("Password was saved successfully")

def view_services(data):
    if not data["services"]:
        return "No services saved yet"

    for service in data["services"]:
        print(f"- {service}")
    return "Success"


def get_service_details(data):
    name = input("Enter service name: ").strip().lower()
    if name not in data["services"]:
        return "The service does not exist!"

    service = data["services"][name]
    username = service["username"]
    password = service["password"]
    note = service["note"]

    text = f"{name}\n{username}\n{password}\n{note}"

    return text

def delete_service(data):
    pass

def menu():
    pass

def main():
    pass

main()

data = create_empty_data()
add_service(data)

print(get_service_details(data))

