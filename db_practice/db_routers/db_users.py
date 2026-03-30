

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db_config import get_db
from db_models.book_table import BookTable
from schemas import UserCreate, MessageResponse, BookCreate, BookResponse
from db_services.db_user_service import create_user, get_all_users, get_user_by_id, del_user_by_id, get_update_user

router = APIRouter()

@router.post("books", response_model=BookResponse)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    new_book = BookTable(
        title=book.title,
        pages=book.pages
    )

    db.add(new_book)
    db.commit()
    db.refresh(new_book)


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


@router.put("/users/{user_id}")
def update_user_route(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    return get_update_user(db, user_id, user)

