from sqlalchemy import create_engine, Engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import sessionmaker, Session

from configs import db_config


class DBController:
    def __init__(
            self
    ):
        self.db_config = db_config
        self.__engine = create_engine(
            url=self.db_config.sync_url,
            pool_size=self.db_config.pool_size,
            max_overflow=self.db_config.max_overflow,
            pool_pre_ping=self.db_config.pool_pre_ping,

        )
        self.__async_engine = create_async_engine(
            url=self.db_config.async_url,
            pool_size=self.db_config.pool_size,
            max_overflow=self.db_config.max_overflow,
            pool_pre_ping=self.db_config.pool_pre_ping,

        )
        self.__session_factory = sessionmaker(self.__engine)
        self.__async_session_factory = async_sessionmaker(self.__async_engine)

    @property
    def session_factory(self) -> sessionmaker[Session]:
        return self.__session_factory

    @property
    def async_session_factory(self) -> async_sessionmaker[AsyncSession]:
        return self.__async_session_factory

    @property
    def engine(self) -> Engine:
        return self.__engine

    def __enter__(self):
        with self.session_factory() as session:
            self.session = session
            return self.session

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

    async def __aenter__(self):
        async with self.async_session_factory() as async_session:
            self.async_session = async_session
            return self.async_session

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.async_session.close()
