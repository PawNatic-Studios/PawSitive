import discord
from discord.ext import commands

Classname = 'Clear'
EL = 'Extention_Loader: {} has been loaded'.format(Classname)

class Clear(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Event
    @commands.Cog.listener()
    async def on_ready(self):
        print(EL)

    # Commands
    # clear + amount/dm
    @commands.command(pass_context=True)
    async def clear(self, ctx, args=None):
        print(f'Clear cmd has been executed by {ctx.author} in channel #{ctx.channel}')

        def mess_is_not_pinned(mess):
            return not mess.pinned

        if args is None:
            await ctx.channel.purge(check=mess_is_not_pinned)
            embed = discord.Embed(title='Moderation',
                                  description=f'All messages of #{ctx.channel} have been deleted by {ctx.author}',
                                  color=0x3A00FF)
            await ctx.send(embed=embed, delete_after=10)

        elif args.isdigit():
            count = int(args) + 1
            deleted = await ctx.channel.purge(limit=count, check=mess_is_not_pinned)
            embed = discord.Embed(title='Moderation',
                                  description='**{}** messages have been deleted in #'.format(
                                      len(deleted) - 1) + f'{ctx.channel} by {ctx.author}',
                                  color=0x3A00FF)
            await ctx.send(embed=embed, delete_after=10)

        #elif args == 'dm':
        #    user = ctx.author
        #    async for message in user.history(limit=100):
        #        if message.author == self.client.user:
        #            await message.delete()

        else:
            await ctx.channel.purge(limit=1)
            embed = discord.Embed(title='Whoops',
                                  description=f'+clear ~**{args}** is not a number!',
                                  color=0x3A00FF)
            await ctx.send(embed=embed, delete_after=10)


def setup(client):
    client.add_cog(Clear(client))
