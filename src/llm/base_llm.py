from abc import abstractmethod
from aiohttp import ClientSession


class BaseLLM:
    def __init__(self):
        self._aiohttp_session = ClientSession

    @property
    def aiohttp_session(self):
        return self._async_session

    @abstractmethod
    async def ask(self):
        """
        Abstract method to ask llm model about something
        :return:
        """
        raise NotImplementedError

    async def ask_with_api(self):
        """
        Method to ask llm model about something using API
        :return:
        """
        async with self.aiohttp_session as aiohttp_session:
            async with aiohttp_session.get(self.api_url) as response:
                pass
    