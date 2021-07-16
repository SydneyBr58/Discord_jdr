import discord
from discord.ext import commands
import youtube_dl

import asyncio
import time

bot = commands.Bot(command_prefix=".")

@bot.event
async def on_ready():
    print("Ready to go!")
    

@bot.event
async def on_message(message):
    """ Reply to user message in chat if it matches a condition """
    if message.author == bot.user:
        return
    channel = message.channel
    word = "test"
    if word.lower() == message.content.lower():
        response = "Successful test, GG"
        await channel.send(response)
    await bot.process_commands(message)


@bot.command()
async def move2(ctx, destination):
    """ Move the sender of the message to the specified voice channel """
    channels = {chn.name: chn for chn in ctx.guild.voice_channels}
    if destination in channels.keys():
        member = ctx.author
        await member.move_to(channels[destination])
    else:
        await ctx.send(f"Incorrect syntax. Use .move2 channel_name\nAvailable voice channels: {channels.keys()}")


@bot.command()
async def rick(ctx):
    """ Rick rolled function """
    voice_channel = ctx.author.voice.channel
    if voice_channel != None:
        voice_client = ctx.voice_client
        filepath = "C:\\Users\\SYDNEY\\discord_bot\\Rick_rolled.mp3"
        source = discord.FFmpegPCMAudio(executable="C:/ffmpeg/bin/ffmpeg.exe",\
         source=filepath)
        source = discord.PCMVolumeTransformer(source, volume=0.1)
        voice_client.play(source)
        time.sleep(30)
        voice_client.stop()
    else:
        await ctx.send("The bot and you must be in a voice channel first")


@bot.command()
async def volume(ctx, vol):
    if ctx.voice_client:
        if ctx.voice_client.is_playing():
            ctx.voice_client.source = discord.PCMVolumeTransformer(ctx.voice_client.source, volume=vol/100)
        else:
            ctx.send("The bot is not playing now.")
    else:
        ctx.send("The bot is not in a voice channel.")


@bot.command()
async def join(ctx):
    """ Makes the bot join the sender's voice channel """
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send("Volume bot joined the channel")
    else:
        await ctx.send("You must be in a voice channel first.")


@bot.command()
async def leave(ctx):
    """ Makes the bot leave its current voice channel """
    if ctx.voice_client:
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Volume bot left the channel")
    else:
        await ctx.send("The bot is not in a voice channel")


@bot.command()
async def stream(ctx, *, url):
    """Streams from a url (same as yt, but doesn't predownload)"""
    if ctx.voice_client:
        player = await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)
        ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
        await ctx.send('Now playing: {}'.format(player.title))
    else:
        await ctx.send("The bot and you must be in a voice channel first.")


file = open(r"C:\Users\SYDNEY\discord_bot\discord_api_token.txt")
token = file.read()
bot.run(token)