import discord
from discord.commands import Option
import random
import time

bot = discord.Bot()

@bot.event
async def on_ready():
    print('Ready!')

@bot.event
async def on_message(ctx):
    if ctx.channel.id == 867074509063323728:
        if ctx.author.id == 877973364797481011:
            return
        if (ctx.content != 'Fard' and ctx.content != 'fard'):
            await ctx.delete()
            await bot.get_channel(878255368025812993).send(f'<@{ctx.author.id}> said: "{ctx.content}" in #fard-chain')
@bot.event
async def on_message_edit(then, now):
    if now.channel.id == 867074509063323728:
        if now.author.id == 877973364797481011:
            return
        if (now.content != 'Fard' and now.content != 'fard'):
            await now.delete()
            await bot.get_channel(878255368025812993).send(f'<@{now.author.id}> edited chat from: "{then.content}" \n to: "{now.content}" in #fard-chain')

@bot.slash_command(name='ping', description="give ping of bot", guild_ids=[866820748366053396])
async def ping(ctx):
    before = time.monotonic()
    message = await ctx.send("ping is:")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"ping is:  `{int(ping)}ms`")

@bot.slash_command(name='rng',description="generate a random number", guild_ids=[866820748366053396])
async def rng(ctx,min:Option(int,'minimum number default=0',required=False,default=0) ,max:Option(int,'maximum number default=10',required=False,default=10)):
    await ctx.send(f'num: `{random.randrange(min,max)}`')
  
bot.run(open('token').read())
