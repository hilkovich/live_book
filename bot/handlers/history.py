import os

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from dotenv import load_dotenv
from keyboards.history import (
    kb_create_history,
    kb_repeat_history,
    kb_save_repeat_history,
)
from queries.history import add_new_history
from queries.prediction import (
    instructions_history,
    prediction_captions,
    prediction_history,
)
from utils.states import ProcessImageStates

load_dotenv()

username = os.getenv("RABBIT_USER")
password = os.getenv("RABBIT_PASSWORD")
host = os.getenv("RABBIT_HOST")

router = Router()


@router.callback_query(F.data == "new_history")
async def cmn_new_history(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(
        "➤ Сперва загрузите от 2 до 5 детских фотографий в хронологическом порядке в рамках одного дня"
    )
    await callback.message.answer(
        "➤ Затем опишите события, которые на них происходят.\n"
        "Пример: Семейная прогулка по парку возле дома с пикником с бабушкой и детьми Полиной 2 года и Максимом 7 лет."
    )
    await state.update_data(photo_file_id=[])
    await state.set_state(ProcessImageStates.addImage)


@router.message(ProcessImageStates.addImage)
async def cmn_get_user_photo(message: Message, state: FSMContext):
    if message.content_type == "photo":
        data = await state.get_data()
        if len(data["photo_file_id"]) < 5:
            data["photo_file_id"].append(message.photo[-1].file_id)
        else:
            await message.answer(
                "Вы загрузили максимальное количество фотографий\n"
                "Для истории будет использованы первые 5 фотографий\n"
                "Сейчас необходимо описать события, которые происходят на фотографиях"
            )
        await state.set_state(ProcessImageStates.addText)
    else:
        await message.answer("Сейчас необходимо загрузить фотографии")
        await state.set_state(ProcessImageStates.addImage)


@router.message(ProcessImageStates.addText)
async def cmn_get_user_text(message: Message, state: FSMContext):
    if message.content_type != "photo":
        await state.update_data(photo_description=message.text)
        await message.answer(
            "Давайте создадим новую историю 🤩\n\n"
            "Создание займет не более 20 секунд",
            reply_markup=kb_create_history(),
        )
    else:
        await message.answer(
            "Сейчас необходимо описать события, которые происходят на фотографиях"
        )
        await state.set_state(ProcessImageStates.addText)


@router.callback_query(F.data == "create_history")
async def cmn_create_history(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Тружусь над историей, скоро будет готово...")
    data = await state.get_data()

    photo_captions = prediction_captions(data["photo_file_id"])
    msg = instructions_history(photo_captions, data["photo_description"])
    history = prediction_history(msg).replace("\n\n", "\n")
    await state.update_data(history=history)
    await state.update_data(photo_captions=photo_captions)
    await callback.message.answer(f"{history}", reply_markup=kb_save_repeat_history())


@router.callback_query(F.data == "repeat_history")
async def cmn_repeat_history(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    add_new_history(
        callback.from_user.id,
        data["photo_captions"],
        data["photo_description"],
        data["history"],
        None,
        0,
    )
    await callback.message.answer(
        "Жаль, что вам не понравилась история 🥺\nСделаем новую?",
        reply_markup=kb_repeat_history(),
    )
