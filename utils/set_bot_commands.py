from aiogram import types


async def commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("help", "Помощь"),
            types.BotCommand("start", "Запуск бота"),
        ]
    )
