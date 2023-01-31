import discord
from cogs.activity_check import ActivityCheckCog
from cogs.welcome import WelcomeCog
from discord.ext import commands

from config import load_config


class CustomBot(commands.Bot):
    async def on_ready(self):
        print(f"We have logged in as {self.user}")


intents = discord.Intents().all()

config = load_config()

bot = CustomBot(command_prefix='!', intents=intents)
bot.add_cog(WelcomeCog(bot))
bot.add_cog(ActivityCheckCog(bot))
bot.run(config.bot.token)
