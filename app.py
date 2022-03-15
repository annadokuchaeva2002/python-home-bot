import users
from aiogram import executor
from main import dp, on_startup

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=False)
