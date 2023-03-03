from typing import List
from fastapi import APIRouter
from models.models import Provider


class ProviderRouter(object):
    router = APIRouter(
        prefix="/provider"
    )

    @staticmethod
    @router.get('/', response_model=List[Provider])
    async def router():
        pass