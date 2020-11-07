from discord.ext import tasks
import os
import traceback
import discord

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

client = discord.Client()

channel_sent = 746047616046858322

@tasks.loop(minites=60)
async def send_message_every_60min():
    await channel_sent.send("!cnow")

@bot.event
async def on_ready():
    global channel_sent 
    channel_sent = client.get_channel(746047616046858322)
    send_message_every_60min.start()

bot.run(token)
