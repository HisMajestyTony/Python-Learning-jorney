from sqlalchemy.orm import Session
from fastapi import  HTTPException

from db_models.user_table import UserTable
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

def del_user_by_id(db: Session, user_id):
    user = db.query(UserTable).filter(UserTable.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db.delete(user)
    db.commit()

    return {"User deleted"}

