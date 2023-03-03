import asyncio

from aiogram import types

from config import dp, bot
from handlers.videos_handler import send_is_find, get_video_resolution, download_video, get_audio_resolution, \
    download_audio


@dp.message()
async def message_command_handler(message: types.Message):
    text = message.text.split()
    reply = message.answer('Действие может быть добавлено!')
    commands = {
        '/send_video': send_is_find,
    }

    if text[0] in commands.keys():
        await commands[text[0]](message)
    else:
        await reply


@dp.callback_query()
async def callback_query_command_handler(q: types.callback_query):
    command = q.data.split()
    print(command)
    commands = {
        '/video_info': get_video_resolution,
        '/download_video': download_video,
        '/audio_info': get_audio_resolution,
        '/download_audio': download_audio,
    }
    if command[0] in commands.keys():
        await commands[command[0]](q)
    else:
        await q.answer('Действие может быть добавлено!')


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
