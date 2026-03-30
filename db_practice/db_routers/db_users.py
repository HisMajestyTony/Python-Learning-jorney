

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from fastapi import HTTPException
from db_config import get_db
from db_models.book_table import BookTable
from db_models.user_table import UserTable
from schemas import UserCreate, MessageResponse, BookCreate, BookResponse, BookUpdate, UserWithBooksResponse
from db_services.db_user_service import create_user, get_all_users, get_user_by_id, del_user_by_id, get_update_user, \
    create_book, get_books, get_book, get_user_books, update_book

router = APIRouter()

@router.post("/books", response_model=BookResponse)
def create_book_route(book: BookCreate, db: Session = Depends(get_db)):
    return create_book(db, book)

@router.get("/books", response_model=list[BookResponse])
def get_books_route(db: Session = Depends(get_db)):
    return get_books(db)


@router.post("/users")
def add_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.get("/users")
def get_users(db: Session = Depends(get_db)):
    return get_all_users(db)

@router.get("/users/{user_id}/full", response_model=UserWithBooksResponse)
def get_user_with_books_route(user_id: int, db: Session = Depends(get_db)):
    user = db.query(UserTable).filter(UserTable.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user

@router.get("/books/{book_id}", response_model=BookResponse)
def get_book_route(book_id: int, db: Session = Depends(get_db)):
    return get_book(db, book_id)


@router.get("/users/{user_id}")
def get_user_id(user_id: int, db: Session = Depends(get_db)):
    return get_user_by_id(db, user_id)


@router.delete("/users/{user_id}")
def delete_user_by_id(user_id: int, db: Session = Depends(get_db)):
    return del_user_by_id(db, user_id)


@router.put("/users/{user_id}")
def update_user_route(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    return get_update_user(db, user_id, user)

@router.put("/books/{book_id}", response_model=BookResponse)
def update_book_route(book_id: int, book: BookUpdate, db: Session = Depends(get_db)):
    return update_book(db, book_id, book)

@router.get("/users/{user_id}/books", response_model=list[BookResponse])
def get_user_books_route(user_id: int, db: Session = Depends(get_db)):
    return get_user_books(db, user_id)


