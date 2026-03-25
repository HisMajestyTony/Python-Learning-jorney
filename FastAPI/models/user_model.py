from pydantic import BaseModel, Field


class User(BaseModel):
    name: str = Field(min_length=3)
    age: int = Field(ge=1, le=120)



class MessageResponse(BaseModel):
    message: str

class UserUpdate(BaseModel):
    age: int

class CountResponse(BaseModel):
    count: int