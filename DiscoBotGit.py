import discord
import asyncio
from discord.ext import commands
from discord.utils import get

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='!', intents=intents)

keywords = ['sutta is']

@client.event
async def on_message(message):
    if message.content.startswith('!mention me'):
        await message.channel.send(message.author.mention)
    for i in range(len(keywords)):
        if keywords[i] in message.content:
         for j in range(1):
                await message.channel.send("a dick!!!")
    await client.process_commands(message)

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, welcome to my Discord server!')

@client.command(help='pings phoenix')
async def pingpenis(ctx):
    pingfarhan = get(ctx.guild.members, name ='phoenix_')
    await ctx.send(f"{pingfarhan.mention}")

@client.command(help='pings av')
async def pingav(ctx):
    pingadhvi = get(ctx.guild.members, name ='av')
    await ctx.send(f"{pingadhvi.mention}")

@client.command(help='joins users vc')
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
@client.command(help='leaves current vc')
async def leave(ctx):
    await ctx.voice_client.disconnect()

client.run('token!')
