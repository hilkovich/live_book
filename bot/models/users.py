from sqlalchemy import Column, Integer, DateTime, BigInteger
from sqlalchemy.orm import declarative_base

from database.connection import Engine

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    telegram_id = Column(BigInteger, unique=True)
    created_on = Column(DateTime)


Base.metadata.create_all(bind=Engine)
