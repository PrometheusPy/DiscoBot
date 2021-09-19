import discord
import asyncio
from discord.ext import commands
from discord.utils import get

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix='!', intents=intents)

keywords = ['hello disco', 'Hello Disco', 'hello Disco', 'Hello disco', 'HELLO DISCO', 'HELLO disco', 'hello DISCO']

@client.event
async def on_message(message):
    if message.content.startswith('!mention me'):
        await message.channel.send(message.author.mention)
    for i in range(len(keywords)):
        if keywords[i] in message.content:
         for j in range(1):
                await message.channel.send("Hello! I'm disco bot!")
    await client.process_commands(message)

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, welcome to my Discord server!')

@client.command()
async def pingsutta(ctx):
    Prometheus = get(ctx.guild.members, name ='Sutta')
    await ctx.send(f"{Prometheus.mention}")

@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

client.run('token!')
