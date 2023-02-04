import datetime
from datetime import timezone

import discord
from db.repositories import MemberRepository, GameSessionRepository
from discord.ext import commands
from utils import get_index_safe


class ActivityCheckCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @commands.Cog.listener()
    async def on_presence_update(
        self,
        before: discord.Member,
        after: discord.Member
    ) -> None:

        member_in_track = await MemberRepository.get_member(before.id)
        if not member_in_track:
            return

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
            print(f"{after.name} начал играть в {after_game.name}")

        if before_game and not after_game:
            gaming_time = str(
                datetime.datetime.now(timezone.utc) -
                before_game.start
            )

            await GameSessionRepository.create_session(
                member_id=before.id,
                duration=gaming_time
            )

            print(f"{after.name} закончил играть в {before_game.name}, \
                он играл в неё {gaming_time}")

        if before_game and after_game:

            print(f"{after.name} изменил игру на {after_game.name}, \
                он играл в {before_game.name} \
                {before_game.end - before_game.start}")
