from sqlalchemy.orm import declarative_base,sessionmaker

from sqlalchemy import create_engine
from config import settings

Base=declarative_base()
url=settings.DB_URL

engine=create_engine(url=url)

SessionFactory=sessionmaker(bind=engine,autoflush=False,autocommit=False)


def connect():
    db=SessionFactory()
    try:
        yield db 
    finally:
        db.close()