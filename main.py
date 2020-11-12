import discord
import asyncio
from discord import Member

import settings
import help

client = discord.Client()

clientID = settings.ID
user = client.get_user(clientID)

p = settings.PREFIX
helplist = help.list

#On ready console log
@client.event
async def on_ready():
    print('{0.user} has logged in Successesfully!\r\n'.format(client)
            + '\r\n\r\n'
            + '{0.user} Version '.format(client) + (settings.VERSION) + '\r\n'
            + 'Discord Py - Rewrite version ' + discord.__version__
            + '\r\n')

    #Add Tasks to workloop
    client.loop.create_task(status_task())


#Test client active/presence functions on server
async def status_task():
    while True:
        await client.change_presence(activity=discord.Game(settings.STATUS1), status=discord.Status.online)
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(settings.STATUS2), status=discord.Status.online)
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game(settings.STATUS3), status=discord.Status.online)
        await asyncio.sleep(10)

def is_not_pinned(mess):
    return not mess.pinned

@client.event
async def  on_message(message):
    if message.author.bot:
        return

#Help command
    if p + 'help' in message.content:
        embed = discord.Embed(title='**How to use {}**'.format(settings.NAME),
                    description= helplist,
                    color = 0x3A00FF)
        await message.author.send(embed=embed)
        await message.channel.purge(limit=1, check = is_not_pinned)


#Clear command
    #clear all function
    if message.content.startswith(p + 'clear' + ' all'):
        #check for permissions
        if message.author.permissions_in(message.channel).manage_messages:
            V_all = 999999999999
            await message.channel.purge(limit=V_all, check=is_not_pinned)
            embed = discord.Embed(title='**Clearing Chat**',
                        description = '`' + message.author.name + ' has deleted all messages!`',
                        color = 0x3A00FF)
            await message.channel.send(embed=embed)


    #clear [lines]
    if message.content.startswith(p + 'clear'):
        #check for permissions
        if message.author.permissions_in(message.channel).manage_messages:
            args = message.content.split(' ')
            if len(args) == 2:
                if args[1].isdigit():
                    count = int(args[1]) + 1
                    deleted = await message.channel.purge(limit=count, check=is_not_pinned)          
                    embed = discord.Embed(title='**Clearing Chat**',
                        description = '`' + message.author.name + ' has deleted {} messages!`'.format(len(deleted)-1),
                        color = 0x3A00FF)
                    await message.channel.send(embed=embed)


            #missing lines
            if len(args) != 2:
                embed = discord.Embed(title='**Clear command**',
                    description='Missing or incorrect argument.\r\n\r\n'
                        '`#clear [lines/args]`',
                    color = 0x3A00FF)
                await message.author.send(embed=embed)


        #no permission
        else:
            embed = discord.Embed(title='**Incorrect Permission**',
                description='Missing permission - in (message.channel).manage_messages!\r\n'
                    '`Only moderators and above are allowed to use the command [#clear]`',
                color=0x22a7f0)
            await message.author.send(embed=embed)
            

#Clear dms
    if message.content.startswith(p + 'clear' + ' dms'):
        deletelast
        print('Deleted dms')

client.run(settings.TOKEN)