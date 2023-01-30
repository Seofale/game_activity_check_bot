import constants
import discord
from discord.ext import commands


class WelcomeCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        super().__init__()

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message) -> None:
        if message.author == self.bot.user:
            return

        if message.guild not in self.bot.guilds:
            await message.channel.send(constants.DONT_ANSWER_IN_PM)

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member) -> None:

        if member.dm_channel:
            await member.dm_channel.send(
                constants.WELCOME_IN_CHANNEL_INFO.format(member.guild.name)
            )
            return

        await member.create_dm()
        await member.dm_channel.send(
            constants.WELCOME_IN_CHANNEL_INFO.format(member.guild.name)
        )
