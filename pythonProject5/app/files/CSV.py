import pathlib as pl
from basic.schemas import File, Table


class CSVTable(Table, File):
    def __init__(self, filename=None, filetype=None, filepath='', head=None, body=None):
        super().__init__(head, body, )
        File.__init__(self, filename, filepath, filetype)
        if self.filetype is None:
            self.filetype = 'csv'

    @property
    async def table_data(self) -> None:
        with open(pl.Path(self.filepath).joinpath(self.filename), 'r', encoding="utf-8") as csv:
            yield await CSVTable.analyze(csv.readlines())

    @staticmethod
    async def analyze(data):
        return [i.split(',') for i in data]

    def __str__(self):
        return f"<{self.head} {self.body} {self.filename} {self.filepath}>"
