from fastapi import FastAPI
from db_routers.db_users import router

app = FastAPI()
app.include_router(router)
