from pytube import YouTube
from cmd import validate


class YTVideoLink(str):
    pass

    def __Name(self: str) -> str:
        return YouTube(self).title

    def __Description(self: str) -> str:
        return YouTube(self).description

    def __Photo(self: str) -> str:
        return YouTube(self).thumbnail_url

    def __Download(self: str):
        vid = YouTube(self).streams.get_highest_resolution().download()
        return vid.split()

    Description = validate(__Description)
    Photo = validate(__Photo)
    Download = validate(__Download)
    Name = validate(__Name)


print(YTVideoLink.Photo('https://www.youtube.com/watch?v=2lAe1cqCOXo&feature=emb_imp_woyt'))
