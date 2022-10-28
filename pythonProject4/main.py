import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.utils.keyboard import InlineKeyboardBuilder

API_TOKEN = '5377436768:AAHS8GHrfdBZIpv-7ab34qActlrVFV02yXk'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


kb = [
    [types.KeyboardButton(text="С пюрешкой")],
    [types.KeyboardButton(text="Без пюрешки")]
]

buttons = [
    [
        types.InlineKeyboardButton(text="1", callback_data="/1"),
        types.InlineKeyboardButton(text="2", callback_data="/2")
    ],
    [types.InlineKeyboardButton(text="3", callback_data="/3")]
]

keyboard_Reply = types.ReplyKeyboardMarkup(keyboard=kb)
keyword_Inline = types.InlineKeyboardMarkup(inline_keyboard=buttons)


buttons1 = [
    [
        types.InlineKeyboardButton(text="1", callback_data="/1"),
        types.InlineKeyboardButton(text="2", callback_data="/2")
    ],
]

keyword_Inline2 = types.InlineKeyboardMarkup(inline_keyboard=buttons1)

@dp.message()
async def message_command_handler(message: types.Message):
    commands = {
        '/start': message.answer(message.text, reply_markup=keyword_Inline),
    }
    if message.text in commands.keys():
        await commands[message.text]
    else:
        await message.answer('Действие может быть добавлено!')


@dp.callback_query()
async def callback_query_command_handler(query: types.callback_query):
    commands = {
        '/1':  [query.answer(query.data)],
        '/2': [query.message.answer(query.data), query.message.answer(query.data)],
        "/3": [query.message.edit_text(text='Отредактировано!', reply_markup=keyword_Inline2)]
    }
    if query.data in commands.keys():
        for i in commands[query.data]:
            await i
    else:
        await query.answer('Действие может быть добавлено!')


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())