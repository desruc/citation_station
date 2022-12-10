from discord.ext import tasks, commands


class SendCitation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.send_daily_citation.start()

    def cog_unload(self):
        self.send_daily_citation.cancel()

    @tasks.loop(seconds=5.0)
    async def send_daily_citation(self):
        try:
            channel = self.bot.get_channel(717531958535782414)
            await channel.send("Keep doing your thing")
        except:
            print("Failed to get channel")


async def setup(bot):
    await bot.add_cog(SendCitation(bot))
