from discord.ext import commands

from citation_station.scheduler.scheduler import Scheduler


class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        print("Initializing bot...")
        self.scheduler = Scheduler(self)
        super().__init__(*args, **kwargs)

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        self.scheduler.initialize()

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        await self.process_commands(message)
