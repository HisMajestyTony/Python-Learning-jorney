from sqlalchemy.orm import Session
from tm_models.task_table import TaskTable
from tm_shcemas.tm_schemas import TaskResponse, TaskCreate, TaskUpdate

def create_task(dbs: Session, task: TaskCreate):
    duplicate = dbs.query(TaskTable).filter(TaskTable.task_name == task.task_name).first()

    if duplicate:
        raise ValueError("Task already exists in DB")

    new_task = TaskTable(
        task_name=task.task_name,
        description=task.description,
        is_done=task.is_done,
        priority=task.priority
    )

    dbs.add(new_task)
    dbs.commit()
    dbs.refresh(new_task)

    return new_task

def get_all_tasks(dbs: Session):
    tasks = dbs.query(TaskTable).all()

    return [
        {

            "id": task.id,
            "task_name": task.task_name,
            "description": task.description,
            "is_done": task.is_done,
            "priority": task.priority
        }
        for task in tasks
    ]


