import discord
from discord.ext import commands

Classname = 'init'
EL = 'Extention_Loader: {} has been loaded'.format(Classname)

# client = discord.Client

class Init(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Event
    @commands.Cog.listener()
    async def on_ready(self):
        print(EL)


def setup(client):
    client.add_cog(init(client))
