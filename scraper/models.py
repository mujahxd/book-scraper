from dataclasses import dataclass
from sqlalchemy import Column, String, Float, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

@dataclass
class Book:
    title: str
    price_excl_tax: float
    price_incl_tax: float
    tax: float
    rating: int
    availability: str
    image_url: str
    category: str
    description: str
    upc: str
    product_page_url: str
    num_reviews: int

class BookSchema(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    price_excl_tax = Column(Float, nullable=False)
    price_incl_tax = Column(Float, nullable=False)
    tax = Column(Float, nullable=False)
    rating = Column(Integer, nullable=False)
    availability = Column(String, nullable=False)
    image_url = Column(String, nullable=False)
    category = Column(String, nullable=False)
    description = Column(String, nullable=True)
    upc = Column(String, unique=True, nullable=False)
    product_page_url = Column(String, unique=True, nullable=False)
    num_reviews = Column(Integer, nullable=False)
