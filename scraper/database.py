from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

# Database setup
DATABASE_URL = "sqlite:///data/books.db"
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def init_db():
    return Base.metadata.create_all(engine)