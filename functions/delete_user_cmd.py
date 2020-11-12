import discord
client = discord.Client()

def is_not_pinned(mess):
    return not mess.pinned

@client.event
async def  on_message(delete_user_cmd):
    await delete_user_cmd.channel.purge(limit=1, check = is_not_pinned)
    print('delete_user_cmd')