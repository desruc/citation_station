import datetime
import discord
from discord.ext import tasks, commands
import os

from citation_station.bot import Bot
from citation_station.utils.quote import get_quote

# This will be in UTC time while in a docker container
HOUR_TO_SEND = 9


class SendCitation(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot
        self.send_daily_citation.start()

    def cog_unload(self):
        self.send_daily_citation.cancel()

    @tasks.loop(minutes=60.0)
    async def send_daily_citation(self):
        now = datetime.datetime.now()

        if (self.bot.is_ready() and now.hour == HOUR_TO_SEND):
            try:
                channel = self.bot.get_channel(int(os.getenv('CHANNEL_ID')))
                quote = await get_quote()

                embed = get_embed(quote[0], quote[1])
                await channel.send(embed=embed)
            except:
                print("Failed to get channel")


def get_embed(quote: str, author: str):
    description = f"**Quote:**\n{quote}\n\n**Author:**\n{author}"

    embed = discord.Embed(
        title="Quote of the Day",
        description=description,
        color=discord.Colour.random()
    )
    return embed


async def setup(bot):
    await bot.add_cog(SendCitation(bot))
