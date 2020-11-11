import discord
import asyncio
from discord import Member

import paw_settings

client = discord.Client()


#On ready console log
@client.event
async def on_ready():
    print('{0.user} has logged in Successesfully!'.format(client))
    print('Version ' + (paw_settings.VERSION)) 


#Add Tasks to workloop

#Status
    client.loop.create_task(status_task())

#Test client active/presence functions on server
async def status_task():
    while True:
        await client.change_presence(activity=discord.Game('Stay PawSitive'), status=discord.Status.online)
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game('Doing Bot things'), status=discord.Status.online)
        await asyncio.sleep(10)
        await client.change_presence(activity=discord.Game('#help'), status=discord.Status.online)
        await asyncio.sleep(10)

#Define values
def is_not_pinned(mess):
    return not mess.pinned

@client.event
async def  on_message(message):
    if message.author.bot:
        return

#Help command
    if '#help' in message.content:
        await message.channel.send('**How to use PAW**\r\n'
            '`#help - Shows all available commands`')

#Userinfo command
    if message.content.startswith('#userinfo'):
        args = message.content.split(' ')
        if len(args) == 2:
            member: Member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
            if member:
                embed = discord.Embed(title='Userinfo für {}'.format(member.name),
                                      description='Dies ist eine Userinfo für den User {}'.format(member.mention),
                                      color=0x22a7f0)
                embed.add_field(name='Server beigetreten', value=member.joined_at.strftime('%d/%m/%Y, %H:%M:%S'),
                                inline=True)
                embed.add_field(name='Discord beigetreten', value=member.created_at.strftime('%d/%m/%Y, %H:%M:%S'),
                                inline=True)
                rollen = ''
                for role in member.roles:
                    if not role.is_default():
                        rollen += '{} \r\n'.format(role.mention)
                if rollen:
                    embed.add_field(name='Rollen', value=rollen, inline=True)
                embed.set_thumbnail(url=member.avatar_url)
                embed.set_footer(text='Ich bin ein EmbedFooter.')
                mess = await message.channel.send(embed=embed)
                await mess.add_reaction('🚍')
                await mess.add_reaction('a:tut_herz:662606955520458754')

                await message.channel.send(embed=embed)
        else:
            embed = discord.Embed(title='**Userinfo Command**',
                description='Missing or incorrect argument **USER**,\r\n'
                    '`#userinfo [User]`',
                color=0x22a7f0)
            await message.channel.send(embed=embed)

#Clear chat command, except Pinned            
    if message.content.startswith('#clear'):
        #check for permissions
        if message.author.permissions_in(message.channel).manage_messages:
            args = message.content.split(' ')
            if len(args) == 2:
                if args[1].isdigit():
                    count = int(args[1]) + 1
                    deleted = await message.channel.purge(limit=count, check=is_not_pinned)
                    await message.channel.send('`{} Messages have been deleted!`'.format(len(deleted)-1))
            #missing lines
            if len(args) != 2:
                embed = discord.Embed(title='**Clear command**',
                    description='Missing or incorrect argument **lines**\r\n'
                        '`#clear [lines]`',
                    color=0x22a7f0)
                await message.channel.send(embed=embed)
        #no permission
        else:
            embed = discord.Embed(title='**Incorrect Permission**',
                description='Missing permission - in (message.channel).manage_messages!\r\n'
                    '`Only moderators and above are allowed to use the command [#clear]`',
                color=0x22a7f0)
            await message.channel.send(embed=embed)

client.run(paw_settings.TOKEN)