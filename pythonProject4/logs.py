import logging
import time

from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware

HANDLED_STR = ['Unhandled', 'Handled']


class MyLogging(BaseMiddleware):
    def __init__(self, logger=__name__):
        if not isinstance(logger, logging.Logger):
            logger = logging.getLogger(logger)

        self.logger = logger

        super(MyLogging, self).__init__()

    def check_timeout(self, obj):
        start = obj.conf.get('_start', None)
        if start:
            del obj.conf['_start']
            return round((time.time() - start) * 1000)
        return -1

    async def on_pre_process_update(self, update: types.Update, data: dict):
        update.conf['_start'] = time.time()
        self.logger.debug(f"Received update '{update.message}' [ID:{update.update_id}]")

    async def on_pre_process_message(self, message: types.Message, data: dict):
        self.logger.info(f"Received message '{message.text}' [ID:{message.message_id}] in chat [{message.chat.type}:{message.chat.id}]")

    async def on_pre_process_callback_query(self, callback_query: types.CallbackQuery, data: dict):
        if callback_query.message:
            message = callback_query.message
            text = (f"Received callback query [ID:{callback_query.id}] "
                    f"from user [ID:{callback_query.from_user.id}] "
                    f"for message [ID:{message.message_id}] "
                    f"in chat [{message.chat.type}:{message.chat.id}] "
                    f"with data: {callback_query.data}")

            if message.from_user:
                text = f"{text} originally posted by user [ID:{message.from_user.id}]"

            self.logger.info(text)

        else:
            self.logger.info(f"Received callback query [ID:{callback_query.id}] "
                             f"from user [ID:{callback_query.from_user.id}] "
                             f"for inline message [ID:{callback_query.inline_message_id}] ")