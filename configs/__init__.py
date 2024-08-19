from .db_config import DBConfig
from .yandex_tmp_config import YandexTmpConfig
from .tg_config import TgConfig


db_config = DBConfig()
yandex_tmp_config = YandexTmpConfig()
tg_config = TgConfig()


class AllConfigs:
    def __init__(self):
        self.db_config: DBConfig = db_config
        self.tg_config: TgConfig = tg_config


all_configs = AllConfigs()
