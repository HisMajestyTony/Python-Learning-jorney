from sqlalchemy import Integer, String,Boolean, Column
from database_config import DBS_tm

class TaskTable(DBS_tm):

    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    task_name = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=False)
    is_done = Column(Boolean, nullable=False)
    priority = Column(String, nullable=False)