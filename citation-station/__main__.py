import asyncio
import os
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


async def load():
    for filename in os.listdir('./citation-station/events'):
        if filename.endswith('.py'):
            await bot.load_extension(f'citation-station.events.{filename[:-3]}')


async def main():
    await load()
    await bot.start(os.getenv('DISCORD_TOKEN'))


try:
    asyncio.run(main())
except KeyboardInterrupt:
    try:
        exit(0)
    except SystemExit:
        os._exit(0)
