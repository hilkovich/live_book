from aiogram import Router
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from keyboards.books import kb_download_book
from keyboards.history import kb_help, kb_new_history
from queries.books import get_all_book
from queries.users import add_new_user, get_user
from utils.states import ProcessImageStates

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    user = get_user(message.from_user.id)
    if user is None:
        add_new_user(message.from_user.id)
    msg = (
        "Привет 👋\n"
        "Я — ботик, умею создавать и вести книги с индивидуальной историей ребенка.\n\n"
        "Вы сможете:\n"
        "➤  создавать и сохранять книги под разные важные события и даты ребенка;\n"
        "➤  загружать фотографии ребенка, сделанные в разные периоды его жизни;\n"
        "➤  добавлять текст к фотографиям, описывая события, которые на них изображены, или чувства и эмоции, связанные с этими событиями;\n"
        "➤  с помощью искусственного интеллекта этот материал превратить в главу книги;\n"
        "➤  добавлять главу в уже созданные книги;\n"
        "➤  скачивать книги, чтобы распечатать их или поделиться;\n"
        "➤  отправлять книги в социальные сети и мессенджеры."
    )
    await message.answer(msg, reply_markup=kb_help())


@router.message(Command("new"))
async def cmn_add_new_history(message: Message, state: FSMContext):
    await message.answer(
        "➤ Сперва загрузите до 20 детских фотографий в хронологическом порядке"
    )
    await message.answer(
        "➤ Затем опишите события, которые на них происходят. Пример: Семейная прогулка по парку возле дома с пикником с бабушкой и детьми Полиной 2 года и Максимом 7 лет."
    )
    await state.update_data(photo_file_id=[])
    await state.set_state(ProcessImageStates.addImage)


@router.message(Command("books"))
async def cmn_get_all_book(message: Message):
    books = get_all_book(message.from_user.id)
    await message.answer(f"Доступные книги:\n{books}", reply_markup=kb_download_book())


@router.message(Command("help"))
async def cmn_help_use(message: Message):
    msg = (
        "Создание истории\n"
        "➤ Для создания новой истории воспользуйтесь меню или кнопкой создания истории\n"
        "➤ Сперва загрузите от 2 до 5 детских фотографий в хронологическом порядке в рамках одного дня\n"
        "➤ На этапе загрузки фотографий не указывайте описания!\n"
        "➤ После загрузки фотографий опишите события, которые на них происходят\n"
        "➤ Описание должно содержать главные моменты, которые стоит учесть при составлении истории\n\n"
        "Доп функции\n"
        "➤ Создание книг под значимые мометы и сохранение в них историй\n"
        "➤ Для повтора инструкции по использованию ботика воспользуйтесь меню\n"
        "➤ Для просмотра сохраненных книг и их скачивания воспользуйтесь меню"
    )
    await message.answer(msg, reply_markup=kb_new_history())
