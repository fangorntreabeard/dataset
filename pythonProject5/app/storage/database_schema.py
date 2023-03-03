import asyncpg as apg


class DataBase(object):
    __slots__ = 'connection_string'

    def __init__(self, connection_string):
        '''
        :param connection_string:
        '''
        self.connection_string: str = connection_string

    async def _connection_(self):
        print(self.connection_string)
        return await apg.connect(self.connection_string)


class Responses(DataBase):
    def __init__(self, connection_string, response_string):
        '''
        :param connection_string:
        :param response_string:
        '''
        self.response_string: str = response_string
        DataBase.__init__(self, connection_string)

    async def execute(self):
        """
        :return:
        """
        conn = await apg.connect(self.connection_string)
        await conn.execute(self.response_string)
        await conn.close()

    async def select(self):
        """
        :return:
        """
        conn = await self._connection_()
        data = await conn.fetch(self.response_string)
        await conn.close()
        return data



    def __str__(self):
        return f'<class {Responses.__name__}" {self.connection_string} {self.response_string} >'
