from main import dp
from aiogram import types

from aiogram.dispatcher.filters.builtin import Command


@dp.message_handler(Command('пока'))
async def bot_start(msg: types.Message):
    await msg.answer(text="Пока-пока!")