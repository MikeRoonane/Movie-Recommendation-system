from sqlalchemy import Column, Integer, String,BigInteger
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Movie(Base):
    __tablename__ = 'movies'
    
    movieId = Column(Integer, primary_key=True)
    title = Column(String)
    genres = Column(String)
    
class Rating(Base):
    __tablename__ = 'ratings'
    
    index = Column(Integer, primary_key=True, autoincrement=True)
    userId = Column(Integer,index=True)
    movieId = Column(Integer,index=True)
    rating = Column(Integer)
    timestamp = Column(BigInteger)