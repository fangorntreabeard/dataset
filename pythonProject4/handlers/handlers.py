from aiogram import types


async def send_is_find(message: types.Message):
    pass


async def send_if_err(message: types.Message):
    pass


async def find_video(message: types.Message):
    pass


async def get_video(query: types.CallbackQuery):
    pass


async def get_audio(query: types.CallbackQuery):
    pass


async def download_audio(query: types.CallbackQuery):
    pass


async def download_video(query: types.CallbackQuery):
    pass


def err_decorator(func, func_if_err, error_type: str = ''):
    def _(arg):
        try:
            return func(arg)
        except eval(error_type):
            return func_if_err(arg)
    return _