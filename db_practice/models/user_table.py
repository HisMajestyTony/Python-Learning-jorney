from sqlalchemy import Integer, String, Column
from db_config import DBBase

class UserTable(DBBase):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    age = Column(Integer, nullable=False)