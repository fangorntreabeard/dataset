from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import cmd as c
import pyjokes


inline_btn_1 = InlineKeyboardButton('Первая кнопка!', callback_data='/send')
inline_btn_2 = InlineKeyboardButton('Вторая кнопка!', callback_data='/rule')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1).add(inline_btn_2)


async def handler(message: types.Message):
    await message.reply("Это сообщение", reply_markup=inline_kb1)


async def callback_query_handler(message: types.Message):
    await message.edit_text(text='kkk', reply_markup=inline_kb1)


async def edit_msg(message: types.Message):
    await message.edit_text("Так", reply_markup=inline_kb1)


async def send_joke(message: types.Message):
    await c.bot.send_message(chat_id=message.chat.id, text=f"{pyjokes.get_joke(language='en', category='all')}")


async def noneHandler(message: types.Message):
    await c.bot.send_message(chat_id=message.chat.id, text="Данное действие может быть добавлено.")


dct = {"key": "value"}
