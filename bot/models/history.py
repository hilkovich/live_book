from sqlalchemy import Column, Integer, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship, declarative_base

from models.users import User
from database.connection import Engine

Base = declarative_base()


class History(Base):
    __tablename__ = "history"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.telegram_id))
    user = relationship(User)
    num_book = Column(Integer)
    created_on = Column(DateTime)
    photo_captions = Column(String)
    photo_description = Column(String)
    history = Column(String)
    save = Column(Integer)

    def __str__(self):
        return f"{self.history}"

    def __repr__(self):
        return f"{self.history}"


Base.metadata.create_all(bind=Engine)
