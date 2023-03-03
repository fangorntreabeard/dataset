from fastapi import FastAPI

from fastapi import APIRouter
from service import main_router
# from provider import ProviderRouter as Pr

# main_router.include_router(Pr.router)
# main_router.include_router(Pr.router)


app = FastAPI()


@app.get('/')
async def root():
    await main_router()
    return {'message': 'ben'}
