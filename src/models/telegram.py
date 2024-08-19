from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

import src.models as models


class TgUser(models.Base):
    __tablename__ = 'tg_users'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(32))
    first_name: Mapped[str] = mapped_column(String(32))
    last_name: Mapped[str] = mapped_column(String(32))
    language_code: Mapped[str] = mapped_column(String(3))
    is_bot: Mapped[bool]
