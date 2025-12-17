from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from core.config import settings

engine = create_engine(
    settings.DATABASE_URL
)

SessionLocal = sessionmaker(bind=engine,autoflush=False,autocommit=False) # attaches the session to your database engine,autoflush=False means SQLAlchemy will not push pending changes to the DB before a query and autocommit=False menas every transaction must be manually committed

Base = declarative_base()

# function to access the database and close it when the session is over
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()


def create_tables():
    Base.metadata.create_all(bind=engine)
