# Discord.py imports
import discord
import os
import dotenv

# Command imports
from discord.ext import commands
from fun_commands import client

dotenv.load_dotenv()
token = os.getenv("TOKEN")

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

# Command imports
from fun_commands import random_choice

@client.command(aliases=["h"])
async def hello(ctx):
    await ctx.send("Hello!")

@client.command(aliases=["c"])
async def cookie(ctx):
    await ctx.send("Have a cookie")

client.run(token)
