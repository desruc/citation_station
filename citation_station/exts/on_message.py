from discord.ext import commands


class OnMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener('on_message')
    async def on_message(self, message):
        if message.author.bot:
            return
        await self.process_commands(message)


async def setup(bot):
    await bot.add_cog(OnMessage(bot))
