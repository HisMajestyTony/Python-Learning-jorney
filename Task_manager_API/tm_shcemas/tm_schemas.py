from pydantic import BaseModel, Field




class TaskCreate(BaseModel):

    task_name: str = Field(min_length=2, max_length=30)
    description: str = Field(min_length=3, max_length=100)
    is_done: bool = False
    priority: str
    category_id: int




class TaskResponse(BaseModel):
    id: int
    task_name: str
    description: str
    is_done: bool
    priority: str
    category_id: int



    model_config = {
        "from_attributes": True
    }

class TaskUpdate(BaseModel):
    description: str = Field(min_length=3, max_length=100)
    is_done: bool
    priority: str


class TaskDeletedResponse(BaseModel):
    id: int
    task_name: str
    message: str


class CategoryCreate(BaseModel):
    name:  str


class CategoryResponse(BaseModel):
    id: int
    name: str

    model_config = {
        "from_attributes": True
    }



