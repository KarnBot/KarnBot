# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    channel = client.get_channel(780611534833188905)
    e = discord.Embed(title='Bot Deploy test')
    await channel.send('Hello', embed=e)

client.run(TOKEN)
