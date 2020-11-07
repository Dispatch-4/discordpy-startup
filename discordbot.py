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

@client.event
async def on_ready():
    while True:
        if time.strftime('%H:%M:%S',time.localtime())=='06:05:00':
            channel = client.get_channel('748898203918663780')
            await client.send_message(channel, '06:05:00')
            sleep(5)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(token)
