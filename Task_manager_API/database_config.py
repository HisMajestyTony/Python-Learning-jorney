from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DBS_URL = "sqlite:///./task_manager.db"

dbs_engine = create_engine(DBS_URL, connect_args={"check_same_thread": False})

DBS_tm_SessionMaker = sessionmaker(autocommit=False, autoflush=False, bind=dbs_engine)

DBS_tm = declarative_base()


def get_dbs():
    dbs = DBS_tm_SessionMaker()

    try:
        yield dbs
    finally:
        dbs.close()