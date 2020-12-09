import os
from discord.ext import commands, tasks
from dotenv import load_dotenv
from discord.ext.commands import CommandNotFound
from discord.utils import get
import get_reddit
import keep_alive

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_DEBUG = os.getenv('DISCORD_GUILD_DEBUG')
CHANNEL_ID = os.getenv("DISCORD_CID")
bot = commands.Bot(command_prefix='/')


@bot.event
async def on_ready():
    print("service is ready")

@tasks.loop(seconds=900,reconnect=True)
async def check():
    await bot.wait_until_ready()
    channel = bot.get_channel(int(CHANNEL_ID))
    link = get_reddit.check_submissions()
    if link:
        alert =f"https://reddit.com{link}"
        await channel.send(alert)

@bot.command(name='test')
async def test_cmds(ctx):
    response = """waiting for waifus"""
    await ctx.send(response)

keep_alive.keep_alive()
check.start()
bot.run(TOKEN)


