import discord
from discord.ext import commands

import json


class Bot(commands.Cog):

    def __init__(self, client) -> None:
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(status=discord.Status.online, activity=discord.Game('>help'))
        print(f"{self.client.user} successfuly started.")
        await self.tree.sync(self.client)

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        with open('data/data.json', 'r') as f:
            data = json.load(f)

        data[str(guild.id)] = {"welcomeChannel": "", "logsChannel": ""}

        with open('data/data.json', 'w') as f:
            json.dump(data, f, indent=2)
            f.close()

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):
        new_data = {}

        with open('data/data.json', 'r') as f:
            data = json.load()

        for entry in data:
            if entry != str(guild.id):
                new_data[str(entry)] = {"welcomeChannel": f"{data[str(entry)]['welcomeChannel']}",
                                        "logsChannel": f"{data[str(entry)]['logsChannel']}"}

                with open('data/data.json', 'w') as f:
                    json.dump(data, f, indent=2)
                    f.close()
                print(new_data)
            else:
                pass


async def setup(client):
    await client.add_cog(Bot(client))
