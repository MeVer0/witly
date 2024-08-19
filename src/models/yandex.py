from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

import src.models as models


class YandexUser(models.Base):
    __tablename__ = "yandex_users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    tg_user_id: Mapped[int] = mapped_column(ForeignKey("tg_users.id"))
    uid: Mapped[int]
    token: Mapped[str]
