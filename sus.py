# shit python bot

import discord
from discord.ext import commands
from discord.utils import get

token = 'ODc3OTczMzY0Nzk3NDgxMDEx.YR6aag.5IhyqL81tcIYW_c8VkSpOpgo8Ek'
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.channel.name == "fard-chain":
        if str(message.content) != 'fard' and str(message.content) != 'Fard':
            if message.content != "":
                await client.get_channel(878255368025812993).send(message.content)
            await message.delete()

client.run(token)

#     if message.content.startswith('give mod pls334245'):
#         member = ctx.message.author
#         role = get(member.server.roles, name="Test")
#         await bot.add_roles(member, role)
