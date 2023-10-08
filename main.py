import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, Document
from aiogram.utils.markdown import hbold

TOKEN = getenv('6321096156:AAGg2IoFSMNmaMwbE4V5-GkxgSbR063Oh0s')
BASE_URL = 'http://127.0.0.1:8081/bot'
bot = Bot(token='6321096156:AAGg2IoFSMNmaMwbE4V5-GkxgSbR063Oh0s')
dp = Dispatcher(base_url=BASE_URL, token=TOKEN)


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")
    sent_message = await bot.send_document(chat_id=message.chat.id, document='https://t.me/downloadsgame/3471')
    file_id = sent_message.document.file_id
    await bot.get_file(file_id)


@dp.message()
async def echo_handler(message: Document) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")


async def main() -> None:
    bot = Bot(token='6321096156:AAGg2IoFSMNmaMwbE4V5-GkxgSbR063Oh0s', parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)
    # await bot.log_out()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
