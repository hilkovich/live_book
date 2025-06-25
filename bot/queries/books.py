from datetime import datetime

from database.connection import SessionLocal
from models.books import Book


def get_num_book(telegram_id):
    with SessionLocal() as session:
        return (
            session.query(Book)
            .filter_by(user_id=telegram_id)
            .order_by(Book.num_book.desc())
            .first()
        )


def add_new_book(telegram_id, name_book):
    if get_num_book(telegram_id) is None:
        num_book = 0
    else:
        num_book = get_num_book(telegram_id).num_book

    with SessionLocal() as session:
        new_book = Book(
            user_id=telegram_id,
            created_on=datetime.now(),
            num_book=num_book + 1,
            name_book=name_book,
        )
        session.add(new_book)
        session.commit()


def get_all_book(telegram_id):
    with SessionLocal() as session:
        all_books = (
            session.query(Book)
            .filter_by(user_id=telegram_id)
            .order_by(Book.num_book.asc())
            .all()
        )
        books = ""
        for book in all_books:
            books += f"{book}\n"
        return books


def get_name_book(telegram_id, num_book):
    with SessionLocal() as session:
        return (
            session.query(Book)
            .filter_by(user_id=telegram_id, num_book=num_book)
            .first()
        )


def create_file_book(telegram_id, num_book, history):
    with open(f"{telegram_id}_{num_book}.docx", "w", encoding="utf-8") as file:
        lines = [
            f"Глава №{i + 1}\n\n{chapter}\n\n" for i, chapter in enumerate(history)
        ]
        file.writelines(lines)
