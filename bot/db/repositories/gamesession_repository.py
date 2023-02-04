from ..engine import async_session
from ..models import GameSession


class GameSessionRepository:

    @classmethod
    async def create_session(cls, member_id, duration) -> None:
        async with async_session() as session:
            await session.merge(
                GameSession(member_id=member_id, duration=duration)
            )
            await session.commit()
