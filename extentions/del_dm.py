import discord
from discord.ext import commands

Classname = 'DelDM'
EL = 'Extention_Loader: {} has been loaded'.format(Classname)

class DelDM(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Event"
    @commands.Cog.listener()
    async def on_ready(self):
        print(EL)

    # Commands
    @commands.command()
    async def deldm(self, ctx):
        user = ctx.author

        await ctx.channel.purge(limit=1)

        async for message in user.history(limit=100):
            if message.author == self.client.user:
                await message.delete()

def setup(client):
    client.add_cog(DelDM(client))
