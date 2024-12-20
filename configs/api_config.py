from pydantic_settings import BaseSettings, SettingsConfigDict


class ApiConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file_encoding='utf-8',
        env_prefix='api_',
        extra='ignore'
    )

    host: str = '127.0.0.1'
    port: int = 8080