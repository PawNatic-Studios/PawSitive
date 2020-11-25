import os
import random
import asyncio
from itertools import cycle

import discord
from discord.ext import commands, tasks

from config import STATUS1
from config import STATUS2
from config import STATUS3

import discord
from discord.ext import commands

from config import PREFIX
from config import SYSPATH
from config import TOKEN

client = commands.Bot(command_prefix=PREFIX)

status = cycle([STATUS1, STATUS2, STATUS3])

#######################################################################
######################## M A I N  L O A D E R #########################
#######################################################################

@client.event
async def on_ready():
    print('\r\n' + client.user.display_name + ' has been established...\r\n')
    change_status.start()

@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)), status=discord.Status.online)

#######################################################################
##########################Extention loader#############################
#######################################################################

# Extention loader
@client.command()
async def load(ctx, extention):
    client.load_extension(f'extentions.{extention}')
    await ctx.channel.purge(limit=1)
    print('Extention_loader: loaded extention ' + extention)
    embed = discord.Embed(title='Extention Loader',
                          description='successesfully loaded extention: {}'.format(extention),
                          color=0x3A00FF)
    await ctx.send(embed=embed, delete_after=10)

# Extention unloader
@client.command()
async def unload(ctx, extention):
    client.unload_extension(f'extentions.{extention}')
    await ctx.channel.purge(limit=1)
    print('Extention_loader: unloaded extention ' + extention)
    embed = discord.Embed(title='Extention Loader',
                          description='successesfully unloaded extention: {}'.format(extention),
                          color=0x3A00FF)
    await ctx.send(embed=embed, delete_after=10)

# get os filedir for extentions and load them in
for filename in os.listdir(SYSPATH):
    if filename.startswith('#'):
        print('\r\nExtention_Loader: ' + (filename[:-3]) + ' is deactivated and will be ignored!\r\n')
    else:
        if filename.endswith('.py'):
            client.load_extension(f'extentions.{filename[:-3]}')


@client.command()
async def reload(ctx, extention):
    client.reload_extension(f'extentions.{extention}')
    print('Extention_loader: reloaded extention ' + extention)
    await ctx.channel.purge(limit=1)
    embed = discord.Embed(title='Extention Loader',
                          description='successesfully reloaded extention: {}'.format(extention),
                          color=0x3A00FF)

    await ctx.send(embed=embed, delete_after=10)

# End of Extentions

#######################################################################
######################E X P E R I M E N T A L##########################
#######################################################################

# End of Experimental

client.run(TOKEN)
