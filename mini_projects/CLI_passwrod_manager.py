import json
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
    except FileNotFoundError:
        return create_empty_data()

def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

def setup_master_password(data):
    master_pass = input("Please create master password: ").strip()
    confirm_pass = input("Please confirm your master password: ").strip()

    if master_pass == confirm_pass:
        hashed_pass = hash_text(master_pass)
        data["master_password_hash"] = hashed_pass
        save_data(data)
        return print("Password saved")
    else:
        return print("Invalid password")


def verify_master_password(data):

    tries = 3

    while tries > 0:
        try_password = input("Please enter your master password: ")

        hashed_pass = hash_text(try_password)


        if hashed_pass == data["master_password_hash"]:
            return True


        else:
            tries -= 1
            print("Access denied")
            print(f"{tries} Tries left")

        if tries == 0:
            return False

    return True

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
    print("Service was saved successfully")

def view_services(data):
    if not data["services"]:
        print("No services saved yet")
        return

    print("----- Saved Services -----")

    for i, service in enumerate(data["services"], start=1):
        print(i, service)


def get_service_details(data):
    name = input("Enter service name: ").strip().lower()
    if name not in data["services"]:
        return print("Service not found")

    service = data["services"][name]
    username = service["username"]
    password = service["password"]
    note = service["note"]

    text = (f"Service: {name}\n"
            f"Username: {username}\n"
            f"Password: {password}\n"
            f"Note: {note}")

    return print(text)

def delete_service(data):
    name = input("Please enter the service you wish to delete: ").strip().lower()

    if name not in data["services"]:
        return print("Service not found")

    else:
        data["services"].pop(name)
        save_data(data)
        return print("Service deleted successfully")





def menu():
    data = load_data()

    if data["master_password_hash"] == "":
        setup_master_password(data)


    else:
        if verify_master_password(data):
            print("Access granted")
        else:
            return print("Access denied")



    while True:

        print("--- Password Manager---")
        print("1. Add new service")
        print("2. View all services")
        print("3. Get service details")
        print("4. Delete service")
        print("0. Exit")

        option = input("Please select an option: ").strip()

        if option == "1":
            add_service(data)

        elif option == "2":
            view_services(data)

        elif option == "3":
            get_service_details(data)

        elif option == "4":
            delete_service(data)


        elif option == "0":
            break

        else :
            print("Invalid option")



def main():
    menu()

if __name__ == '__main__':
    main()






