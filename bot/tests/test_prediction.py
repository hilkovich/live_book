import pytest

from queries.prediction import prediction_history, instructions_history


def test_prediction_history():
    message = "Напиши историю про Николая на 50 слов"
    history = prediction_history(message)
    assert isinstance(history, str)


def test_instructions_history():
    photo_captions = ["Описание мальчика", "Описание девочки"]
    photo_description = "Тестовое примечание"
    message = instructions_history(photo_captions, photo_description)
    assert "Описание мальчика" in message
    assert "Описание девочки" in message
    assert "Тестовое примечание" in message


if __name__ == "__main__":
    pytest.main()
