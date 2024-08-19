from pydantic_settings import BaseSettings, SettingsConfigDict

from src.constants import env_path


class TgConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=env_path,
        env_file_encoding='utf-8',
        env_prefix='tg_',
        extra='ignore'
    )

    bot_token: str
