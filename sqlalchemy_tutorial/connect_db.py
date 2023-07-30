import os

from sqlalchemy import create_engine, MetaData, Column, String, Integer, Float
from sqlalchemy.orm import declarative_base

DB_URL = os.getenv('DB_URL')

engine = create_engine(DB_URL)
connection = engine.connect()
metadata = MetaData()

Base = declarative_base()


class Product(Base):
    __tablename__ = 'product'

    index = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    description = Column(String(500))
