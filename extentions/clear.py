import discord
from discord.ext import commands

Classname = 'Clear'
EL = 'Extention_Loader: {} has been loaded'.format(Classname)

client = discord.Client


class Clear(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Event
    @commands.Cog.listener()
    async def on_ready(self):
        print(EL)

    # Commands
    @commands.command(pass_context=True)
    async def clear(self, ctx, number):
        print(f'Clear cmd has been executed by {ctx.author} in channel #{ctx.channel}')

        def mess_is_not_pinned(mess):
            return not mess.pinned

        count = int(number)
        await ctx.channel.purge(limit=count, check=mess_is_not_pinned)
        print(f'{count} messages have been deleted!')

def setup(client):
    client.add_cog(Clear(client))
