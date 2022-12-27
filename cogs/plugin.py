from discord.ext import commands


class Plugin(commands.Cog):
    def __init__(self, client) -> None:
        self.client = client
        self.owner = 546673415650541596

    @commands.group(name='plugin', invoke_without_command=True)
    async def plugin(self, ctx: commands.Context):
        if ctx.author.id == self.owner:
            await ctx.send("Please specify... -> 'load', 'unload' or 'reload'.")
        else:
            await ctx.send("You are not allowed to use this command.")

    @plugin.command(name='load', invoke_without_command=True)
    async def load_cmd(self, ctx: commands.Context, extension: str):
        if ctx.author.id == self.owner:
            try:
                await self.client.load_extension(f'cogs.{extension[:-3]}')
                await ctx.send(f"The extension: {extension} has been loaded.")
                print(f"Extension: {extension} has been loaded.")
            except:
                print(f"Extension: {extension} doesn't exist")
        else:
            await ctx.send("You are not allowed to use this command.")

    @plugin.command(name='unload', invoke_without_command=True)
    async def unload_cmd(self, ctx: commands.Context, extension: str):
        if ctx.author.id == self.owner:
            try:
                await self.client.unload_extension(f'cogs.{extension[:-3]}')
                await ctx.send(f"The extension: {extension} has been unloaded.")
                print(f"Extension: {extension} has been unloaded.")
            except:
                print(f"Extension: {extension} doesn't exist")
        else:
            await ctx.send("You are not allowed to use this command.")

    @plugin.command(name='reload', invoke_without_command=True)
    async def reload_cmd(self, ctx: commands.Context, extension: str):
        if ctx.author.id == self.owner:
            try:
                await self.client.unload_extension(f'cogs.{extension[:-3]}')
                await self.client.load_extension(f'cogs.{extension[:-3]}')
                await ctx.send(f"The extension: {extension} has been reloaded.")
                print(f"Extension: {extension} has been reloaded.")
            except:
                print(f"Extension: {extension} doesn't exist")
        else:
            await ctx.send("You are not allowed to use this command.")


async def setup(client):
    await client.add_cog(Plugin(client))
