import logging
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram import Bot, Dispatcher, types

from logs import MyLogging

# from aiogram.contrib.fsm_storage.memory import MemoryStorage



API_TOKEN = '5377436768:AAHS8GHrfdBZIpv-7ab34qActlrVFV02yXk'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, run_tasks_by_default=True)
dp.middleware.setup(MyLogging())


