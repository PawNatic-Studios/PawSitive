import discord
from discord.ext import commands

import os
import config

Classname = 'UserinfoReaction'
EL = 'Extention_Loader: {} has been loaded'.format(Classname)


class UserinfoReaction(commands.Cog):

    # Event"
    @commands.Cog.listener()
    async def on_ready(self):
        print(EL)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        bot = payload.member.bot

        react1 = config.info_reaction1
        react2 = config.info_reaction2
        react3 = config.info_reaction3

        if bot is not True:

            #userinfo_reaction_1
            if payload.emoji.name == react1:
                await payload.member.send('PawSitive')
            elif react1.startswith(':'):
                c_emoji1 = react1[1:-19]
                if payload.emoji.name == c_emoji1:
                    await payload.member.send('PawSitive')

            #userinfo_reaction_2
            if payload.emoji.name == react2:
                await payload.member.send('User description')
            elif react2.startswith(':'):
                c_emoji2 = react2[1:-19]
                if payload.emoji.name == c_emoji2:
                    await payload.member.send('PawSitive')

            #userinfo_reaction_3
            if payload.emoji.name == react3:
                await payload.member.send('Love')
            elif react3.startswith(':'):
                c_emoji3 = react3[1:-19]
                if payload.emoji.name == c_emoji3 == react3[1:-19]:
                    await payload.member.send('Love')

        #if config.info_reaction1.startswith(':'):
        #    custom1 = config.info_reaction1[1:-19]
        #    if payload.emoji.name == custom1:
        #        if bot is not True:
        #            await payload.member.send('PawSitive')

def setup(client):
    client.add_cog(UserinfoReaction(client))
