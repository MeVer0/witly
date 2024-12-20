import uvicorn

from src.api.app import app
from configs import api_config

if __name__ == "__main__":
    print()
    uvicorn.run(app, host=api_config.host, port=api_config.port)