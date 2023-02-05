from sqlalchemy import delete

from ..engine import async_session
from ..models import GuildDb


class GuildRepository:

    @classmethod
    async def create_guild(cls, guild_id) -> None:
        async with async_session() as session:
            await session.merge(
                GuildDb(guild_id=guild_id)
            )
            await session.commit()

    @classmethod
    async def delete_guild(cls, guild_id) -> None:
        sql = delete(GuildDb).where(GuildDb.member_id == guild_id)
        async with async_session() as session:
            await session.execute(sql)
            await session.commit()
