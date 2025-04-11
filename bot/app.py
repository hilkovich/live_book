import os
import asyncio
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher

from utils.commands import set_commands
from handlers import books, commands, history, help

load_dotenv()

bot = Bot(token=os.getenv("TG_BOT_TOKEN"))
dp = Dispatcher()


async def start():
    await set_commands(bot)
    try:
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await bot.session.close()


dp.include_router(commands.router)
dp.include_router(help.router)
dp.include_router(books.router)
dp.include_router(history.router)


if __name__ == "__main__":
    asyncio.run(start())
