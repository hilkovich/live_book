import re
import os
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext

from utils.states import ProcessBookStates
from keyboards.books import kb_create_save_book
from keyboards.history import kb_new_history
from queries.history import add_new_history, get_successful_save_history
from queries.books import (
    add_new_book,
    get_num_book,
    get_all_book,
    create_file_book,
    get_name_book,
)

router = Router()


@router.callback_query(F.data == "save_history")
async def cmn_save_history(callback: CallbackQuery):
    await callback.message.answer(
        "Создайте новую книгу или добавьте главу в вашу книгу",
        reply_markup=kb_create_save_book(),
    )


@router.callback_query(F.data == "create_book")
async def cmn_name_book(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Как назавем книгу?")
    await state.set_state(ProcessBookStates.addBook)


@router.message(ProcessBookStates.addBook)
async def cmn_create_book(message: Message, state: FSMContext):
    if len(message.text) < 30:
        data = await state.get_data()

        add_new_book(message.from_user.id, message.text)
        num_book = get_num_book(message.from_user.id).num_book
        add_new_history(
            message.from_user.id,
            data["photo_captions"],
            data["photo_description"],
            data["history"],
            num_book,
            1,
        )

        await state.clear()
        await message.answer(
            "Вы создали новую книгу и сохранили историю 🎉",
            reply_markup=kb_new_history(),
        )
    else:
        await message.answer("Слишком длинное название книги")
        await state.set_state(ProcessBookStates.addBook)


@router.callback_query(F.data == "save_book")
async def cmn_num_book(callback: CallbackQuery, state: FSMContext):
    num_book = get_num_book(callback.from_user.id)
    if num_book is None:
        await callback.message.answer("Созданных книг не существует")
    else:
        books = get_all_book(callback.from_user.id)
        await callback.message.answer(f"Доступные книги:\n{books}")
        await callback.message.answer("Укажите номер книги для загрузки")
        await state.set_state(ProcessBookStates.numBook)


@router.message(ProcessBookStates.numBook)
async def cmn_save_book(message: Message, state: FSMContext):
    if re.findall(r"\d+", message.text):
        last_book = get_num_book(message.from_user.id)
        if last_book.num_book < int(message.text) or int(message.text) == 0:
            await message.answer("Такой книги не существует")
            await state.set_state(ProcessBookStates.numBook)
        else:
            data = await state.get_data()

            add_new_history(
                message.from_user.id,
                data["photo_captions"],
                data["photo_description"],
                data["history"],
                int(message.text),
                1,
            )

            await state.clear()
            await message.answer("История сохранена 🎉", reply_markup=kb_new_history())
    else:
        await message.answer("Необходимо указать номер книги")
        await state.set_state(ProcessBookStates.numBook)


@router.callback_query(F.data == "download_book")
async def cmn_num_download_book(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Необходимо указать номер книги")
    await state.set_state(ProcessBookStates.allBook)


@router.message(ProcessBookStates.allBook)
async def cmn_download_book(message: Message, state: FSMContext):
    if re.findall(r"\d+", message.text):
        last_book = get_num_book(message.from_user.id)
        if last_book.num_book < int(message.text) or int(message.text) == 0:
            await message.answer("Такой книги не существует")
            await state.set_state(ProcessBookStates.allBook)
        else:
            books = get_successful_save_history(message.from_user.id, int(message.text))
            create_file_book(message.from_user.id, int(message.text), books)
            name_book = get_name_book(message.from_user.id, int(message.text)).name_book

            dir_file = f"{message.from_user.id}_{int(message.text)}.docx"
            file_book = FSInputFile(path=dir_file, filename=name_book)
            await message.answer_document(document=file_book)
            os.remove(dir_file)
    else:
        await message.answer("Необходимо указать номер книги")
        await state.set_state(ProcessBookStates.allBook)
