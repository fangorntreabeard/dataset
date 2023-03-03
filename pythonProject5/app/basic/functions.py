import asyncio as aio
from datetime import datetime, date
from functools import wraps, partial
from multiprocessing import Process


def error_decorator(func, string='Err: What are u waiting for?', exception=''):
    def _(arg):
        try:
            return func(arg)
        except eval(exception):
            print(string)
            return _

    return _


def str_to_date(date_str: str) -> date:
    return datetime.strptime(date_str, '%d.%m.%Y').date()


def async_decorator(func):
    @wraps(func)
    async def run(*args, loop=None, executor=None, **kwargs):
        if loop is None:
            loop = aio.get_event_loop()
        partial_func = partial(func, *args, **kwargs)
        return await loop.run_in_executor(executor, partial_func)

    return run


def to_sync_generator(ait):
    loop = aio.get_event_loop()
    try:
        while True:
            try:
                coro = ait.__anext__()
                res = loop.run_until_complete(coro)
            except StopAsyncIteration:
                return
            else:
                yield res
    finally:
        coro = loop.shutdown_asyncgens()
        loop.run_until_complete(coro)


async def aio_to_list(aio_gen) -> list:
    lst = []
    async for i in aio_gen:
        lst.append(i)
    return lst


async def aio_concat_lists(*lists):
    result_list = []
    for lst in lists:
        lst = (await aio_to_list(lst))[0]
        if lst:
            result_list.append(lst)
    return result_list


def get_item(lst: list, index: int):
    return None if index > len(lst) else lst[index]


async def open_bytes(filename: str):
    with open(filename, 'rb') as file:
        yield file.read()


def threading_writing(file, data):
    data = f'\n{datetime.now()} {data}\n',
    with open(file, 'a') as f:
        Process(target=f.write, args=data, ).run()
    Process(target=print, args=data, ).start()
    return
