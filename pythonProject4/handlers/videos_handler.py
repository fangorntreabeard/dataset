from aiogram.types import URLInputFile

import pytube as pt
import aiogram as ag

from config import bot


async def send_is_find(message: ag.types.Message):
    await err_decorator(find_video, send_if_err)(message)


async def send_if_err(message: ag.types.Message):
    await message.answer('Произошла ошибка! Проверьте веденные данные!')


async def find_video(message: ag.types.Message):
    link = message.text.split()
    youtube_video = pt.YouTube(link[1])
    if youtube_video.length > 200:
        await message.answer('Видео слишком длинное. Данный бот предназначен для создания мемов!')
    else:
        buttons = [[ag.types.InlineKeyboardButton(text="Audio", callback_data=f"/audio_info {link[1]}")],
                   [ag.types.InlineKeyboardButton(text="Video", callback_data=f"/video_info {link[1]}")]
                   ]
        print(buttons)
        await message.answer(f"Видео найдено!\n{youtube_video.title}\n{youtube_video.author}",
                             reply_markup=ag.types.InlineKeyboardMarkup(inline_keyboard=buttons))


async def get_video_resolution(q: ag.types.CallbackQuery):
    link = q.data.split()
    youtube_video = pt.YouTube(link[1])
    video_streams = youtube_video.streams.filter(file_extension='mp4', only_video=True)
    buttons = []
    for stream in video_streams[-3:]:
        buttons.append([ag.types.InlineKeyboardButton(text=f"{stream.resolution}",
                                                      callback_data=f"/download_video {link[1]} {stream.itag}")])
    print(buttons)
    await q.message.edit_reply_markup(reply_markup=ag.types.InlineKeyboardMarkup(inline_keyboard=buttons))


async def get_audio_resolution(q: ag.types.CallbackQuery):
    link = q.data.split()
    youtube_video = pt.YouTube(link[1])
    audio_streams = youtube_video.streams.filter(file_extension='mp4', only_audio=True)
    buttons = []
    for stream in enumerate(audio_streams):
        buttons.append([ag.types.InlineKeyboardButton(text=f"{stream[0]}",
                                                      callback_data=f"/download_audio {link[1]} {stream[1].itag}")])
    await q.message.edit_reply_markup(reply_markup=ag.types.InlineKeyboardMarkup(inline_keyboard=buttons))


async def download_video(q: ag.types.CallbackQuery):
    link = q.data.split()
    youtube_video = pt.YouTube(link[1])
    streams = youtube_video.streams.filter(file_extension='mp4', only_video=True)
    size = streams.get_by_itag(int(link[2])).filesize
    file = ''
    for stream in streams:
        if stream.itag == int(link[2]):
            file = stream.url
            break
    print(file, size)
    document = URLInputFile(
        file,
        filename="video.mp4",
        chunk_size=size,
        timeout=100
    )

    await bot.send_document(q.message.chat.id, document=document)


async def download_audio(q: ag.types.CallbackQuery):
    link = q.data.split()
    youtube_video = pt.YouTube(link[1])
    streams = youtube_video.streams.filter(only_audio=True)
    size = streams.get_by_itag(int(link[2])).filesize
    file = ''
    for stream in streams:
        if stream.itag == int(link[2]):
            file = stream.url
            break

    print(file, size)
    document = URLInputFile(
        file,
        filename="audio.mp3",
        chunk_size=size,
        timeout=100
    )

    await bot.send_document(q.message.chat.id, document=document)


def err_decorator(func, func_if_err):
    def _(arg):
        try:
            return func(arg)
        except:
            return func_if_err(arg)
    return _
