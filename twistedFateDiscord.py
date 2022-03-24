import discord
import json

from discord.ext import commands

#----- Me liblary --------
from adminHelpers import addUserToJson
from TwistedFate import main


def setup(bot: commands.Bot):
        bot.add_cog(TwistedFateDiscord(bot))

class TwistedFateDiscord(commands.Cog):
    """A couple of simple commands."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        

    @commands.command(name='tfAdd')
    async def tfAdd(self, ctx: commands.context, *arg):
        
        id = ctx.author.id
        SumName = ' '.join(arg)

        info = main.getSummoner(SumName)
        SumId = info['accountId']
        discordName = ctx.author.name
        result = addUserToJson(id, SumId, discordName)

        await ctx.send(info)

    @commands.command(name='tfRank')
    async def tfRank(self, ctx: commands.context):
        
        with open('assets/tfConfig.json','r') as f:
            obj_list = json.load(f)

        sumIds = []

        for i in range(len(obj_list)):
            sumIds.append(obj_list[i]['SumId'])
        
        main.xd(sumIds)
        await ctx.send('Poszło?')

    
