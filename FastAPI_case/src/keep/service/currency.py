from http.client import HTTPResponse
from typing import List

from fastapi import APIRouter
from models.models import Currency


class CurrencyRouter(object):
    router = APIRouter(
        prefix="/currency"
    )

    @staticmethod
    @router.get('/{provider}/')
    async def get_currency(provider):
        return provider
    #
    # @staticmethod
    # @router.post('/')
    # async def get_currency():
    #     return {'Pidoras'}
    #
    # @staticmethod
    # @router.delete('/{provider}')
    # async def get_currency():
    #     return 'Pidoras'
    #
    # @staticmethod
    # @router.put('/')
    # async def get_currency():
    #     return 'Pidoras'

