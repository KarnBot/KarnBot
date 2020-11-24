# bot.py
import os
import random

import discord
from dotenv import load_dotenv
from discord.ext.commands import Bot

import cmd_split

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = Bot(command_prefix="$")
test_channel = None


@bot.event
async def on_ready():
    print(f"Bot connected as {bot.user}")
    # Setup test channel
    global test_channel
    test_channel = bot.get_channel(432709546042195994)
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.playing, name="Karn's Temporal Sundering"
        )
    )


@bot.command(name="split", help="automatically splits people into games")
async def split_groups(context, *args):
    split_tables = cmd_split.split_group(args)
    result = []
    for (i, table) in enumerate(split_tables):
        result.append(f"Table {i+1}: {','.join(table)}")
    await context.channel.send("\n".join(result))


@bot.command(name="roll", help="randomly roll any list of dice")
async def roll_dice(context, *args):
    dices = cmd_split.split_group(args)
    result = 0
    for dice in enumerate(dices):
        intdice = int(dice)
        result = result + random.randint(1, intdice)
    await context.channel.send("You rolled a " + result)


bot.run(TOKEN)
