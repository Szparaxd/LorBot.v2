from turtle import title
import discord
import random

from discord.ext import commands




def setup(bot: commands.Bot):
    bot.add_cog(LastVersionCommands(bot))

class LastVersionCommands(commands.Cog):
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.last_msg = None

    @commands.command(name='toxic')
    async def toxic(self, ctx: commands.context):
        rdm = random.randrange(101)
        msg = "Poziom toksyczności wynosi: " + str(rdm) + "%"
        embed = discord.Embed(title="Toxic", description=msg)
        await ctx.send(embed=embed)

    @commands.command(name='simp')
    async def simp(self, ctx: commands.context):
        rdm = random.randrange(101)
        msg = "Simprate: " + str(rdm) + "%"
        embed = discord.Embed(title="Simp", description=msg)
        await ctx.send(embed=embed)

    @commands.command(name='dick')
    async def dick(self, ctx: commands.context):
        rdm = random.randrange(30)
        msg = "Twój dick ma " + str(rdm) + "cm"
        embed = discord.Embed(title="Dick", description=msg)
        await ctx.send(embed=embed)

    @commands.command(name='iq')
    async def iq(self, ctx: commands.context):
        rdm = random.randrange(201)
        msg = "Masz " + str(rdm) + "iq" 
        embed = discord.Embed(title="Iq", description=msg)
        await ctx.send(embed=embed)

    @commands.command(name='pussy')
    async def pussy(self, ctx: commands.context):
        msg = "Chętnie zobaczymy"
        embed = discord.Embed(title="=Pussy", description=msg)
        await ctx.send(embed=embed)
    
    @commands.command(name='tilt')
    async def tilt(self, ctx: commands.context):
        zmienna = random.randrange(0, 11)
        s = str(zmienna)

        if (zmienna == 10):
            msg = "Poziom Szymon ~ Daj sobie spokój na dziś"
        elif (zmienna == 9):
            msg = "Poziom Kacper ~ Dobra ff to nie ma sensu"
        elif (zmienna == 8):
            msg = "Poziom Bartek ~ Wkurwiony jak sam diabeł"
        else:
            msg = "Dziś można grać "
        embed = discord.Embed(title="=tilt", description=msg)
        await ctx.send(embed=embed)

    @commands.command(name='thotrate')
    async def pussy(self, ctx: commands.context):
        rdm = random.randrange(100)
        msg = "thotrate: " + str(rdm) + "%" 
        embed = discord.Embed(title="Thotrate", description=msg)
        await ctx.send(embed=embed)

    @commands.command(name='hug')
    async def hug(self, ctx: commands.context):
        await ctx.send("https://tenor.com/bpJ0h.gif")
    
    @commands.command(name='sad')
    async def sad(self, ctx: commands.context):
        await ctx.send("https://tenor.com/Ulb6.gif")

    @commands.command(name='jednorozec')
    async def jednorozec(self, ctx: commands.context):
        await ctx.send("https://cdn.discordapp.com/attachments/754459079107412079/854681869827178506/unknown.png")

    @commands.command(name='rabbit')
    async def rabbit(self, ctx: commands.context):
        await ctx.send("https://cdn.discordapp.com/attachments/754459079107412079/854432534862626856/unknown.png")

    @commands.command(name='qń')
    async def qn(self, ctx: commands.context):
        await ctx.send("https://cdn.discordapp.com/attachments/754459079107412079/854850444849315852/received_322974979328752.jpeg")
    
    @commands.command(name='60')
    async def szezdziesiat(self, ctx: commands.context):
        await ctx.send("https://cdn.discordapp.com/attachments/788148287391793192/892511106541686784/received_373078791175589.jpeg")
    
    @commands.command(name='rozlam')
    async def rozlam(self, ctx: commands.context):
        embed = discord.Embed(title="rozlam")
        embed.add_field(name="Rozłam pierwszy", value='popatrz na to tak\nkto ma ich zintować jak nie ty \npotrzebują Cię \n"Ja idę na bota" ~ Łukasz Grochowiak 2021' ,inline=False)
        embed.add_field(name='Rozłam drugi', value='Ja pierdole debilu jebany czemu zbanowałeś zeda" ~ Mateusz Górczak 2021',inline=False)
        embed.add_field(name='Rozłam trzeci', value='Wy macie takie jazdy na bani" ~ Adam Lorek 2021',inline=False)
        embed.add_field(name="Rozłam czwarty", value='Nie trzeba umieć grać jungle żeby zgankować" ~ Kacper Dropek 2021',inline=False)
        await ctx.send(embed=embed)


    



    



    