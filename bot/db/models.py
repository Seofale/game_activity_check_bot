import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class GameSession(Base):
    __tablename__ = 'game_session'

    id: Mapped[int] = mapped_column(primary_key=True)
    member_id: Mapped[int] = mapped_column(ForeignKey("members_db.id"))
    duration: Mapped[datetime.timedelta]


class MemberDb(Base):
    __tablename__ = 'members_db'

    id: Mapped[int] = mapped_column(primary_key=True)
    member_id: Mapped[int] = mapped_column(unique=True)
    guild_id: Mapped[int] = mapped_column(
        ForeignKey("guilds_db.id"),
        nullable=True
    )
    game_sessions: Mapped[list[GameSession]] = relationship()


class GuildDb(Base):
    __tablename__ = "guilds_db"

    id: Mapped[int] = mapped_column(primary_key=True)
    guild_id: Mapped[int]
    members: Mapped[list[MemberDb]] = relationship()
