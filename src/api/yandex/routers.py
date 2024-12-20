from fastapi import APIRouter
from starlette.requests import Request
from starlette.templating import Jinja2Templates

import src.dto as dto
from src.constants import templates_path

router = APIRouter(prefix='/yandex')
templates = Jinja2Templates(directory=templates_path)


@router.get("/authorize")
def read_root(request: Request,):
    return templates.TemplateResponse(
        request=request,
        name="yandex_aouth.html"
    )


@router.post('/d')
def save_yandex_data(data: dto.api_dto.YandexTokenData):
    print(data)

