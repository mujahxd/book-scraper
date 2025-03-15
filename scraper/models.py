from sqlalchemy import Column, String, Integer
from scraper import Base

class BookModel(Base):
    __tablename__ = "books"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    price = Column(String, nullable=False)
    availability = Column(String, nullable=False)
    rating = Column(String, nullable=False)
    description = Column(String)
    upc = Column(String, unique=True, nullable=False)
    product_type = Column(String, nullable=False)
    price_excl_tax = Column(String, nullable=False)
    price_incl_tax = Column(String, nullable=False)
    tax = Column(String, nullable=False)
    number_of_reviews = Column(Integer, nullable=False)
    book_link = Column(String, nullable=False)

