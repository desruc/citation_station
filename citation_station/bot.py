import os
from discord.ext import commands

from citation_station.scheduler.scheduler import Scheduler

class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        self.scheduler = Scheduler(self)

        super().__init__(*args, **kwargs)

    async def load_exts(self):
        for filename in os.listdir('./citation_station/exts'):
            if filename.endswith('.py'):
                try:
                    await self.load_extension(f'citation_station.exts.{filename[:-3]}')
                    print(f"Loaded extension '{filename}'")
                except Exception as e:
                    print(f"Failed to load extension {filename}. Error: {e}")

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        self.scheduler.initialize()


    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        await self.process_commands(message)
