from aiogram import types

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
buttons = ["Все задания 🤩", "Добавить 📝"]
button = "Скрыть клавиутуру 😤"
keyboard.add(*buttons)
keyboard.add(button)