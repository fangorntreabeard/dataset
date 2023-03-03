import os
import sys

import asyncpg as apg


sys.path.append(os.path.abspath("../../base"))
sys.path.append(os.path.abspath("../"))
sys.path.append(os.path.abspath("../../files"))

sys.path.append(os.path.abspath("../"))
sys.path.append(os.path.abspath("../../../db_config.py"))


from functions import aio_to_list, threading_writing
from schemas import File
from JSON import JSONSettings
from app.storage.database_schema import Responses, DataBase
from config import log_path


class MyDBProject(DataBase):
    def __init__(self, connection_string):
        super().__init__(connection_string)

    async def insert_into_input_file(self, values: list):

        q = """insert into input_file(name, data) values($1, $2);"""
        conn = await apg.connect(self.connection_string)
        for value in values:
            name = value[0].split('/')
            data = value[1]
            await conn.execute(q, name[len(name) - 1], data)
        await conn.close()

    async def insert_into_output_file(self, rows):

        q = """insert into output_file(input_file_id, name, data) values($1, $2, $3);"""
        conn = await apg.connect(self.connection_string)
        identificator = rows[0]
        name = rows[1]
        data = rows[2]
        await conn.execute(q, identificator, name, data)
        await conn.close()

    async def select_distinct(self, tablename: str, condition: str, val):
        conn = await apg.connect(self.connection_string)
        result = await conn.fetch(
            f"""
            select distinct * from {tablename} where {condition} = $1
            """,
            val)
        await conn.close()
        return list(map(dict, result))[0]

    async def find_in_database(self):
        settings = await JSONSettings().get_settings()
        new_data = []
        for item in settings:
            try:
                new_data.append([await self.select_distinct('input_file', 'name', item['filename']), item['city']])
            except:
                pass
        threading_writing(log_path, f"Current data: {new_data}")
        return new_data

    async def find_files(self, filepath='../files'):
        await self.insert_into_input_file(
            await JSONSettings.files_to_rows((await aio_to_list(File(filepath=filepath).get_files()))[0]))

    async def select_file(self, tablename: str, *columns) -> object:

        q = "select "
        for column in columns:
            q += column
        q += f" from {tablename};"
        data = await Responses(self.connection_string, q).select()
        return data
