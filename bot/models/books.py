from models.base import Base
from models.users import User
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


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
