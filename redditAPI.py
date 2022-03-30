import discord
import time
import requests
import json
import re
import random

from datetime import datetime
from discord.ext import commands
from adminHelpers import logger

def setup(bot: commands.Bot):
    bot.add_cog(RedditAPI(bot))

def getHeaders():
    with open('assets/passwd.json', 'r') as f:
        data = json.load(f)

    result = {
            'grant_type' : data['grant_type'],
            'username' : data['userName'],
            'password' : data['password'],
            'client_Id' : data['client_Id'],
            'client_secret' : data['client_secret']
        }

    auth = requests.auth.HTTPBasicAuth(result['client_Id'], result['client_secret'])

    headers = {
        'User-Agent': 'MyAPI/0.0.1'
    }

    res = requests.post('https://www.reddit.com/api/v1/access_token',
                        auth=auth, data= result, headers=headers)

    TOKEN = res.json()
    headers['Authorization'] = 'bearer' + ' ' +TOKEN['access_token']
    
    return headers


def r(arg=''):
    headers = getHeaders()

    if not arg:
        return 'Nie podałeś czego szukać :/'

    response = requests.get('https://oauth.reddit.com/r/'+ arg +'/hot', headers=headers)
    
    if response.status_code == 404:
        return 'Prawdopodobnie nie ma takiego tagu'
    
    data =  response.json()['data']['children']

    result = []
    for i in data:
        result.append(i['data']['url'])

    reg = re.compile(".*i.imgur.*")
    filter_list = list(filter(reg.match, result))
    
    return(random.choice(filter_list))




class RedditAPI(commands.Cog):
    """API reddit"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @commands.command(name='r')
    async def r(self, ctx: commands.context, arg):

        embed = discord.Embed(title='Random reddit' + '-'+arg, colour=0x87CEEB,timestamp=datetime.utcnow())

        if not arg:
           await ctx.send('Nie podałeś czego szukać ¯\_(ツ)_/¯')
           return

        headers = getHeaders()
        res = requests.get('https://oauth.reddit.com/r/'+ arg +'/hot', headers=headers)

        logger.debug(res.status_code)
        if res.status_code == 404:
            await ctx.send('Prawdopodobnie nie ma takiego tagu')
            return
        elif(not res.json()['data']):
            await ctx.send('Prawdopodobnie nie ma takiego tagu')
            return
      
        data =  res.json()['data']['children']

        result = []
        for i in data:
            result.append(i['data']['url'])

        reg = re.compile(".*\.(jpg|png|txt)")
        filter_list = list(filter(reg.match, result))
        if(len(filter_list) < 1):
            await ctx.send('Niestety nic nie znalazłem :c')
            return

        img_url = random.choice(filter_list)
        embed.set_image(url=img_url)

        await ctx.send(embed=embed)

