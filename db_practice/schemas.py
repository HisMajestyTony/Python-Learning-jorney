from pydantic import BaseModel,Field
from typing import List

class UserCreate(BaseModel):
    name: str = Field(min_length=2, max_length=30)
    age: int = Field(ge=0, le=120)


class BookCreate(BaseModel):
    title: str
    pages: int
    user_id: int

class BookResponse(BaseModel):
    id: int
    title: str
    pages: int
    user_id: int

    model_config = {
        "from_attributes": True
    }

class BookUpdate(BaseModel):
    title: str
    pages: int


class MessageResponse(BaseModel):
    message: str

class UserWithBooksResponse(BaseModel):
    id: int
    name: str
    age: int
    books: List[BookResponse]

    model_config = {
        "from_attributes": True
    }

