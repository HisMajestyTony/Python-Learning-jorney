from pydantic import BaseModel,Field

class UserCreate(BaseModel):
    name: str = Field(min_length=2, max_length=30)
    age: int = Field(ge=0, le=120)


class BookCreate(BaseModel):
    title: str
    pages: int

class BookResponse(BaseModel):
    title: str
    pages: int


class MessageResponse(BaseModel):
    message: str