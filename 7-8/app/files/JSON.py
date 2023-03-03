import json
import pathlib as pl

from app.base.functions import aio_to_list, open_bytes, threading_writing
from app.base.schemas import File, Table
from app.config import log_path as lp


class JSON(File):
    def __init__(self, filename: object = None, filepath: object = None, filetype: object = None):
        """
        :rtype: object
        """
        File.__init__(self, filename, filepath, filetype)
        if self.filetype is None:
            self.filetype = 'json'

    async def get(self):
        with open(self.filepath, 'r', encoding='utf-8') as settings:
            yield json.loads(settings.read())


class JSONTable(Table, JSON):
    def __init__(self, filename=None, filetype="json", filepath='', head=None, body=None):
        File.__init__(self, filename, filepath, filetype)
        Table.__init__(self, head, body)

    @property
    async def table_data(self):
        with open(pl.Path(self.filepath).joinpath(self.filename), 'r') as js:
            yield await self.analyze(js.read())

    @staticmethod
    async def analyze(data):
        return [tuple(i.values())[1:] for i in json.loads(data)['Table']]

    def __str__(self):
        return f"<JSONTable {self}{self.head} {self.body} {self.filename} {self.filepath}>"


class JSONSettings(JSON):
    def __init__(self, filename: object = None, filepath: object = None, filetype: object = None):
        """
        :rtype: object
        """
        File.__init__(self, filename, filepath, filetype)
        if self.filetype is None:
            self.filetype = 'json'

    @staticmethod
    async def files_to_rows(filelist):
        result_list = []
        for filenames in filelist:
            for filename in filenames:
                result_list.append((filename, (await aio_to_list(open_bytes(filename)))[0]))
        return result_list

    async def get_settings(self):
        if self.filepath is None:
            self.filepath = '../settings/input_files'
        file_list = (await aio_to_list(JSON(filepath=self.filepath, filetype='json').find_in_directory()))[0]
        threading_writing(lp, f"Get file settings: {file_list}")
        if not len(list(file_list)[0]):
            print("Finding settings: No files founded! Next iteration...")
        tasks = []
        for file in file_list:
            tasks.append((await aio_to_list(JSON(filepath=file, filetype='').get()))[0])
        threading_writing(lp, f"Get {len(tasks)} setting(-s). Current settings: {tasks}")
        return tasks
