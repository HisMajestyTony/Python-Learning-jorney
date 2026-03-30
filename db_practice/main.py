from fastapi import FastAPI
from db_routers.db_users import router
from db_config import DBBase, db_engine

# import models so SQLAlchemy knows they exist
from db_models.user_table import UserTable
from db_models.book_table import BookTable

app = FastAPI()

DBBase.metadata.create_all(bind=db_engine)

app.include_router(router)