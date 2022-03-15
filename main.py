from aiogram import Bot, Dispatcher, types
from environs import Env
from datetime import datetime


env = Env()
env.read_env()

TOKEN = env.str("TOKEN")
ADMIN = env.str("ID")

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)
"""
messageEntityBold => <b>bold</b>, <strong>bold</strong>, **bold**
messageEntityItalic => <i>italic</i>, <em>italic</em> *italic*
messageEntityCode => <code>code</code>, `code`
messageEntityStrike => <s>strike</s>, <strike>strike</strike>, <del>strike</del>, ~~strike~~
messageEntityUnderline => <u>underline</u>
messageEntityPre => <pre language="c++">code</pre>,
"""


async def on_startup(dispatcher):
    await dispatcher.bot.send_message(chat_id=ADMIN,
                                      text=f"<b>🤖 Бот запущен</b>\n"
                                           f"<b>🕔 UTC:</b> <i>{datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')}</i>")

