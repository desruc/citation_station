import asyncio
import os
import discord


from citation_station.bot import Bot
intents = discord.Intents.default()
intents.message_content = True

bot = Bot(command_prefix='!', intents=intents)


async def main():
    await bot.load_exts()
    await bot.start(os.getenv('DISCORD_TOKEN'))


try:
    asyncio.run(main())
except KeyboardInterrupt:
    try:
        exit(0)
    except SystemExit:
        os._exit(0)
