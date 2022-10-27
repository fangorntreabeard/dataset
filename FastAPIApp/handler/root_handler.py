from imports import *

router = APIRouter()


@router.get('/')
async def root(request: Request):
    return RedirectResponse("/home")


@router.get('/{handler_name}')
async def run_handler(request: Request, handler_name: str):
    paths = {
            'home': templates.TemplateResponse("index.html", {"request": request}),
            'registration': templates.TemplateResponse("registration.html", {"request": request}),
        }
    if handler_name in paths.keys():
        return paths[handler_name]
    return templates.TemplateResponse("index.html", {"request": request}, status_code=404)