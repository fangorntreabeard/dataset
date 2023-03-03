import logging

from aiogram import Dispatcher, Bot

API_TOKEN = '5377436768:AAHS8GHrfdBZIpv-7ab34qActlrVFV02yXk'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
