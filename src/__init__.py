import src.constants
import src.enums as enums
import src.db_controller as db_controller
import configs as configs


class GlobalContext:
    def __init__(self):
        self.constants = constants
        self.db_controller = db_controller
        self.enums = enums
        self.configs = configs
