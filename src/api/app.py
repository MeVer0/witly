import uvicorn
from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from src.constants import static_path
from src.api.yandex.routers import router as yandex_router

app = FastAPI()

app.mount("/static", StaticFiles(directory=static_path), name="static")
app.include_router(router=yandex_router)
