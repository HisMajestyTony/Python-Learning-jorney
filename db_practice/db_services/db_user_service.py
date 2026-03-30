from sqlalchemy.orm import Session
from fastapi import  HTTPException

from db_models.user_table import UserTable
from db_models.book_table import BookTable
from schemas import UserCreate


def create_user(db: Session, user: UserCreate):
    existing = db.query(UserTable).filter(UserTable.name == user.name).first()

    if existing:
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

def get_all_users(db: Session):
    users = db.query(UserTable).all()

    return [
        {"id": user.id, "name": user.name, "age": user.age}
        for user in users
    ]

def get_user_by_id(db: Session, user_id):
    user = db.query(UserTable).filter(UserTable.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {"id": user.id, "name": user.name, "age": user.age}

def del_user_by_id(db: Session, user_id: int):
    user = db.query(UserTable).filter(UserTable.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()

    return {"message": "User deleted"}

def get_update_user(db: Session, user_id: int, updated_user: UserCreate):
    user = db.query(UserTable).filter(UserTable.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user.name = updated_user.name
    user.age = updated_user.age

    db.commit()
    db.refresh(user)

    return {
        "id": user.id,
        "name": user.name,
        "age": user.age
    }

def get_version():
    return "v1.0"









