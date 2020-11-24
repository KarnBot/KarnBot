# bot.py
import os

import discord
from dotenv import load_dotenv
from discord.ext.commands import Bot

from . import split

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = Bot(command_prefix="$")
test_channel = None


@bot.event
async def on_ready():
    print(f"Bot connected as {bot.user}")
    # Setup test channel
    test_channel = bot.get_channel(780611534833188905)
    await bot.change_presence(
        activity=discord.Activity(
            type=Discord.ActivityType.playing, name="Karn's Temporal Sundering"
        )
    )


@bot.command(name="split", help="automatically splits people into games")
async def split_groups(context):
    await test_channel.send(f"Split command registered")
    split.split_group()


bot.run(TOKEN)
