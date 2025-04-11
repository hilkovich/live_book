from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="start", description="Запустить ботика"),
        BotCommand(command="help", description="Как пользоваться ботиком"),
        BotCommand(command="new", description="Создать новую историю"),
        BotCommand(command="books", description="Показать все книги"),
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
