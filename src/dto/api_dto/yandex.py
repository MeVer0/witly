import datetime

from pydantic import BaseModel, Field, AliasChoices, ConfigDict
from pydantic.alias_generators import to_camel


class YandexUser(BaseModel):
    id: int
    uid: int


class InvocationInfo(BaseModel):
    req_id: str = Field(validation_alias=AliasChoices('req-id'))
    hostname: str
    exec_duration_millis: int = Field(validation_alias=AliasChoices('exec-duration-millis'))


class YandexUserSettings(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        from_attributes=True,
    )

    uid: int
    lastFm_scrobbling_enabled: bool = Field(validation_alias=AliasChoices('lastFmScrobblingEnabled'))
    facebook_scrobbling_enabled: bool | None = None
    shuffle_enabled: bool | None = None
    add_new_track_on_playlist_top: bool | None = None
    volume_percents: int | None = None
    user_music_visibility: str | None = None
    user_social_visibility: str | None = None
    ads_disabled: bool | None = None
    modified: datetime.datetime | None = None
    rbt_disabled: bool | None = None
    theme: str | None = None
    promos_disabled: bool | None = None
    auto_play_radio: bool | None = None
    sync_queue_enabled: bool | None = None
    explicit_forbidden: bool | None = None
    child_mod_enabled: bool | None = None
    wizard_is_passed: bool | None = None
    user_collection_hue: int | None = None


class YandexUserSettingsResponse(BaseModel):
    invocation_info: InvocationInfo
    result: YandexUserSettings


class YandexTokenData(BaseModel):
    access_token: str
    token_type: str
    expires_in: str
    cid: str
