# bot.py
import os
import string
import traceback

import disnake
from dotenv import load_dotenv
from disnake.ext import commands

import cmd_split
from karntypes import UserList

load_dotenv()
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


def safe_command(*cmdargs, **cmdkwargs):
    """Wrapper for bot.command, that will send errors to test_channel."""

    def outter_wrapper(wrapped):
        @bot.slash_command(*cmdargs, **cmdkwargs)
        async def wrapper(context, *args):
            try:
                return await wrapped(context, *args)
            except Exception:
                cmd_name = cmdkwargs["name"]
                tb = traceback.format_exc()
                await test_channel.send(
                    f"Exception on bot command: {cmd_name}\n{tb}"
                )

        return wrapper

    return outter_wrapper


@safe_command(name="split", help="Automatically splits people into tables")
async def split_groups(context, players: UserList):
    split_tables = cmd_split.split_group(players)
    result = []
    for (i, table) in enumerate(split_tables):
        result.append(f"Table {i+1}: {', '.join(table)}")
    table_string = "\n".join(result)
    await context.response.send_message(f"\n{table_string}")


bot.run(TOKEN)
