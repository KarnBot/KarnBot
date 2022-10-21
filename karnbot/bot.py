# bot.py
import os
import string
import traceback

import disnake
from disnake.ext import commands

import cmd_split
from karntypes import UserList

TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.InteractionBot(test_guilds=[780585690446561340])
test_channel = None


@bot.event
async def on_ready():
    print(f"Bot connected as {bot.user}")
    # Setup test channel
    global test_channel
    test_channel = bot.get_channel(780611534833188905)
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
        tb = traceback.format_exc()
        await test_channel.send(f"Exception on bot command: {cmd_name}\n{tb}")


bot.run(TOKEN)
