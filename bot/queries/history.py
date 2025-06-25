from datetime import datetime

from database.connection import SessionLocal
from models.history import History


def add_new_history(
    telegram_id, photo_captions, photo_description, history, num_book=None, save=0
):
    with SessionLocal() as session:
        new_history = History(
            user_id=telegram_id,
            num_book=num_book,
            created_on=datetime.now(),
            photo_captions=photo_captions,
            photo_description=photo_description,
            history=history,
            save=save,
        )
        session.add(new_history)
        session.commit()


def get_successful_save_history(telegram_id, num_book):
    with SessionLocal() as session:
        all_history = (
            session.query(History)
            .filter_by(user_id=telegram_id, num_book=num_book, save=1)
            .order_by(History.created_on.asc())
            .all()
        )

        return all_history
