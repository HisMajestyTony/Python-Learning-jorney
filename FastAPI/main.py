from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

from database import Base, engine, get_db
from models.user_db_model import UserDB

app = FastAPI()

# create tables
Base.metadata.create_all(bind=engine)


# ---------- Pydantic model (INPUT) ----------
class UserCreate(BaseModel):
    name: str
    age: int


# ---------- ROUTES ----------

@app.get("/")
def home():
    return {"message": "Database works"}


# GET all users
@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    users = db.query(UserDB).all()

    result = []
    for user in users:
        result.append({
            "id": user.id,
            "name": user.name,
            "age": user.age
        })

    return result


# POST create user
@app.post("/users")
def create_user(user: UserCreate, db: Session = Depends(get_db)):

    # check duplicate
    existing = db.query(UserDB).filter(UserDB.name == user.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="User already exists")

    new_user = UserDB(name=user.name, age=user.age)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "id": new_user.id,
        "name": new_user.name,
        "age": new_user.age
    }