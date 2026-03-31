from pydantic import BaseModel, Field

from tm_models.task_table import TaskTable


class TaskCreate(BaseModel):

    task_name: str = Field(min_length=2, max_length=30)
    description: str = Field(min_length=3, max_length=100)
    is_done: bool
    priority: str

    model_config = {
        "from_attributes": True
    }



class TaskResponse(BaseModel):
    id: int
    task_name: str = Field(min_length=2, max_length=30)
    description: str = Field(min_length=3, max_length=100)
    is_done: bool
    priority: str



    model_config = {
        "from_attributes": True
    }

class TaskUpdate(BaseModel):
    description: str = Field(min_length=3, max_length=100)
    is_done: bool
    priority: str


