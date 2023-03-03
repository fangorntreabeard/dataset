import asyncio as aio

import magic
import pandas as pd
import sys
import os


sys.path.append(os.path.abspath("../app"))
sys.path.append(os.path.abspath("./base"))
sys.path.append(os.path.abspath("./files"))
sys.path.append(os.path.abspath("../storage"))

from base.functions import threading_writing
from files.CSV import CSVTable
from files.HTML import HTMLTable
from files.JSON import JSONTable
from files.XLSX import XLSXTable
from storage.my_database.mydatabase import MyDBProject
from config import log_path as lp


async def app():
    global log_path
    conn = MyDBProject("postgres://admin:1234@localhost:5433/postgres?sslmode=disable")
    threading_writing(lp, f"Current database: {conn.connection_string}")
    data = await conn.find_in_database()
    for row in data:
        cur_data = row[0]['data']
        tpe = magic.from_buffer(cur_data).lower()
        city = row[1]
        threading_writing(lp, f"Getting city: {city}")

        if 'csv' in tpe:
            cur_data = await HTMLTable.sort_rows(await CSVTable.analyze(cur_data.decode()), city)
        if 'excel' in tpe:
            cur_data = await HTMLTable.sort_rows(await XLSXTable.analyze(pd.read_excel(cur_data).values.tolist()), city)
        if 'json' in tpe:
            cur_data = await HTMLTable.sort_rows(await JSONTable.analyze(cur_data.decode()), city)

        html = await HTMLTable.render(cur_data)
        threading_writing(lp, f'Rendering HTML: {html}')
        html = html.encode()
        name = row[0]['name'] + ".html"
        id = row[0]['id']

        await conn.insert_into_output_file([id, name, html])


async def main():
    while True:
        await aio.gather(MyDBProject("postgres://admin:1234@localhost:5433/postgres?sslmode=disable").find_files(), app())

if __name__ == '__main__':
    try:
        aio.run(main())
    except KeyboardInterrupt:
        print('Goodbuy!\n\n...Exiting...\n')
    print(f'Log saved: {lp}.')
