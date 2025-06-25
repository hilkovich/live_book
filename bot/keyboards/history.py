from aiogram import types


def kb_help():
    buttons = [
        [
            types.InlineKeyboardButton(
                text="Как пользоваться ботиком", callback_data="help_use"
            ),
        ]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)


def kb_new_history():
    buttons = [
        [
            types.InlineKeyboardButton(
                text="Создать новую историю", callback_data="new_history"
            ),
        ]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)


def kb_create_history():
    buttons = [
        [
            types.InlineKeyboardButton(
                text="Создать историю", callback_data="create_history"
            ),
        ]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)


def kb_save_repeat_history():
    buttons = [
        [
            types.InlineKeyboardButton(text="Сохранить", callback_data="save_history"),
            types.InlineKeyboardButton(
                text="Повторить историю", callback_data="repeat_history"
            ),
        ]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)


def kb_repeat_history():
    buttons = [
        [
            types.InlineKeyboardButton(
                text="Повторить историю", callback_data="create_history"
            ),
            types.InlineKeyboardButton(
                text="Изменить фотографии", callback_data="new_history"
            ),
        ]
    ]
    return types.InlineKeyboardMarkup(inline_keyboard=buttons)
