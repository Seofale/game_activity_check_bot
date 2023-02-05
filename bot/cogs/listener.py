import datetime
import logging
from datetime import timezone

import discord
from db.repositories import (MemberRepository, GameSessionRepository,
                             GuildRepository)
from discord.ext import commands
from utils import get_index_safe


class ListenerCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @commands.Cog.listener()
    async def on_guild_join(guild: discord.Guild) -> None:
        await GuildRepository.create_guild(guild_id=guild.id)

    @commands.Cog.listener()
    async def on_guild_remove(guild: discord.Guild) -> None:
        await GuildRepository.delete_guild(guild_id=guild.id)

    @commands.Cog.listener()
    async def on_presence_update(
        self,
        before: discord.Member,
        after: discord.Member
    ) -> None:

        # member_in_track = await MemberRepository.get_member(before.id)
        # if not member_in_track:
        #     return

        if after.activity:
            logging.info(f"{after.name} starts {after.activity.name}")

        gaming_type = discord.ActivityType.playing

        before_game = get_index_safe(
            0,
            [act for act in before.activities if act.type == gaming_type]
        )

        after_game = get_index_safe(
            0,
            [act for act in after.activities if act.type == gaming_type]
        )

        if not before_game and not after_game or before_game == after_game:
            return

        if not before_game and after_game:
            logging.info(f"{after.name} starts [GAME]{after_game.name}")

        if before_game and not after_game:
            gaming_time = datetime.datetime.now(
                timezone.utc) - before_game.start

            await GameSessionRepository.create_session(
                member_id=before.id,
                duration=gaming_time
            )

            logging.info(f"{after.name} end playing in {before_game.name}, \
                (duration: {str(gaming_time)})")

        if before_game and after_game:
            pass
