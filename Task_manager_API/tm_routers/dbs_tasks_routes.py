from fastapi import APIRouter, Depends , HTTPException
from sqlalchemy.orm import Session
from database_config import get_dbs
from tm_services.dbs_service import create_task, get_all_tasks, get_single_task, update_task, delete_task
from tm_shcemas.tm_schemas import TaskCreate, TaskUpdate, TaskResponse, TaskDeletedResponse



router = APIRouter()

@router.post("/tasks",response_model=TaskResponse)
def create_task_route(task: TaskCreate, dbs: Session = Depends(get_dbs)):
    try:
       return create_task(dbs, task)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/tasks", response_model=list[TaskResponse])
def get_all_tasks_route(dbs: Session = Depends(get_dbs)):
    return get_all_tasks(dbs)


@router.get("/tasks/{task_id}",response_model=TaskResponse)
def get_single_task_route(task_id: int, dbs: Session = Depends(get_dbs)):
    try:
        return get_single_task(task_id, dbs)
    except (ValueError, LookupError) as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task_route(task_id: int,task: TaskUpdate, dbs: Session = Depends(get_dbs)):
    try:
        return update_task(dbs, task_id, task)
    except LookupError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.delete("/tasks/{task_id}",response_model=TaskDeletedResponse)
def delete_task_route(task_id: int, dbs: Session = Depends(get_dbs)):
    try:
        return delete_task(task_id, dbs)
    except LookupError as e:
        raise HTTPException(status_code=404, detail=str(e))