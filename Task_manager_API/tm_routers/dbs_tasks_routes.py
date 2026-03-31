from fastapi import APIRouter, Depends , HTTPException
from sqlalchemy.orm import Session
from database_config import get_dbs
from tm_models.task_table import TaskTable
from tm_services.dbs_service import create_task, get_all_tasks
from tm_shcemas.tm_schemas import TaskCreate, TaskUpdate, TaskResponse
#from tm_services.dbs_service import


router = APIRouter()

@router.post("/tasks",response_model=TaskResponse)
def create_task_route(task: TaskCreate, dbs: Session = Depends(get_dbs)):
    try:
       return create_task(dbs, task)
    except:
        raise HTTPException(status_code=400, detail="Could not create new task")


@router.get("/tasks", response_model=list[TaskResponse])
def get_all_tasks_route(dbs: Session = Depends(get_dbs)):
    return get_all_tasks(dbs)