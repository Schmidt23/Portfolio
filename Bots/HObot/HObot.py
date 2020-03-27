# bot.py
import os
import random
import discord
import COVID as cov
import heise as h
import nlp as nlp
import urban as ud
import movielib as ml
import fortyk
import datetime
from discord.ext import commands
from dotenv import load_dotenv
from discord.ext.commands import CommandNotFound

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
GUILD_DEBUG = os.getenv('DISCORD_GUILD_DEBUG')


bot = commands.Bot(command_prefix='#')

@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{bot.user.name} has connected to Discord on the following guild! \n'
        f'{guild.name} (id: {guild.id})'
    )
    members = '\n -'.join([member.name for member in guild.members])
    print(f'Guild members: \n -{members}')


@bot.event
async def on_member_join(self, member):
    print(f'{member} joined')
    ment = member.mention
    await self.client.get_channel("692784589156122634").send(f"{ment} has joined the server.")

@bot.event
async def on_message(message):
    friday = "Benis xD"
    if message.author == bot.user:
        return
    if len(message.content) > 500 and message.author != bot.user:
        with open(f'pics\\reactions\himark.jpg', 'rb') as f:
            pic = discord.File(f)
            await message.channel.send(file=pic)

    elif "freitag" in message.content.lower():
        response = friday
        rdm = random.choice(os.listdir("pics\\benis"))
        with open(f'pics\\benis\{rdm}', 'rb') as f:
            pic = discord.File(f)
            await message.channel.send(response, file=pic)

    elif "weihnachten" in message.content.lower():
        with open(f'pics\\reactions\christmas.jpg', 'rb') as f:
            pic = discord.File(f)
            await message.channel.send(file=pic)
    elif "69 " in message.content.lower():
        print(message.content.lower())
        rdm = random.choice(os.listdir("pics\\reactions\\nice"))
        with open(f'pics\\reactions\\nice\\{rdm}', 'rb') as f:
            pic = discord.File(f)
            await message.channel.send(file=pic)
    elif str(bot.user.id) in message.content:
        noun_list = ['dein Penis sieht', 'dein Geschlecht sieht', 'deine Nippel sehen', 'deine Hoden sehen', 'deine Vulva sieht', 'deine Brüste sehen']
        adj_list = ['schwülstig', 'nass', 'hart', 'pulsierend', 'stimuliert', 'leckbar']
        response = f'Hi {message.author.name}! Ich muss sagen, {random.choice(noun_list)} heute besonders {random.choice(adj_list)} aus.'
        await message.channel.send(response)
    else:
        pass
    await bot.process_commands(message)

@bot.command(name='test')
async def test_cmds(ctx):
    response = """\tToll the Great Bell Once!\n
Pull the Lever forward to engage the Piston and Pump...\n
Toll the Great Bell Twice!\n
With push of Button fire the Engine\n
And spark Turbine into life...\n
Toll the Great Bell Thrice!\n
Sing Praise to the God of All Machines"""
    await ctx.send(response)

@bot.command(name='openpodbaydoors')
async def hal(ctx):
    with open(f'pics\\reactions\\HAL9000.jpg', 'rb') as f:
        pic = discord.File(f)
        response = f"I'm sorry {ctx.author.name}, I'm afraid i can't let you do that"
        await ctx.send(file=pic)
        await ctx.send(response, tts=True)

@bot.command(name='40k')
async def ftyk(ctx, *, search):
    rlegion = fortyk.return_legion(search)
    with open(f'pics\\40k\\{rlegion.pic}', 'rb') as f:
        pic = discord.File(f)
        response = (f"Number: {rlegion.number}\nName: {rlegion.name}\nPrimarch: {rlegion.primarch} "
                    f"\nBattlecry: {rlegion.motto}\nAllegiance: {rlegion.affiliation}")
        await ctx.send(file=pic)
        await ctx.send(response)

@bot.command(name='badbot')
async def bad(ctx):
    rdm = random.choice(os.listdir("pics\\reactions\\bad"))
    with open(f'pics\\reactions\\bad\{rdm}', 'rb') as f:
        pic = discord.File(f)
        await ctx.send(file=pic)

@bot.command(name='thesaurus')
async def syn(ctx, *, text):
    response = nlp.synonymize(text)
    await ctx.send(response)

@bot.command(name='translate')
async def translate(ctx, *, text):
    response = nlp.trans_to_ger(text)
    await ctx.send(response)

@bot.command(name='urban')
async def urban(ctx, *, text):
    response = ud.get_def(text)
    await  ctx.send(response)

@bot.command(name='heise')
async def hnews(ctx):
    response_total = h.feed_head()
    await ctx.send("Heise NEWS")
    await ctx.send(response_total)

@bot.command(name='sad')
async def sad(ctx):
    rdm = random.choice(os.listdir("pics\\reactions\\sad"))
    with open(f'pics\\reactions\\sad\{rdm}', 'rb') as f:
        pic = discord.File(f)
        await ctx.send(file=pic)

@bot.command(name='nelli')
async def nelli(ctx):
    with open(f'pics\\nelli.jpg', 'rb') as f:
        pic = discord.File(f)
        await ctx.send(file=pic)

@bot.command(name='slowpat')
async def slowpat(ctx):
    with open(f'pics\\reactions\slowpat.png', 'rb') as f:
        movie, link = ml.newest_movie()
        response = f"Hey Leute! Habt ihr schon von \"{movie}\" gehört? Soll echt gut sein. {link}"
        pic = discord.File(f)
        await ctx.send(response, file=pic)

@bot.command(name='speak')
async def speak(ctx):
    await ctx.send("01000100 01100101 01101001 01101110 01100101 00100000 01001101 01110101 01110100 01110100 01100101 01110010 00100000 01110011 01110100 01101001 01101110 01101011 01110100 00101110", tts=True)

@bot.command(name='goodbot')
async def good(ctx):
    with open(f'pics\\reactions\happy.jpg', 'rb') as f:
        pic = discord.File(f)
        await ctx.send(file=pic)

@bot.command(name='corona')
async def corona(ctx):
    confirmed = cov.return_numbers()[0]
    dead = int(cov.return_numbers()[1])
    recovered = int(cov.return_numbers()[2])
    dt = cov.return_numbers()[3]
    response = f"As of {dt}:\nCurrently confirmed cases: {confirmed:,}\nCurrent death toll: {dead:,}\nRecovered: {recovered:,}"
    with open(f'Coronachan\Coroanchan.png', 'rb') as f:
        pic = discord.File(f)
        await ctx.send(file=pic)
        await ctx.send(response)

@bot.command(name='hannscript')
async def hann(ctx):
    now = datetime.datetime.now()
    chan = await ctx.message.channel.history(before=now, limit=2).flatten()
    #text = (chan[-1].content).split(" ")
    #print(text)
    #random.shuffle(text)
    response = nlp.hann_sent(chan[-1].content)
    await ctx.send(response)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        rdm = random.choice(os.listdir("pics\\reactions\\error"))
        with open(f'pics\\reactions\\error\\{rdm}', 'rb') as f:
            pic = discord.File(f)
            await ctx.send("U wot m8!?")
            await ctx.send(file=pic)
    else:
        print(error)

bot.run(TOKEN)