# bot.py
import os
import traceback

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
    test_channel = bot.get_channel(780611534833188905)
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.playing, name="Karn's Temporal Sundering"
        )
    )


def safe_command(*cmdargs, **cmdkwargs):
    """Wrapper for bot.command, that will send errors to test_channel."""

    def outter_wrapper(wrapped):
        @bot.command(*cmdargs, **cmdkwargs)
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
async def split_groups(context, *args):
    split_tables = cmd_split.split_group(list(args))
    result = []
    for (i, table) in enumerate(split_tables):
        result.append(f"Table {i+1}: {', '.join(table)}")
    table_string = "\n".join(result)
    await context.channel.send(f"\n{table_string}")


bot.run(TOKEN)
