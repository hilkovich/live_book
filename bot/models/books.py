from sqlalchemy import Column, Integer, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship, declarative_base

from models.users import User
from database.connection import Engine

Base = declarative_base()


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.telegram_id))
    user = relationship(User)
    created_on = Column(DateTime)
    num_book = Column(Integer)
    name_book = Column(String)

    def __str__(self):
        return f"{self.num_book}. {self.name_book}"

    def __repr__(self):
        return f"{self.num_book}. {self.name_book}"


Base.metadata.create_all(bind=Engine)
