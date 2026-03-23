from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

class LoginRequest(BaseModel):
    username: str
    password: str


class User(BaseModel):
    name: str
    age: int

DATA_FILE = "users.json"


@app.get("/users/search")
def search_user(name: str):
    results = [
        user for user in users_db
        if name.lower() in user["name"].lower()
    ]

    if not results:
        return {"message": "No users found"}

    return results

def load_users():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except:
        return []

def save_users(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)



@app.post("/users")
def create_user(user: User):
    for u in users_db:
        if u in users_db:
            if u["name"] == user.name:
                return {"error": "User already exists"}

    users_db.append(user.dict())
    save_users(users_db)

    return {"message": "User added"}

@app.put("/users/{name}")
def update_age(name: str, age = int):
    for user in users_db:
        if user["name"] == name:
            user["age"] = age
            save_users(users_db)
            return {"message": "User's age updated"}
    return {"message": "User not found"}





@app.delete("/users/{name}")
def delete_user(name: str):
    for user in users_db:
        if user["name"] == name:
            users_db.remove(user)
            save_users(get_users)
            return {"message": "User deleted"}

    return {"error": "user not found"}

@app.get("/users")
def get_users():
    return users_db

@app.get("/")
def home():
    return {"message": "Hello Antonio"}


@app.get("/hello/{name}")
def say_hello(name):
    return {"message": f"Hello {name}"}


@app.get("/add/{a}/{b}")
def add(a: int, b: int):
    return {"result": a + b}


@app.get("/weather/{city}")
def get_weather(city):
    return {
        "city": city,
        "temperature": 20,
        "status": "Sunny"
    }

@app.get("/weather")
def get_weather(city: str = "sofia"):
    return {"city": city}

@app.get("/square/{num}")
def squaring(num: int):
    result = num * num
    return {"result": result}


@app.get("/user/{name}/{age}")
def age(name: str, age: int):
    return {"name": name, "age": age}

@app.get("/cars")
def cars(brand: str, year: int):
    return {"brand": brand, "year": year}

## LESION 3 .. POST + JSON

@app.post("/login")
def login(data: LoginRequest):
    if data.username == "admin" and data.password == "1234":
        return {"message": "Login Success"}
    return {"message": "Invalid credentials"}

users_db = load_users()






