import constants
from db.engine import async_session
from db.models import MemberDb
from discord.ext import commands
from sqlalchemy import delete


class CommandsCog(commands.Cog):

    def __init__(self, bot):
        self.bot: commands.Bot = bot
        super().__init__()

    @commands.command()
    async def help(self, ctx: commands.Context) -> None:
        if ctx.guild not in self.bot.guilds:
            return

        await ctx.message.channel.send(constants.HELP)

    @commands.command()
    async def start_track(self, ctx: commands.Context) -> None:
        if ctx.guild not in self.bot.guilds:
            return

        async with async_session() as session:
            await session.merge(MemberDb(member_id=ctx.author.id))
            await session.commit()

        if ctx.author.dm_channel:
            await ctx.author.dm_channel.send(constants.TRACK_ADDED)
            return

        await ctx.author.create_dm()
        await ctx.author.dm_channel.send(constants.TRACK_ADDED)

    @commands.command()
    async def end_track(self, ctx: commands.Context) -> None:
        if ctx.guild not in self.bot.guilds:
            return

        sql = delete(MemberDb).where(MemberDb.member_id == ctx.author.id)
        async with async_session() as session:
            await session.execute(sql)
            await session.commit()

        if ctx.author.dm_channel:
            await ctx.author.dm_channel.send(constants.TRACK_REMOVED)
            return

        await ctx.author.create_dm()
        await ctx.author.dm_channel.send(constants.TRACK_REMOVED)
