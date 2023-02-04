import constants
from db.repositories.member_repository import MemberRepository
from discord.ext import commands


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

        await MemberRepository.create_member(
            ctx.author.id, ctx.guild.id
        )

        if ctx.author.dm_channel:
            await ctx.author.dm_channel.send(constants.TRACK_ADDED)
            return

        await ctx.author.create_dm()
        await ctx.author.dm_channel.send(constants.TRACK_ADDED)

        await ctx.message.delete(delay=2.0)

    @commands.command()
    async def end_track(self, ctx: commands.Context) -> None:
        if ctx.guild not in self.bot.guilds:
            return

        await MemberRepository.delete_member(ctx.author.id)

        if ctx.author.dm_channel:
            await ctx.author.dm_channel.send(constants.TRACK_REMOVED)
            return

        await ctx.author.create_dm()
        await ctx.author.dm_channel.send(constants.TRACK_REMOVED)

        await ctx.message.delete(delay=2.0)
