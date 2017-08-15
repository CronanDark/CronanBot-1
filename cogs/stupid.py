import discord
from discord.ext import commands

class Stupid():
    """Stupid commands Cronan builds in for no reason what so ever"""

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def cronan(self):
        """why? just why?"""
        await self.bot.say("ew... y do u like that cringy yter who cant even code me right or have me alive 24/7")


def setup(bot):
    n = Stupid(bot)
    bot.add_cog(n)
