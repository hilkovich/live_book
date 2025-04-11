import pytest

from queries.history import add_new_history, get_successful_save_history


def test_add_new_history():
    telegram_id = 123058345
    photo_captions = "Тестовое описание фотографий"
    photo_description = "Тестовое примечание к фотографиям"
    history = "Тестовая история"
    num_book = 12
    add_new_history(
        telegram_id, photo_captions, photo_description, history, num_book, 1
    )
    all_history = get_successful_save_history(telegram_id, num_book)
    assert len(all_history) == 1


if __name__ == "__main__":
    pytest.main()
