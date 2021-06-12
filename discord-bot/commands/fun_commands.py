# Discord.py imports
import discord
import os
import dotenv

# Command imports
from discord.ext import commands
import random

client = commands.Bot(command_prefix="!")

@client.command(aliases=["random"])
async def random_choice(ctx):
    variables = ctx.message.content.split(' ')
    num = random.choice(variables[1:])
    await ctx.send(num)



