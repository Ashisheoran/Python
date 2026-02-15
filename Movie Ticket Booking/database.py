from sqlalchemy import create_engine,text,Column,String,Integer, ForeignKey,Time
from sqlalchemy.orm import declarative_base , sessionmaker, relationship
from dotenv import load_dotenv
import os

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key = True)
    username = Column(String)


class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer,primary_key=True )
    title = Column(String(100),nullable=False)
    showtimes = relationship("Showtime",back_populates="movie")

class Showtime(Base):
    __tablename__ = "showtimes"
    id = Column(Integer,primary_key=True)
    movie_id = Column(Integer,ForeignKey('movies.id'))
    time = Column(String(20))
    movie = relationship("Movie",back_populates="showtimes")
    seats = relationship("Seat",back_populates="showtime")

class Seat(Base):
    __tablename__ = "seats"
    id = Column(Integer,primary_key=True)
    showtime_id = Column(Integer,ForeignKey("showtimes.id"))
    seat_no = Column(String(20))
    is_booked = Column(Integer,default=0)
    showtime = relationship("Showtime" , back_populates="seats")

class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer,primary_key=True)
    user_name = Column(String(30),nullable=False)
    movie_id = Column(Integer , ForeignKey("movies.id"))
    showtime_id = Column(Integer)
    seat_number = Column(String(200))

load_dotenv()
engine = create_engine(os.getenv("DATABASE_URL"))
Base.metadata.create_all(engine)

Session = sessionmaker(bind= engine)
session = Session()


