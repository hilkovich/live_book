import pytest

from queries.books import get_num_book, add_new_book, get_name_book


def test_add_new_book():
    add_new_book(123058345, "Тестовая книга №1")
    assert get_num_book(123058345) is not None


def test_get_name_book():
    assert get_name_book(123058345, 1).name_book == "Тестовая книга №1"


if __name__ == "__main__":
    pytest.main()
