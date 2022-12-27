import discord
from discord import app_commands
from discord.ext import commands

import os

import asyncio

with open("keys/TOKEN.cfg") as f:
    TOKEN = f.read()

client = commands.Bot(command_prefix='>', intents=discord.Intents.all())


async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await client.load_extension(f'cogs.{filename[:-3]}')
            print(f"Loaded file: {filename}")


async def main():
    await load()
    await client.start(token=TOKEN)

asyncio.run(main())
