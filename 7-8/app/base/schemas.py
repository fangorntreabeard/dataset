import os
import sys
from glob import glob


sys.path.append(os.path.abspath("../base"))

from functions import str_to_date, error_decorator, aio_to_list, aio_concat_lists


class Table(object):
    def __init__(self, head, body):
        self.head: list[str] = head
        self.body: list[str] = body

    async def rows(self, name_of_city=None):
        table = (await aio_to_list(self.table_data))[0]
        print('LOG: get table:', table)
        yield await self.sort_rows(table, name_of_city)

    @staticmethod
    async def sort_rows(table, name_of_city):
        return sorted(list(filter(lambda x: x[0] == name_of_city, table)),
                      key=lambda x: error_decorator(str_to_date, "str_to_date")(x[1]))

    @property
    async def table_data(self):
        return []

    @staticmethod
    async def analyze(data):
        return


class File(object):
    def __init__(self, filename=None, filepath=None, filetype=None):
        self.filename: str = filename
        self.filepath: str = filepath
        self.filetype = filetype

    async def find_in_directory(self):
        yield glob(f'{self.filepath}/*.{self.filetype}')

    async def get_files(self):
        files = await aio_concat_lists(File(filepath=self.filepath, filetype="xlsx", filename='').find_in_directory(),
                               File(filepath=self.filepath, filetype="json", filename='').find_in_directory(),
                               File(filepath=self.filepath, filetype="csv", filename='').find_in_directory())

        yield files

    @property
    async def read_file(self):
        with open(self.filepath, 'r') as f:
            yield f

    async def create_file(self):
        pass

    async def load_file_(self):
        pass

    async def create_load(self):
        pass
