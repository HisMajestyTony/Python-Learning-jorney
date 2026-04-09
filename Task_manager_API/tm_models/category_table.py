from sqlalchemy import Integer, Column, String
from sqlalchemy.orm import relationship
from database_config import DBS_tm

class CategoryTable(DBS_tm):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    tasks = relationship("TaskTable", back_populates="category")



