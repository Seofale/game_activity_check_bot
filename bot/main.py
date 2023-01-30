import discord
from cogs.activity_check import ActivityCheckCog
from cogs.welcome import WelcomeCog
from discord.ext import commands


class CustomBot(commands.Bot):
    async def on_ready(self):
        print(f"We have logged in as {self.user}")


intents = discord.Intents().all()

bot = CustomBot(command_prefix='!', intents=intents)
bot.add_cog(WelcomeCog(bot))
bot.add_cog(ActivityCheckCog(bot))
bot.run(
    'MTA2ODE0ODEwODk2NzU1NTA3Mw.GSzISp.cc9vtcWmuQFcYmU502kdOh_DZ7EuHs8EEGNTik'
)
