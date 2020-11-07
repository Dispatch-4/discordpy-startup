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

@client.event
async def on_ready():
    print("on_ready")
    print(discord.__version__)

from discord.ext import tasks
import discord

client = discord.Client()

channel_sent = 746047616046858322

@tasks.loop(minites=60)
async def send_message_every_60min():
    await channel_sent.send("!cnow")

    @client.event
async def on_ready():
    global channel_sent 
    channel_sent = client.get_channel(746047616046858322)
    send_message_every_60min.start()

client.run(token)
