import discord
from discord.ext import commands

Classname = 'GiveAway'
EL = 'Extention_Loader: {} has been loaded'.format(Classname)

client = discord.Client


class GiveAway(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Event
    @commands.Cog.listener()
    async def on_ready(self):
        print(EL)

    # Commands
    @commands.command(pass_context=True)
    async def giveaway(self, ctx):
        headline = '**GIVEAWAY**'
        giveawayitem = 'T-Shirt'
        embed = discord.Embed(title=giveawayitem,
                              description='Some giveaway text',
                              color=0x3A00FF)
        await ctx.send(headline, embed=embed)


def setup(client):
    client.add_cog(GiveAway(client))
