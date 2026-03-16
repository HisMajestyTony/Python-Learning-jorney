import json

# # SAVING DATA TO A JSON FILE
# transactions = {
#     "2026-01": {"income": 2000, "expense": 500},
#     "2026-02": {"income": 2200, "expense": 700}
# }
#
# with open("data.json" , "w") as file:
#     json.dump(transactions,file, indent=4)
#
# # LOADING JSON BACK TO PYTHON
# with open("data.json", "r") as file:
#     data = json.load(file)
#
# print(data["2026-01"])

# movies = {
#     "Inception": 9,
#     "Interstellar": 10,
#     "The Dark Knight": 10
# }
#
# with open("movies.json", "r") as file:
#     movies = json.load(file)
#
# movies["Dune"] = 9
#
# with open("movies.json", "w") as file:
#     json.dump(movies, file, indent=4)
#


transactions = [
    {"type": "income", "amount": 2000},
    {"type": "expense", "amount": 500}
]

with open("transactions.json", "w") as file:
    json.dump(transactions, file, indent=4)

with open("transactions.json", "r") as file:
    transactions = json.load(file)

# ACCESSING ELEMENTS
print(transactions[0])

# ACCESSING VALUES
print(transactions[0]["amount"])

# ADDING NEW DATA 1 - LOAD / 2 - MODIFY / 3 - SAVE
with open("transactions.json", "r") as file:
    transactions = json.load(file)

transactions.append({"type": "expense", "amount": 300})
transactions.append({"type": "income", "amount": 1000})

with open("transactions.json", "w") as file:
    json.dump(transactions, file, indent=4)



# LOOP THRU JSON DATA
# total = 0
# for t in transactions:
#    # print(t["type"], t["amount"])
#     if t["type"] == "income":
#         total+= t["amount"]
# BOTH ARE CORRECT BUT COMPREHENSIONS ARE MORE PYTONIC


total = sum(t["amount"] for t in transactions if t["type"] == "income")

print(f"Total income: {total}")

# THE BIG BEGINNER MISTAKE - DO NOT APPEND ( "a" ) . The file becomes corrupted
# with open("transactions.json", "a") as file:
#     json.dump(new_transaction, file)
#
    #CORRECT METHODS
    #load
    #modify
    #overwrite file

# CORRECT WAY TO DO IT
# transactions = json.load(file)
#
# transactions.append(new_transaction)
#
# json.dump(transactions, file)


FILE_NAME = "transactions.json"


def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

#EXAMPLE REAL CLI LOGIC

def add_transaction(amount, type):
    data = load_data()

    data.append({
        "type": type,
        "amount": amount
    })

    save_data(data)