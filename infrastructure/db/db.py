from datetime import datetime

from aiocache import cached
from aiocache.serializers import PickleSerializer
from loguru import logger
from peewee_async import Manager

from tg_bot_template import dp
from interfaces.bot.states import UserFormData
from services.feature_flags import TgUser
from infrastructure.db.models import users


def _get_conn() -> Manager:
    return dp.get_db_conn()


async def check_user_registered(*, tg_user: TgUser) -> bool:
    return bool(await get_user_for_filters(tg_user=tg_user))


@cached(ttl=0.2, serializer=PickleSerializer())
async def get_user_for_filters(*, tg_user: TgUser) -> users | None:
    return await get_user(tg_user=tg_user)


async def get_user(*, tg_user: TgUser) -> users | None:
    try:
        user = await _get_conn().get(users, social_id=tg_user.tg_id)
    except Exception:
        return None
    else:
        user.username = tg_user.username
        await _get_conn().update(user)
        return user  # type: ignore[no-any-return]


async def create_user(*, tg_user: TgUser) -> None:
    await _get_conn().create(
        users, social_id=tg_user.tg_id, username=tg_user.username, registration_date=datetime.now()  # noqa: DTZ005
    )
    logger.info(f"New user[{tg_user.username}] registered")


async def update_user_info(*, tg_user: TgUser, user_form_data: UserFormData) -> None:
    user = await get_user(tg_user=tg_user)
    if user is not None:
        user.name = user_form_data.name
        user.info = user_form_data.info
        user.photo = user_form_data.photo
        await _get_conn().update(user)


async def incr_user_taps(*, tg_user: TgUser) -> None:
    user = await get_user(tg_user=tg_user)
    if user is not None:
        user.taps += 1
        await _get_conn().update(user)


async def get_all_users() -> list[users]:
    return list(await _get_conn().execute(users.select().order_by(users.taps.desc())))
