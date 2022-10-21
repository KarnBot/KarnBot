# bot.py
import os
import traceback

import disnake
from disnake.ext import commands

import cmd_decklist
import cmd_rolldice
import cmd_split
from config import test_guild, test_channel_id
from karnstatus import get_status

TOKEN = os.getenv("DISCORD_TOKEN")

activity = disnake.Activity(
    type=disnake.ActivityType.playing, name=get_status()
)
bot = commands.InteractionBot(test_guilds=[test_guild], activity=activity)


async def log_error(bot, command_name: str):
    test_channel = bot.get_channel(test_channel_id)
    tb = traceback.format_exc()
    await test_channel.send(
        f"```\nException on bot command: {command_name}\n{tb}\n```"
    )


@bot.event
async def on_ready():
    print(f"Bot connected as {bot.user}")


@bot.slash_command(
    name="split", description="Automatically splits people into tables"
)
async def split_groups(
    context: disnake.ApplicationCommandInteraction,
    players: str = commands.Param(
        name="players", description="Players to split between tables"
    ),
):
    cmd_name = "split"
    try:
        players = players.split(",")
        split_tables = cmd_split.split_group(players)
        result = []
        for (i, table) in enumerate(split_tables):
            result.append(f"Table {i+1}: {', '.join(table)}")
        table_string = "\n".join(result)
        await context.response.send_message(f"\n{table_string}")
    except Exception:
        await log_error(bot, cmd_name)


@bot.slash_command(name="roll", description="Randomly roll any list of dice")
async def roll_dice(
    context: disnake.ApplicationCommandInteraction,
    num_dice: int = commands.Param(
        name="number", description="Number of dice to roll"
    ),
    num_sides: int = commands.Param(
        name="sides", description="Number of sides on die to roll"
    ),
    bonus: int = commands.param(
        name="bonus", description="Bonus to add to the roll", default=0
    ),
):
    cmd_name = "roll"
    try:
        msg = cmd_rolldice.roll_dice(num_dice, num_sides, bonus=bonus)
        await context.response.send_message(f"\n{msg}")
    except Exception:
        await log_error(bot, cmd_name)


@bot.slash_command(
    name="decklist", description="Get links to registered decklists"
)
async def decklist(
    context: disnake.ApplicationCommandInteraction,
    player: cmd_decklist.Players = commands.Param(
        name="player", description="Player to get decks for"
    ),
    color_combination: cmd_decklist.ColorCombination = commands.Param(
        name="colors", description="Color combination (C = colorless)"
    ),
):
    cmd_name = "decklist"
    try:
        msg = cmd_decklist.get_deck(player, color_combination)
        await context.response.send_message(f"\n{msg}")
    except Exception:
        await log_error(bot, cmd_name)


bot.run(TOKEN)
