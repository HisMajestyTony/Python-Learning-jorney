import json

DATA_FILE = "users.json"

def load_users():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except:
        return []

def save_users(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)