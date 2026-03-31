from fastapi import FastAPI
from database_config import DBS_tm, dbs_engine
from tm_routers.dbs_tasks_routes import router
from tm_models.task_table import TaskTable

app = FastAPI()

DBS_tm.metadata.create_all(bind=dbs_engine)

app.include_router(router)