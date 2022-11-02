from interactions import Client, Intents, Permission, PermissionType
import os
import sys
from messages import commands

BOT_TOKEN = os.environ.get("HELPER_BOT_TOKEN")

if BOT_TOKEN is None:
    print("BOT TOKEN IS MISSING")
    sys.exit(1)

client = Client(token=BOT_TOKEN)
guild_ids = [703325111209427015, 763798356484161566] # Test Server, Stellar Quest Server

quest_roles = [
	Permission(id=766768688342499390, type=PermissionType.ROLE, permission=True), # Lumenaut
	Permission(id=763798356484161566, type=PermissionType.ROLE, permission=False)  # Everyone
]

@client.event
async def on_ready():
    print("Ready!")

@client.command(name="ping", description="Ping!", scope=guild_ids)
async def _ping(ctx): # Defines a new "context" (ctx) command called "ping."
    await ctx.send(f"Pong! ({client.latency*1000}ms)")

for command in commands:
    command = command.lower()
    function_name = f"_{command}"
    @client.command(name=command, scope=guild_ids,
				 description=f"{commands[command.upper()][:97]}...")
    async def function_name(ctx):
        await ctx.send(f"{commands[command.upper()]}")

client.start()
