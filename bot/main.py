import asyncio
import logging

import discord
from cogs.listener import ListenerCog
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


def add_cogs(bot: commands.Bot) -> None:
    bot.remove_command("help")
    bot.add_cog(WelcomeCog(bot))
    bot.add_cog(ListenerCog(bot))
    bot.add_cog(CommandsCog(bot))


async def main():
    logging.basicConfig(
        level="INFO",
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    await create_db_tables()

    bot = CustomBot(command_prefix='!', intents=intents)
    add_cogs(bot)

    await bot.start(config.bot.token)


asyncio.run(main())
