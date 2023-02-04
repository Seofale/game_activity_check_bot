from typing import Union

from sqlalchemy import delete, select

from ..engine import async_session
from ..models import MemberDb


class MemberRepository:

    @classmethod
    async def create_member(cls, member_id: int, guild_id: int) -> None:
        async with async_session() as session:
            await session.merge(
                MemberDb(member_id=member_id, guild_id=guild_id)
            )
            await session.commit()

    @classmethod
    async def delete_member(cls, member_id: int) -> None:
        sql = delete(MemberDb).where(MemberDb.member_id == member_id)
        async with async_session() as session:
            await session.execute(sql)
            await session.commit()

    @classmethod
    async def get_member(cls, member_id: int) -> Union[MemberDb, None]:
        async with async_session() as session:
            sql = select(MemberDb).where(
                MemberDb.member_id == member_id)
            result = await session.execute(sql)
            member = result.scalar()

            if member:
                return member

            return None
