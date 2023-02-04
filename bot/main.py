import asyncio

import discord
from cogs.activity_check import ActivityCheckCog
from cogs.commands import CommandsCog
from cogs.welcome import WelcomeCog
from config import load_config
from db.engine import create_db_tables
from discord.ext import commands


class CustomBot(commands.Bot):
    async def on_ready(self):
        print(f"We have logged in as {self.user}")


intents = discord.Intents().all()

config = load_config()


async def main():

    await create_db_tables()

    bot = CustomBot(command_prefix='!', intents=intents)
    bot.add_cog(WelcomeCog(bot))
    bot.add_cog(ActivityCheckCog(bot))
    bot.remove_command("help")
    bot.add_cog(CommandsCog(bot))
    await bot.start(config.bot.token)


asyncio.run(main())
