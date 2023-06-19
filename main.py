import discord
from discord.ext import commands
import os
token = os.environ['DISCORD_TOKEN']

# Adds prefix and intents
bot = commands.Bot(command_prefix="$", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot is Online") # bot status msg
    

bot.run(token)