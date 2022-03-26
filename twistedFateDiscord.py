from email.policy import default
import discord
import json

from discord.ext import commands
from datetime import datetime

#----- Me liblary --------
from adminHelpers import addUserToJson, logger
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
    async def tfRank(self, ctx: commands.context, arg):
        
        with open('assets/tfConfig.json','r') as f:
            obj_list = json.load(f)

        sumIds = []

        for i in range(len(obj_list)):
            sumIds.append(obj_list[i]['SumId'])
        
        match arg:
            case 'flex':
                title = 'Gorsza kolejka'
                rank = main.summonersSorted(sumIds, 'flex')

            case _:
                title = 'Solo'
                rank = main.summonersSorted(sumIds)

        txt = ''
        for idx,val in enumerate(rank):
            txt += str(idx+1) + '. ' + val + '\n'

        logger.debug(txt)

        embed = discord.Embed(title='Ranking Discordowy lola - '+ title,description=txt, colour=0x87CEEB, timestamp=datetime.utcnow())

        await ctx.send(embed=embed)

    
