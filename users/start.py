from main import dp
from aiogram import types

from aiogram.dispatcher.filters.builtin import CommandStart


@dp.message_handler(CommandStart())
async def bot_start(msg: types.Message):
    await msg.reply(text="Привет, я бот для напоминания домашки, посмотреть мои функции можно тут /help")
