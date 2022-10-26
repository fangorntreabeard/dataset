from asyncio import run as r
from typing import Union
from tracemalloc import BaseFilter
from aiogram.utils.callback_data import CallbackData

from handler_interface import *
from aiogram import executor, types
from pprint import pprint as prp
import cmd as c

c.dp.register_message_handler(send_message_handler.handler, commands=['start'])


class DataFilter(BaseFilter):
    data: Union[str, list]

    async def __call__(self, CallBackQuery: types.CallbackQuery) -> bool:
        if isinstance(self.data, str):
            return CallBackQuery.data == self.data
        else:
            return CallBackQuery.data in self.data


async def send_on_callback(CallBackQuery: types.CallbackQuery):
    prp(CallBackQuery)
    await CallBackQuery.message.answer(CallBackQuery.message.chat.id)


async def edit_on_call_back(CallBackQuery: types.CallbackQuery):
    prp(CallBackQuery)
    await CallBackQuery.message.edit_text(text='None')


c.dp.register_callback_query_handler(send_on_callback, DataFilter)


def main():
    executor.start_polling(c.dp)


if __name__ == '__main__':
    main()
