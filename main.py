import discord
from discord.ext import commands

import paw_settings

client = commands.Bot(command_prefix='!')

#Login check on console
@client.event
async def on_ready():
    print('{0.user} has logged in Successesfully!'.format(client))
    print('Version ' + (paw_settings.VERSION)) 

#Test client active functions on server
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('xyc'):
        await message.channel.send('PawSitive is still running...')


client.run(paw_settings.TOKEN)