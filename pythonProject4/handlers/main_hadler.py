import asyncio

from aiogram import types, Dispatcher, Bot
import logging

from handlers

API_TOKEN = '5377436768:AAHS8GHrfdBZIpv-7ab34qActlrVFV02yXk'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher()



@dp.message()
async def message_handler(message: types.Message):
    text = message.text.split()
    commands = {
        '/send_video': send_is_find,
    }
    command = text[0]
    if command in commands.keys():
        await commands[command](message)
    else:
        await message.answer('Действие может быть добавлено.')


@dp.callback_query()
async def query_handler(query: types.callback_query):
    text = query.data.split
    commands = {
        '/': min,
    }
    command = text[0]
    if command in commands.keys():
        await commands[command](query)
    else:
        await query.answer('Действие может быть добавлено.')


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())