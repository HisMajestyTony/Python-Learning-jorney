from sqlalchemy.orm import Session

from tm_models.category_table import CategoryTable
from tm_models.task_table import TaskTable
from tm_shcemas.tm_schemas import TaskCreate, TaskUpdate, CategoryCreate


def create_task(dbs: Session, task: TaskCreate):
    duplicate = dbs.query(TaskTable).filter(TaskTable.task_name == task.task_name).first()

    if duplicate:
        raise ValueError("Task already exists in DB")

    category = dbs.query(CategoryTable).filter(CategoryTable.id == task.category_id).first()
    if not category:
        raise ValueError("Category not found")

    new_task = TaskTable(
        task_name=task.task_name,
        description=task.description,
        is_done=task.is_done,
        priority=task.priority,
        category_id=task.category_id
    )

    dbs.add(new_task)
    dbs.commit()
    dbs.refresh(new_task)

    return new_task


def create_category(dbs: Session, category: CategoryCreate):
    duplicate_category = dbs.query(CategoryTable).filter(CategoryTable.name == category.name).first()
    if duplicate_category:
        raise ValueError("Category already exists")

    new_category = CategoryTable(name=category.name)

    dbs.add(new_category)
    dbs.commit()
    dbs.refresh(new_category)

    return new_category


def get_all_tasks(dbs: Session):
    return dbs.query(TaskTable).all()


def get_single_task(task_id: int, dbs: Session):
    if task_id <= 0:
        raise ValueError("Task ID cannot be less than 0")



    task = dbs.query(TaskTable).filter(TaskTable.id == task_id).first()

    if not task:
        raise LookupError("Task not found")

    return task

def update_task(dbs: Session,task_id: int,  updated_task: TaskUpdate):
    task = dbs.query(TaskTable).filter(TaskTable.id == task_id).first()

    if not task:
        raise LookupError("Task not found")

    task.description = updated_task.description
    task.is_done = updated_task.is_done
    task.priority = updated_task.priority

    dbs.commit()
    dbs.refresh(task)

    return task

def delete_task(task_id: int, dbs: Session):
    task = dbs.query(TaskTable).filter(TaskTable.id == task_id).first()

    if not task:
        raise   LookupError("Task not found")

    dbs.delete(task)
    dbs.commit()

    return {
        "id": task.id,
        "task_name": task.task_name,
        "message": "Task deleted"
    }