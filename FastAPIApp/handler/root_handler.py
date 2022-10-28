from typing import Optional

from fastapi import Request, APIRouter, Cookie
from starlette.responses import RedirectResponse, JSONResponse
from config import templates
from fastapi import Response
router = APIRouter()


@router.get('/set', response_class= RedirectResponse, status_code=302)
async def sel_log_on(response: Response):
        response.set_cookie(key="is_login", value='False')
        return "/home"

@router.get('/read')
async def reading(refresh_token: Optional[str] = Cookie(None)):
    return refresh_token

@router.get('/')
async def redirect(request: Request):
    return RedirectResponse("/home", )


@router.get('/home')
async def run_handler(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})