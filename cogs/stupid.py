import discord
from discord.ext import commands
import asyncio

class Stupid():
    """Stupid commands Cronan builds in for no reason what so ever"""

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def cronan(self):
        """why? just why?"""
        await self.bot.say("ew... y do u like that cringy yter who cant even code me right or have me alive 24/7")

    @commands.command(pass_context=True)
    async def annoyme(self, ctx):
        """The bot will annoy you"""
        user = ctx.message.author.id
        usermention = "<@" + user + ">"
        for i in range(10):
            await self.bot.say(usermention)
            await asyncio.sleep(600)

    @commands.command(pass_context=True)
    async def spam(self, ctx, message):
        """spams chat with what u make it say.
        Note: You will be responsible for any trouble you get into"""
        msgdude = str(message)
        user = str(ctx.message.author.name)
        msgdel = ctx.message
        await self.bot.delete_message(msgdel)
        for i in range(25):
            await self.bot.say(msgdude)
            await asyncio.sleep(1)
        await asyncio.sleep(5)
        await self.bot.say(user + " made me do it")


def setup(bot):
    n = Stupid(bot)
    bot.add_cog(n)
