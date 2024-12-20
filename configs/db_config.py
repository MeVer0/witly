from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import computed_field


class DBConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file_encoding='utf-8',
        env_prefix='postgres_',
        extra='ignore'
    )

    host: str
    port: str
    name: str
    user: str
    password: str
    echo: bool = False
    pool_pre_ping: bool = True
    pool_size: int = 50
    max_overflow: int = 10

    @computed_field
    def async_url(self) -> str:
        return f'postgresql+asyncpg://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}'

    @computed_field
    def sync_url(self) -> str:
        return f'postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}'
