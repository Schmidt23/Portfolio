# bot.py
import os
import random
import discord
import COVID as cov
import heise as h
import nlp as nlp
import urban as ud
import movielib as ml
import ai
import fortyk
import weather
import datetime
import music
from discord.ext import commands
from dotenv import load_dotenv
from discord.ext.commands import CommandNotFound
from discord.utils import get
from keep_alive import keep_alive

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
GUILD_DEBUG = os.getenv('DISCORD_GUILD_DEBUG')


bot = commands.Bot(command_prefix='#')
queue = {}

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
    #ensure bot is not replying to itself
    if message.author == bot.user:
        return
    #reply on long messages
    if len(message.content) > 500 and message.author != bot.user:
        with open(f'pics/reactions/himark.jpg', 'rb') as f:
            pic = discord.File(f)
        await message.channel.send(file=pic)
    #reply if freitag is mentioned
    elif "freitag" in message.content.lower():
        response = friday
        rdm = random.choice(os.listdir("pics/benis"))
        with open(f'pics/benis/{rdm}', 'rb') as f:
            pic = discord.File(f)
        await message.channel.send(response, file=pic)
    #reply if weihnachten is mentioned
    elif "weihnachten" in message.content.lower():
        with open(f'pics/reactions/christmas.jpg', 'rb') as f:
            pic = discord.File(f)
        await message.channel.send(file=pic)
    #reply if 69 is mentionend (needs better filter atm)
    elif " 69 " in message.content and "<@" not in message.content:
        rdm = random.choice(os.listdir("pics/reactions/nice"))
        with open(f'pics/reactions/nice/{rdm}', 'rb') as f:
            pic = discord.File(f)
        await message.channel.send("69", file=pic)
    #reply if directly mentioned with a random compliment
    elif str(bot.user.id) in message.content:
        greeting = ['Hi', 'Hola', 'Huhu', 'Guten Tag', 'Servus']
        noun_list = ['dein Penis sieht', 'dein Geschlecht sieht', 'deine Nippel sehen', 'deine Hoden sehen', 'deine Vulva sieht', 'deine Brüste sehen']
        adj_list = ['schwülstig', 'nass', 'hart', 'pulsierend', 'stimuliert', 'leckbar']
        response = f'{random.choice(greeting)} {message.author.name}! Ich muss sagen, {random.choice(noun_list)} heute besonders {random.choice(adj_list)} aus.'
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
    with open(f'pics/reactions/HAL9000.jpg', 'rb') as f:
        pic = discord.File(f)
    response = f"I'm sorry {ctx.author.name}, I'm afraid i can't let you do that"
    await ctx.send(file=pic)
    await ctx.send(response, tts=True)

@bot.command(name='40k', help="find 30k Legion Info\t use: #40k <text>>")
async def ftyk(ctx, *, search):
    outlegion = fortyk.return_legion(search)
    for rlegion in outlegion:
        with open(f'pics/40k/{rlegion.pic}', 'rb') as f:
            pic = discord.File(f)
        response = (f"Number: {rlegion.number}\nName: {rlegion.name}\nPrimarch: {rlegion.primarch} "
                    f"\nBattlecry: {rlegion.motto}\nAllegiance: {rlegion.affiliation}")
        embed = discord.Embed(title="40k", description=response)
        await ctx.send(embed=embed, file=pic)

@bot.command(name='badbot')
async def bad(ctx):
    rdm = random.choice(os.listdir("pics/reactions/bad"))
    with open(f'pics/reactions/bad\{rdm}', 'rb') as f:
        pic = discord.File(f)
    await ctx.send(file=pic)

@bot.command(name='thesaurus',help="find synonym (english)\tuse: #thesaurus <text>")
async def syn(ctx, *, text):
    response = nlp.synonymize(text)
    await ctx.send(response)

@bot.command(name='translate', help="translate to german\tuse: #translate <text>",)
async def translate(ctx, *, text):
    response = nlp.trans_to_ger(text)
    await ctx.send(response)

@bot.command(name='urban', help="give top definition of urbandictionary\tuse: #urban chad")
async def urban(ctx, *, text):
    response = ud.get_def(text)
    await  ctx.send(response)

@bot.command(name='heise',help="top stories from heise.de")
async def hnews(ctx):
    response_total = h.feed_head()
    await ctx.send("Heise NEWS")
    await ctx.send(response_total)

@bot.command(name='sad')
async def sad(ctx):
    rdm = random.choice(os.listdir("pics/reactions/sad"))
    with open(f'pics/reactions/sad\{rdm}', 'rb') as f:
        pic = discord.File(f)
    await ctx.send(file=pic)

@bot.command(name='nelli')
async def nelli(ctx):
    with open(f'pics/nelli.jpg', 'rb') as f:
        pic = discord.File(f)
    await ctx.send(file=pic)

@bot.command(name='slowpat')
async def slowpat(ctx):
    with open(f'pics/reactions/slowpat.png', 'rb') as f:
        pic = discord.File(f)
    movie, link = ml.newest_movie()
    response = f"Hey Leute! Habt ihr schon von \"{movie}\" gehört? Soll echt gut sein. {link}"
    await ctx.send(response, file=pic)

@bot.command(name='speak', help="ai generated text")
async def speak(ctx):
    response = ai.textgen()
    await ctx.send(response)

@bot.command(name='train', help="start a training session for ai(pls don't)")
async def speak(ctx):
    response = "I'd rather not"#ai.textgen(train=True)
    await ctx.send(response)

@bot.command(name='goodbot')
async def good(ctx):
    with open(f'pics/reactions/happy.jpg', 'rb') as f:
        pic = discord.File(f)
        await ctx.send(file=pic)

@bot.command(name='corona')
async def corona(ctx):
    confirmed, dead, recovered, dt = cov.return_numbers()
    response = f"As of {dt}:\nCurrently confirmed cases: {confirmed:,}\nCurrent death toll: {dead:,}\nRecovered: {recovered:,}"

    with open(f'Coronachan/Coroanchan.png', 'rb') as f:
        pic = discord.File(f)
    embed = discord.Embed(title="News from Coronachan", description=response, color=0x00ff00)
    await ctx.send(embed=embed, file=pic)

@bot.command(name='corona_country',help="corona data for specific country\tuse: #corona_country <text>")
async def cc(ctx, *, country):
    nation, cases, new_cases, deaths, new_deaths, recovered = cov.by_country(country)
    response = (f'Currently confirmed cases: {cases:,} (+{new_cases:,})\nCurrent death toll: {deaths:,}(+{new_deaths})'
               f'\nRecovered: {recovered:,}')

    with open(f'Coronachan/Coroanchan.png', 'rb') as f:
        pic = discord.File(f)
    embed = discord.Embed(title=f"News from Coronachan for {nation}", description=response, color=0x00ff00)
    await ctx.send(embed=embed, file=pic)

@bot.command(name='hannscript',help="mix up previous message")
async def hann(ctx):
    now = datetime.datetime.now()
    chan = await ctx.message.channel.history(before=now, limit=2).flatten()
    #text = (chan[-1].content).split(" ")
    #print(text)
    #random.shuffle(text)
    response = nlp.hann_sent(chan[-1].content)
    await ctx.send(response)

@bot.command(name='embed', help="debugging embed function")
async def emb(ctx):
    with open(f'pics/reactions/HAL9000.jpg', 'rb') as f:
        pic = discord.File(f)
        response = "test"
        embed = discord.Embed(title= "TestEmbed", description="des", color=0x00ff00)
        #embed.add_field(name="picfield", value=pic, inline=False)
        embed.add_field(name="Textfield", value=response, inline=True)
        #await ctx.send(embed=embed, file=pic)
        await ctx.send(file=pic, embed=embed)

@bot.command(name='weather', help="info weather\tuse: #weather <city>")
async def openweather(ctx, *, city):
    icon, temp, temp_min, temp_max = weather.give_weather(city)
    response = f"{icon}\nTemp:\t{temp:.1f}°C\n{temp_min:.1f}°C-{temp_max:.1f}°C"
    await ctx.send(response)


@bot.command(name="join")
async def join(ctx):
    author = ctx.message.author
    channel = author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
    voice = get(bot.voice_clients, guild = ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

@bot.command(name="leave")
async def leave(ctx):
    voice = get(bot.voice_clients, guild = ctx.guild)
    await voice.disconnect()

@bot.command(name='play')
async def play(ctx, url):

    def check_q(song_file):
        print(f"removing {song_file}")
        os.remove(f"{song_file}")
        try:
            song = os.listdir("music")[0]
            print(f"choosing {song}")
            if not voice_client.is_playing():
                player = voice_client.play(discord.FFmpegPCMAudio(f"./music/{song}"), after=lambda e: check_q(f'./music/{song}'))
        except Exception as e:
            print(e)

    guild = ctx.guild
    voice_client = guild.voice_client
    song = music.dl_file(url)
    if not voice_client.is_playing():
        player = voice_client.play(discord.FFmpegPCMAudio(song), after=lambda e: check_q(song))

@bot.command(name="queue")
async def queueing(ctx, url):
    song = music.dl_file(url)
    response = f"Adding {song} to queue"

@bot.command(name="pause")
async def pause(ctx):
    guild = ctx.guild
    voice_client = guild.voice_client
    if voice_client.is_playing():
        voice_client.pause()

@bot.command(name="resume")
async def resume(ctx):
    guild = ctx.guild
    voice_client = guild.voice_client
    if not voice_client.is_playing():
        voice_client.resume()


@bot.command(name="stop")
async def stop(ctx):
    guild = ctx.guild
    voice_client = guild.voice_client
    if voice_client.is_playing():
        voice_client.stop()


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        rdm = random.choice(os.listdir("pics/reactions/error"))
        with open(f'pics/reactions/error/{rdm}', 'rb') as f:
            pic = discord.File(f)
            await ctx.send("U wot m8!?")
            await ctx.send(file=pic)
    else:
        print(error)

keep_alive()
bot.run(TOKEN)