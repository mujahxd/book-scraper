from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from scraper import Base

DATABASE_URL = "sqlite:///data/books_data.db"


def get_engine():
    return create_engine(DATABASE_URL, echo=True)

def create_tables():
    engine = get_engine()
    Base.metadata.create_all(engine)

def get_session():
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    return Session()