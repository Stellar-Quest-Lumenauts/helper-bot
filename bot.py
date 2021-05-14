import discord
import discord_slash
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_permission
from discord_slash.model import SlashCommandPermissionType
import os

client = discord.Client(intents=discord.Intents.default())
slash = SlashCommand(client, sync_commands=True) # Declares slash commands through the client.
guild_ids = [703325111209427015, 763798356484161566] # Test Server, Stellar Quest Server

quest_roles = [
	create_permission(766768688342499390, SlashCommandPermissionType.ROLE, True), # Lumenaut
	create_permission(763798356484161566, SlashCommandPermissionType.ROLE, False),  # Everyone
]

@client.event
async def on_ready():
    print("Ready!")

@slash.slash(name="ping", guild_ids=guild_ids)
@slash.permission(guild_id=763798356484161566,permissions=quest_roles)
async def _ping(ctx): # Defines a new "context" (ctx) command called "ping."
    await ctx.send(f"Pong! ({client.latency*1000}ms)")

client.run(os.environ.get("BOT_TOKEN"))
