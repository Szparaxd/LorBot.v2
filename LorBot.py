import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has joined Discord!')

bot.load_extension("somecommands")
bot.load_extension("lastVersionCommands")
bot.load_extension("twistedFateDiscord")
#bot.load_extension('testcommands')

bot.run('ODU0MzA5MjkyMDcyNTAxMjc5.YMiDhw._y1r5lxMuZ4eXR-pSyV5xroLLdo')