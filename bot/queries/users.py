from datetime import datetime

from database.connection import SessionLocal
from models.users import User


def add_new_user(telegram_id):
    with SessionLocal() as session:
        new_user = User(
            telegram_id=telegram_id,
            created_on=datetime.now(),
        )
        session.add(new_user)
        session.commit()


def get_user(telegram_id):
    with SessionLocal() as session:
        return session.query(User).filter_by(telegram_id=telegram_id).first()
