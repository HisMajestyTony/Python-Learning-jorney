from sqlalchemy import Integer, String, Column
from db_config import DBBase

class BookTable(DBBase):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, unique=True)
    pages = Column(Integer, nullable=False)