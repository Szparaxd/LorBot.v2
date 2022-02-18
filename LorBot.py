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

bot.run('ODU0MzA5MjkyMDcyNTAxMjc5.YMiDhw.WShdj-i3DqsWH4d8c31GTHkzV1c')