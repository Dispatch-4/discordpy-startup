from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

from discord.ext import tasks
import discord

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

bot.run(token)

import discord
client = discord.Client()

@client.event
async def on_ready():
    print("on_ready")
    print(discord.__version__)

client.run(Nzc0NzA3MjI0NzIzNDU2MDIx.X6bsUw.4V8BcjfC2LXD2fvG07Fzk6nn2f4)

from discord.ext import tasks
import discord

client = discord.Client()

channel_sent = None

@tasks.loop(seconds=10)
async def send_message_every_10sec():
    await channel_sent.send("10秒経ったよ")

    @client.event
async def on_ready():
    global channel_sent 
    channel_sent = client.get_channel(any_channel_id)
    send_message_every_10sec.start()

client.run("hogehogetoken")
