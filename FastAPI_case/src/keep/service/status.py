from fastapi import APIRouter


class StatusRouter(object):
    router = APIRouter(
        prefix="/status"
    )

    @staticmethod
    @router.get('/')
    async def get_status():
        pass