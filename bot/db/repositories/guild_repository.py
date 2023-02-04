from ..engine import async_session
from ..models import GuildDb


class GameSessionRepository:

    @classmethod
    async def create_guild(cls, guild_id) -> None:
        async with async_session() as session:
            await session.merge(
                GuildDb(guild_id=guild_id)
            )
            await session.commit()
