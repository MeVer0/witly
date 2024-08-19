import uvicorn
from fastapi import FastAPI, Request
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from src.constants import templates_path, static_path
import src.dto as dto


app = FastAPI()

templates = Jinja2Templates(directory=templates_path)
app.mount("/static", StaticFiles(directory=static_path), name="static")


@app.get("/autorise_yandex")
def read_root(request: Request,):
    return templates.TemplateResponse(
        request=request,
        name="yandex_aouth.html"
    )


@app.post('d')
def save_yandex_data(data: dto.api_dto.YandexTokenData):
    print(data)



if __name__ == "__main__":
    print()
    uvicorn.run(app, host="127.0.0.1", port=8080)
