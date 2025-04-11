from aiogram import types


def kb_create_save_book():
    buttons = [
        [
            types.InlineKeyboardButton(
                text="Создать книгу", callback_data="create_book"
            ),
            types.InlineKeyboardButton(
                text="Сохранить в книгу", callback_data="save_book"
            ),
        ]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)


def kb_download_book():
    buttons = [
        [
            types.InlineKeyboardButton(
                text="Скачать книгу", callback_data="download_book"
            ),
        ]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)
