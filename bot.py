import discord
from discord.ext import commands

DISCORD_TOKEN = ''

BOT_COMMAND_PREFIX = '!'

client = commands.Bot(command_prefix = BOT_COMMAND_PREFIX)

@client.event
async def on_ready():
    print('Bot is online!')

client.run(DISCORD_TOKEN)
