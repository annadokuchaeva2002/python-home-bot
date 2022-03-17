from main import dp
from aiogram import types
from utils.keyboard import keyboard
from aiogram.dispatcher.filters.builtin import CommandStart


@dp.message_handler(CommandStart())
async def bot_start(msg: types.Message):
    await msg.answer(text="Привет, я бот для напоминания домашки, посмотреть мои функции можно тут /help",
                     reply_markup=keyboard)
