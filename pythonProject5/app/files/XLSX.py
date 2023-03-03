import pathlib as pl

import pandas as pd
from basic.schemas import File, Table


class XLSXTable(Table, File):
    def __init__(self, filename=None, filetype=None, filepath='', head=None, body=None):
        File.__init__(self, filename, filepath, filetype)
        Table.__init__(self, head, body)
        self.filetype = 'xlsx'

    @property
    async def table_data(self) -> object:
        df: object = pd.read_excel(pl.Path(self.filepath).joinpath(self.filename)).values.tolist()
        yield await self.analyze(df)

    @staticmethod
    async def analyze(data):
        toTime = lambda t: t.strftime('%d.%m.%Y') if type(t) == pd.Timestamp else t
        return [list(map(str, [i for i in map(toTime, (i for i in j))])) for j in data]

    def __str__(self):
        return f"<XLSXTable {self.head} {self.body} {self.filename} {self.filepath}>"
