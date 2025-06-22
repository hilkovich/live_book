from aiogram.fsm.state import State, StatesGroup


class ProcessImageStates(StatesGroup):
    addImage = State()
    addText = State()


class ProcessBookStates(StatesGroup):
    addBook = State()
    numBook = State()
    allBook = State()
