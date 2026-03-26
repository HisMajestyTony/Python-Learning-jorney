from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DB_URL = "sqlite:///./practice.db"

db_engine = create_engine(DB_URL, connect_args={"check_same_thread": False})

DBSession = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

DBBase = declarative_base()

def get_db():
    db = DBSession()
    try:
        yield  db
    finally:
        db.close()