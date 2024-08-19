from aiohttp import ClientSession

from src.db_controller import DBController


class BaseApiSection:

    def __init__(self):
        self.aiohttp_session = ClientSession
        self.db_controller = DBController

