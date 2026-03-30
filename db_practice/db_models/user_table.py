from sqlalchemy import Integer, String, Column
from db_config import DBBase
from sqlalchemy.orm import relationship


class UserTable(DBBase):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    age = Column(Integer, nullable=False)

    books = relationship("BookTable", back_populates="owner", cascade="all, delete-orphan")