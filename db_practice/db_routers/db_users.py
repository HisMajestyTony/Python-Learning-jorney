from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db_config import get_db
from schemas import UserCreate
from db_services.db_user_service import create_user, get_all_users, get_user_by_id, del_user_by_id

router = APIRouter()

@router.post("/users")
def add_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.get("/users")
def get_users(db: Session = Depends(get_db)):
    return get_all_users(db)

@router.get("/users/{user_id}")
def get_user_id(user_id: int, db: Session = Depends(get_db)):
    return get_user_by_id(db, user_id)


@router.delete("/users/{user_id}")
def delete_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return del_user_by_id(db, user_id)
