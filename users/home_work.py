from main import dp
from aiogram import types

from aiogram.dispatcher.filters.builtin import Text


@dp.message_handler(Text(equals="Все задания 🤩"))
async def vse_zadaniya(msg: types.Message):
    await msg.answer(text="<b>Ваши задания:</b>\n\nскоро наполню")


@dp.message_handler(Text(equals="Добавить 📝"))
async def dobavit(msg: types.Message):
    await msg.answer(text="прикрепите ваше задание")


@dp.message_handler(Text(equals="Скрыть клавиутуру 😤"))
async def dobavit(msg: types.Message):
    await msg.answer(text="Клавиатура скрыта\nДля вызова /start", reply_markup=types.ReplyKeyboardRemove())

