import discord
import os
from apscheduler.triggers.cron import CronTrigger

from citation_station.utils.quote import get_quote

# This will be in UTC time while in a docker container
HOUR_TO_SEND = os.getenv('HOUR_TO_SEND') if os.getenv(
    'HOUR_TO_SEND') else 22  # 10pm UTC = 8am AEST


class DailyCitationJob():
    def __init__(self, bot):
        self.bot = bot

    def schedule(self, scheduler):
        print("Scheduling daily citation job...")
        job = scheduler.add_job(self.send_daily_citation, CronTrigger(
            year="*", month="*", day="*", hour=HOUR_TO_SEND, minute=0, second=0
        ))
        return job

    async def send_daily_citation(self):
        if (self.bot.is_ready()):
            try:
                channel = self.bot.get_channel(int(os.getenv('CHANNEL_ID')))
                quote = await get_quote()

                embed = self.get_embed(quote[0], quote[1])
                await channel.send(embed=embed)
            except:
                print("Failed to get channel")

    def get_embed(self, quote: str, author: str):
        description = f"**Quote:**\n{quote}\n\n**Author:**\n{author}"

        embed = discord.Embed(
            title="Quote of the Day",
            description=description,
            color=discord.Colour.random()
        )
        return embed
