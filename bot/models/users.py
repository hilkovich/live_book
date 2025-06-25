from models.base import Base
from sqlalchemy import BigInteger, Column, DateTime, Integer


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    telegram_id = Column(BigInteger, unique=True)
    created_on = Column(DateTime)
