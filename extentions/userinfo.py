import discord
from discord.ext import commands

import time

Classname = 'Userinfo'
EL = 'Extention_Loader: {} has been loaded'.format(Classname)


class Userinfo(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Event
    @commands.Cog.listener()
    async def on_ready(self):
        print(EL)

    # Commands
    @commands.command()
    async def userinfo(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        roles = [role for role in member.roles]

        print(f'UserInfoCmd has been executed by {ctx.author} in channel #{ctx.channel}, about {member}')

        await ctx.channel.purge(limit=1)

        embed = discord.Embed(colour=discord.Colour.dark_purple(), timestamp=ctx.message.created_at)

        embed.set_author(name=f'User Info - {member}')
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)

        embed.add_field(name='ID:', value=member.id)
        embed.add_field(name='Display name:', value=member.display_name)

        embed.add_field(name='Created at:', value=member.created_at.strftime('%d/%m/%Y, %H:%M:%S'), inline=True)
        embed.add_field(name='Joined at:', value=member.joined_at.strftime('%d/%m/%Y, %H:%M:%S'), inline=True)

        embed.add_field(name=f'Role/s:({len(roles)})', value=' '.join([role.mention for role in roles]))

        await ctx.send(embed=embed, delete_after=60)


def setup(client):
    client.add_cog(Userinfo(client))
