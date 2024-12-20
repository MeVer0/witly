from pydantic_settings import BaseSettings, SettingsConfigDict


class YandexTmpConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file_encoding='utf-8',
        env_prefix='yandex_',
        extra='ignore'
    )

    token: str
    app_client_id: str
