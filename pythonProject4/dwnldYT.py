import pytube
from pytube import YouTube


def download_Video(video_yt) -> None:
    video_streams = video_yt.streams.filter(file_extension='mp4', only_video=True)
    for streams in video_streams:
        print(
         f"Скрытая ссылка: {streams.url}\
         Тэг : {streams.itag} \
         Разрешение : {streams.resolution} \
         Кодек : {streams.codecs[0]}"
        )
    input_itag: str = input("Введите тэг : ")
    video = video_yt.streams.get_by_itag(input_itag)
    print(video_yt.streams.get_by_itag(input_itag).filesize)
    print((video.download()))
    print("Загрузка: ", video_yt.title + ".mp4")


link = "https://youtu.be/9bZkp7q19f0"
yt = pytube.YouTube(link)
print(yt.length)
download_Video(yt)

# def download_Video(video_yt) -> None:
#     video_streams = video_yt.streams.filter(only_audio=True)
#     for streams in video_streams:
#         print(
#          f"Скрытая ссылка: {streams.url}\
#          Тэг : {streams.itag} \
#          Разрешение : {streams.resolution} \
#          Кодек : {streams.codecs[0]}"
#         )
#     input_itag: str = input("Введите тэг : ")
#     video = video_yt.streams.get_by_itag(input_itag)
#     print(video.download())
#     print("Загрузка: ", video_yt.title + ".mp4")
#
# link = "https://www.youtube.com/watch?v=EHfx9LXzxpw"
# yt = pytube.YouTube(link)
# download_Video(yt)
#
#
# def func(*a):
#     b = 0
#     print(eval("b"))
#

YouTube('https://youtu.be/9bZkp7q19f0').streams.first().download()
yt = YouTube('http://youtube.com/watch?v=9bZkp7q19f0')
yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()