from discord.ext import commands


class OnReady(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener('on_ready')
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')


async def setup(bot):
    await bot.add_cog(OnReady(bot))
