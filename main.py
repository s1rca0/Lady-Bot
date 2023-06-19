import discord
from discord.ext import commands
import os
token = os.environ['DISCORD_TOKEN']

bot = commands.Bot(command_prefix="$", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot is Online")
    

bot.run(token)