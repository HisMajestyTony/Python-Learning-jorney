from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel

from db_config import DBBase, db_engine, get_db, DBSession
from models.user_table import UserTable

#FastAPI app
app = FastAPI()

#STEP 2 - IMPORT DB STUFF

#STEP 3 - CREATE TABLES
DBBase.metadata.create_all(bind=db_engine)

class UserInput(BaseModel):
    name: str
    age: int

#STEP 4 - test route
@app.get("/")
def home():
    return {"message": "DB practice works"}

@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    users = db.query(UserTable).all()

    result = []
    for user in users:
        result.append({
            "id": user.id,
            "name": user.name,
            "age": user.age
        })

    return result


@app.post("/users")
def create_user(user: UserInput, db: Session = Depends(get_db)):

    existing_user = db.query(UserTable).filter(UserTable.name == user.name).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    new_user = UserTable(name=user.name, age=user.age)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        "id": new_user.id,
        "name": new_user.name,
        "age": new_user.age
    }
