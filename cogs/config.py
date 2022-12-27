import discord
from discord.ext import commands
from discord import app_commands

import json


class Config(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client

    @commands.group(name='config', invoke_without_command=True)
    async def config(self, ctx: commands.Context):
        await ctx.send("Embed coming here soon...")

    @config.command(name='welcomeChannel', invoke_without_command=True)
    async def setWelcomeChannel_cmd(self, ctx: commands.Context, textChannel: discord.TextChannel):
        if textChannel is None:
            textChannelID = str(ctx.channel.id)
        else:
            textChannelID = str(textChannel.id)

        with open('data/data.json', 'r') as f:
            data = json.load(f)

        data[str(ctx.guild.id)]['welcomeChannel'] = textChannelID

        with open('data/data.json', 'w') as f:
            json.dump(data, f, indent=2)

        try:
            await textChannel.send("This channel has been setup as the welcome channel, each time a new member joins it will be announced in this channel")
        except AttributeError:
            await ctx.send("problem ?")

    @config.command(name="logsChannel", invoke_without_command=True)
    async def setLogsChannel_cmd(self, ctx: commands.Context, textChannel: discord.TextChannel):
        if textChannel is None:
            textChannelID = str(ctx.channel.id)
        else:
            textChannelID = str(textChannel.id)

        with open('data/data.json', 'r') as f:
            data = json.load(f)

        data[str(ctx.guild.id)]['logsChannel'] = textChannelID

        with open('data/data.json', 'w') as f:
            json.dump(data, f, indent=2)

        try:
            await textChannel.send("This is now the new logs channel.")
        except AttributeError:
            await ctx.send("problem ?")


async def setup(client):
    await client.add_cog(Config(client))
