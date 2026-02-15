from sqlalchemy import create_engine, Column, String, Float, Integer
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv
import os 

Base = declarative_base()

class ProductModel(Base):
    __tablename__ = "products"

    product_id = Column(String(100),primary_key = True)
    name = Column(String(100), nullable = False)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)
    

class UserModel(Base):
    __tablename__ = "users"

    username = Column(String(20), primary_key=True)
    password = Column(String(100), nullable=False)
    role = Column(String(10), nullable= False)


load_dotenv()

DB_URL = os.getenv("DATABASE_URL")

engine = create_engine(DB_URL,echo=False)
Session = sessionmaker(bind = engine)

def create_tables():
    Base.metadata.create_all(bind = engine)