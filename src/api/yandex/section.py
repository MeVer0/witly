from aiohttp import ClientSession
from yandex_music import ClientAsync
import asyncio

import src.models as models
import src.dto as dto

from src.api.base_section import BaseApiSection
from configs import yandex_tmp_config


class YandexApiSection(BaseApiSection):
    def __init__(self):
        super().__init__()
        self.base_url = 'https://api.music.yandex.net'

    def _get_user_token(self) -> str:
        #TODO: take tokens from DB, not config
        return yandex_tmp_config.token

    async def register_user_in_db(self):
        """
        Registers a user with data from yandex in the database
        using yandex-api token
        :return:
        """
        url = f'{self.base_url}/account/settings'
        user_token = self._get_user_token()
        headers = {'Authorization': f'OAuth {user_token}'}

        async with self.aiohttp_session() as session:
            async with session.get(url=url, headers=headers) as resp:
                user_settings = await resp.json()
                result = dto.api_dto.YandexUserSettings.parse_obj(
                    user_settings.get('result', {})
                )
                invocation_info = dto.api_dto.InvocationInfo.parse_obj(
                    user_settings.get('invocationInfo', {})
                )
                user_settings = dto.api_dto.YandexUserSettingsResponse(
                    invocation_info=invocation_info,
                    result=result
                )
        async with self.db_controller() as db_session:
            db_session.add(
                models.YandexUser(
                    tg_id=tg_user_id,
                    uid=user_settings.result.uid,
                    token=user_token
                )
            )
            await db_session.commit()

    async def get_user(self) -> models.YandexUser:
        """

        :return:
        """

        async with self.db_controller() as db_session:
            db_session.get_one()

    def save_yandex_token(
            self,
            access_token: str,
            token_type: str,
            expires_in: str,
            cid: str
    ):
        print(access_token, token_type, expires_in, cid)



if __name__ == '__main__':
    y = YandexApiSection()
    asyncio.run(y.register_yandex_user_in_db())