import asyncio
import os
import logging
import discord
from citation_station.bot import Bot

logging.basicConfig(level=logging.INFO)

intents = discord.Intents.default()
intents.message_content = True

bot = Bot(command_prefix="!", intents=intents)


async def main():
    await bot.start(os.getenv("DISCORD_TOKEN"))


try:
    logging.info("Starting routine")
    asyncio.run(main())
except Exception as e:
    logging.exception("An error has occurred: %s", e)
except KeyboardInterrupt:
    try:
        exit(0)
    except SystemExit:
        os._exit(0)
