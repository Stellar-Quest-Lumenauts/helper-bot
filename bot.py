import discord
from discord_slash import SlashCommand # Importing the newly installed library.
import os

client = discord.Client(intents=discord.Intents.default())
slash = SlashCommand(client, sync_commands=True) # Declares slash commands through the client.
guild_ids = [703325111209427015, 763798356484161566] # Test Server, Stellar Quest Server

@client.event
async def on_ready():
    print("Ready!")

@slash.slash(name="ping", guild_ids=guild_ids)
async def _ping(ctx): # Defines a new "context" (ctx) command called "ping."
    await ctx.send(f"Pong! ({client.latency*1000}ms)")

client.run(os.environ.get("BOT_TOKEN"))
