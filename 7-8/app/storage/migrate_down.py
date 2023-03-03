import asyncio as aio
import pathlib as pl

from database_schema import Responses
from config import CONFIG


async def migrate_down(connection_str: str, path: str, file_name) -> None:
    """
    :param connection_str:
    :param path:
    :param file_name:
    :return:
    """
    try:
        with open(pl.Path(path + file_name), 'r', encoding='utf-8') as response:
            await Responses(connection_str, str(response.read())).execute()
            print("LOG: migration down: Pass")
    except:
        print("LOG: migration down: Error")


if __name__ == "__main__":
    aio.run(migrate_down(*CONFIG, '../responses/migrate-down.sql'))
