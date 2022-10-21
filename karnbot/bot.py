# bot.py
import os

import disnake
from disnake.ext import commands

import cmd_split
import cmd_rolldice
from karntypes import UserList
from testchannel import TestChannel
from config import test_guild

TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.InteractionBot(test_guilds=[test_guild])
test_channel = TestChannel()


@bot.event
async def on_ready():
    print(f"Bot connected as {bot.user}")
    test_channel.configure()

    await bot.change_presence(
        activity=disnake.Activity(
            type=disnake.ActivityType.playing, name="Karn's Temporal Sundering"
        )
    )


@bot.slash_command(
    name="split", description="Automatically splits people into tables"
)
async def split_groups(context, players: UserList):
    try:
        players = players.split(",")
        split_tables = cmd_split.split_group(players)
        result = []
        for (i, table) in enumerate(split_tables):
            result.append(f"Table {i+1}: {', '.join(table)}")
        table_string = "\n".join(result)
        await context.response.send_message(f"\n{table_string}")
    except Exception:
        cmd_name = "split"
        test_channel.log_error(cmd_name)


@bot.slash_command(name="roll", description="Randomly roll any list of dice")
async def roll_dice(context, num_dice: int, num_sides: int, bonus: int = 0):
    msg = cmd_rolldice.roll_dice(num_dice, num_sides, bonus=bonus)
    await context.response.send_message(f"\n{msg}")


bot.run(TOKEN)
