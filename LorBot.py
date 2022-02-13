import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

bot.load_extension("somecommands")

bot.run('ODU0MzA5MjkyMDcyNTAxMjc5.YMiDhw.WShdj-i3DqsWH4d8c31GTHkzV1c')