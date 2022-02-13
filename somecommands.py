import discord
import time

from discord.ext import commands
from datetime import datetime

def setup(bot: commands.Bot):
        bot.add_cog(SomeCommands(bot))

class SomeCommands(commands.Cog):
    """A couple of simple commands."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.last_msg = None

    @commands.command(name='ping')
    async def ping(self, ctx: commands.context):
        """Get the bot's current websocket latency."""
        start_time = time.time()
        message = await ctx.send("Testing Ping...")
        end_time = time.time()

        await message.edit(content=f"Pong! {round(self.bot.latency * 1000)}ms\nAPI: {round((end_time - start_time) * 1000)}ms")

    @commands.command(name='testMessage')
    async def testMessage(self, ctx: commands.context):
        """Test message with all options embed"""
        

        embed = discord.Embed(title="Hello, world!", description=":D", colour=0x87CEEB, timestamp=datetime.utcnow())
        embed.set_author(name="vcokltfre", icon_url="https://avatars.githubusercontent.com/u/16879430")
        embed.add_field(name="Field 1", value="Not an inline field!", inline=False)
        embed.add_field(name="Field 2", value="An inline field!", inline=True)
        embed.add_field(name="Field 3", value="Look I'm inline with field 2!", inline=True)
        embed.set_footer(text="Wow! A footer!", icon_url="https://cdn.discordapp.com/emojis/754736642761424986.png")

        await ctx.send(embed=embed)


    @commands.command(name='setstatus')
    async def setstatus(self, ctx: commands.context, *, text: str):
        """Set the bot's status."""
        await self.bot.change_presence(activity=discord.Game(name=text))
    
    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        channel = self.bot.get_channel(788148287391793192)

        if not channel:
            return  
        await channel.send(f"Welcome, {member}!")
    
    @commands.Cog.listener()
    async def on_message_delete(self,message: discord.Message):
        self.last_msg = message
    
    @commands.command(name="snipe")
    async def snipe(self, ctx:commands.Context):
        """A command to snipe delte messages."""
        if not self.last_msg:
            await ctx.send("There is no message to snipe!")
            return
        
        author = self.last_msg.author
        content = self.last_msg.content

        embed = discord.Embed(title=f"message from {author}", description=content)
        await ctx.send(embed=embed)




    

