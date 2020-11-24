import discord
from discord.ext import commands, tasks

import time
import asyncio
from itertools import cycle

from config import STATUS1
from config import STATUS2
from config import STATUS3

Classname = 'Status'
EL = 'Extention_Loader: {} has been loaded'.format(Classname)

client = discord.client
status = cycle([STATUS1, STATUS2, STATUS3])


class Status(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.client.change_status.start()

    # Event
    @commands.Cog.listener()
    async def on_ready(self):
        print(EL)

    # Tasks
    @tasks.loop(seconds=1.0)
    async def change_status(self):
        print('Bot has change status')
        await self.client.change_presence(activity=discord.Game(next(status)))

    # Commands
    @commands.command(pass_context=True)
    async def ping(self, ctx):
        print('Ping cmd executed')
        channel = ctx.message.channel
        t1 = time.perf_counter()
        await ctx.send(channel, delete_after=0)
        t2 = time.perf_counter()
        pingtime = ("Ping: {}ms".format(round((t2 - t1) * 1000)))
        embed = discord.Embed(title='Still alive',
                              description=pingtime,
                              color=0x3A00FF)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Status(client))
