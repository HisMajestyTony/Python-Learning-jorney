from pydantic import BaseModel, Field




class TaskCreate(BaseModel):

    task_name: str = Field(min_length=2, max_length=30)
    description: str = Field(min_length=3, max_length=100)
    is_done: bool
    priority: str




class TaskResponse(BaseModel):
    id: int
    task_name: str
    description: str
    is_done: bool
    priority: str



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



