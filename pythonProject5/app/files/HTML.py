import os
import pathlib as pl
import sys

import jinja2 as jj2

from files.CSV import CSVTable
from files.JSON import JSONTable
from files.XLSX import XLSXTable
from basic.functions import aio_to_list
from basic.schemas import Table, File


# noinspection PyTypeChecker
class HTMLTable(Table, File):
    def __init__(self, filename=None, filetype=None, filepath='', head=None, body=None, ):
        super().__init__(head, body)
        File.__init__(self, filename, filepath, filetype)
        if self.filetype is None:
            self.filetype = 'html'

    def __str__(self):
        return f"<HTMLTable {self.head} {self.body} {self.filename} {self.filepath}>"

    async def create_file(self) -> None:
        """
        :rtype: object
        """
        head = '<meta charset="utf-8"><table>'
        with open(pl.Path(self.filepath).joinpath(self.filename), 'w') as html:
            html.write(head + '{% for i in items %}<TR>{% for j in i %}<TD class="c3">"{{j}}"</TD>{% endfor %}</TR>'
                              '{% endfor %}</table>')

    async def load_data(self) -> None:
        self.body = self.body[0]
        with open(pl.Path(self.filepath).joinpath(self.filename), 'w', encoding="utf-8") as f:
            f.write(await self.render(self.body))

    @staticmethod
    async def render(arg):
        template = '<meta charset="utf-8">' \
                   '<table>{% for i in items %}' \
                   '<TR>{% for j in i %}<TD class="c3">"{{j}}"</TD>{% endfor %}</TR>' \
                   '{% endfor %}</table>'

        return jj2.Template(template).render(items=arg)

    async def create_load(self, name_of_city='', ttype=None, filename='', filepath=''):
        """
        :param name_of_city:
        :param ttype:
        :param filename:
        :return:
        """
        file = CSVTable(head='', body='', filename=filename, filepath=filepath)
        if ttype == JSONTable:
            file = JSONTable(head='', body='', filename=filename, filepath=filepath)
        if ttype == XLSXTable:
            file = XLSXTable(head='', body='', filename=filename, filepath=filepath)
        self.body = await aio_to_list(Table.rows(file, name_of_city))
        await HTMLTable.create_file(self)
        await HTMLTable.load_data(self)

    @staticmethod
    async def create_load_from_csv(name_of_city: str, filename: str, html_filename: str,
                                   path="../../files") -> None:
        try:
            html = HTMLTable(head=["Town", "Date", "Weather"], body="", filepath=pl.Path(path), filename=html_filename)
            await html.create_load(name_of_city, CSVTable, filename, filepath=pl.Path(path))
        except:
            raise Exception("Что тебе от меня надо?")

    @staticmethod
    async def create_load_from_json(name_of_city: str, filename: str, html_filename: str,
                                    path="../../../files") -> None:
        try:
            html = HTMLTable(head=["Town", "Date", "Weather"], body="", filepath=pl.Path(path),
                             filename=html_filename)
            await html.create_load(name_of_city, JSONTable, filename, filepath=pl.Path(path))
        except:
            raise Exception("Что тебе от меня надо?")

    @staticmethod
    async def create_load_from_xlsx(name_of_city: str, filename: str, html_filename: str,
                                    path="../../files/") -> None:
        # try:
        html = HTMLTable(head=["Town", "Date", "Weather"], body="", filepath=pl.Path(path),
                         filename=html_filename)
        await html.create_load(name_of_city, XLSXTable, filename, filepath=pl.Path(path))
    # except:
    #     raise Exception("Что тебе от меня надо?")

# aio.run(HTMLTable.create_load_from_csv(name_of_city='Moscow', filename="csvFile.csv", html_filename="index.html", ))
# aio.run(HTMLTable.create_load_from_xlsx(name_of_city='Москва', filename="Weather.xlsx", html_filename="index.html", ))
