import discord
from discord.ext import commands

import os
import config

Classname = 'Reaction'
EL = 'Extention_Loader: {} has been loaded'.format(Classname)

client = discord.Client

class Reaction(commands.Cog):

    def __init__(self, client):
        self.client = client

    # Event"
    @commands.Cog.listener()
    async def on_ready(self):
        print(EL)

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        channel = reaction.message.channel
        if reaction.emoji == config.info_reaction1:
            if not user.bot:
                await user.send('MY DM1')
        if reaction.emoji == config.info_reaction2:
            if not user.bot:
                await user.send('MY DM2')
        if reaction.emoji == config.info_reaction3:
            if not user.bot:
                await user.send('MY DM3')
        print(channel, '{} has added {} to the message: {}'.format(user.name, reaction.emoji, reaction.message.id))


def setup(client):
    client.add_cog(Reaction(client))
