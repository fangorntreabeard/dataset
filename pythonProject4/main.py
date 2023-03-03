import asyncio
from aiogram import types

from cmd import getItem
from config import dp, bot
from handlers.videos_handler import send_is_find, get_video_resolution, download_video, get_audio_resolution, \
    download_audio

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


# @dp.message()
# async def message_command_handler(message: types.Message):
#     text = message.text.split()
#     reply = message.answer('Действие может быть добавлено!')
#     commands = {
#         '/start': 'message.answer(message.text, reply_markup=keyword_Inline)',
#         '/send': f'bot.send_message(message.chat.id, text= "{getItem(text, 0)}, https://rr1---sn-ov8vuxaxjvh-v8cs.googlevideo.com/videoplayback?expire=1668113174&ei=tg5tY4j8GLKVv_IPxtC_yA4&ip=178.49.149.7&id=o-AAtuPgtaCtKrJVl7IVwDn4xBZPB5jlB-LlwnCRp2pakd&itag=394&source=youtube&requiressl=yes&mh=ZC&mm=31%2C29&mn=sn-ov8vuxaxjvh-v8cs%2Csn-axq7sn7e&ms=au%2Crdu&mv=m&mvi=1&pl=19&initcwndbps=2048750&vprv=1&mime=video%2Fmp4&gir=yes&clen=395453&dur=71.249&lmt=1639149086707186&mt=1668091274&fvip=2&keepalive=yes&fexp=24001373%2C24007246&c=ANDROID&txp=5532434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRAIgRG8VG-VGqCGByhMKY2PNlDYjd3xTeus-nW5peHQB6RsCIGb-puRcXD1iKeDBgcpYN4ewJHwvhTPTgW7kdE0PyJeK&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhANZ_dR65GKc6ks_ibk5HNeezhfUYO6AJq-e6SqfF6jkQAiEAklEb4xGoAiCKGjiK_D0trM_rTtMzvkm5iD5hv4Rktp4%3D")',
#         '/send_video': 'bot.send_video(chat_id=message.chat.id, ))',
#         '/send_foto': 'bot.send_photo(chat_id=message.chat.id, photo="https://i.ytimg.com/vi/YbJOTdZBX1g/sddefault.jpg?v=5c072972")',
#     }
#
#     if text[0] in commands.keys():
#         reply = eval(commands[text[0]])
#
#     await reply

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


# @dp.callback_query()
# async def callback_query_command_handler(query: types.callback_query):
#     commands = {
#         '/1':  [query.answer(query.data)],
#         '/2': [query.message.answer(query.data), query.message.answer(query.data)],
#         "/3": [query.message.edit_text(text='Отредактировано!', reply_markup=keyword_Inline2)]
#     }

#     if query.data in commands.keys():
#         for command in commands[query.data]:
#             await command
#     else:
#         await query.answer('Действие может быть добавлено!')


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())