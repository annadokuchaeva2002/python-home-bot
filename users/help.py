from main import dp
from aiogram import types

from aiogram.dispatcher.filters.builtin import CommandHelp


@dp.message_handler(CommandHelp())
async def bot_start(msg: types.Message):
    await msg.reply(text="<b>Мои возможности:</b>\n\nскоро наполню")