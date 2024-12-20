FROM python:3.12-slim AS builder

WORKDIR /witly
ENV PYTHONPATH=/witly

COPY . .
RUN --mount=type=cache,target=/root/.cache pip install -r requirements.txt --upgrade --no-compile

FROM builder as api
ENTRYPOINT [ "/bin/sh", "-c", "python scripts/run_api.py"]

FROM builder as tg-bot
ENTRYPOINT [ "/bin/sh", "-c", "python scripts/run_tg_bot.py"]
