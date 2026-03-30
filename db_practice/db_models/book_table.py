from sqlalchemy import Integer, String, Column, ForeignKey
from db_config import DBBase
from sqlalchemy.orm import relationship

class BookTable(DBBase):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    pages = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    owner = relationship("UserTable", back_populates="books")