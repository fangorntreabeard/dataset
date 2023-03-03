from http.client import IncompleteRead
import typing


def getItem(array, ID: int) -> str:
    try:
        return array[ID]
    except IndexError:
        return ' '


def validate(function):
    def func(link):
        try:
            my_video = function(link)
        except IncompleteRead as e:
            my_video = e.partial
        return my_video
    return func