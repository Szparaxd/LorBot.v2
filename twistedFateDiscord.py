import discord

import TwistedFate.main as tf

from discord.ext import commands

def setup(bot: commands.Bot):
        bot.add_cog(TwistedFateDiscord(bot))

class TwistedFateDiscord(commands.Cog):
    """A couple of simple commands."""

    @commands.command(name='rank')
    async def rank(self, ctx: commands.context):
        await ctx.send(tf.jsonRead('TwistedFate\config.json'))
