#!/usr/bin/python
import praw
import pdb
import re
import os
import discord
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import time
import json

secrets_file=open("/mnt/e/kurwa/руст/polanbot/secrets.json")
secrets=secrets_file.read()
secret=json.loads(secrets)
embedcolor=0x64C13F
bot = commands.Bot(command_prefix=secret['command_prefix'])

@bot.event
async def on_ready():
    print ("huehuehue")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)
    print("my name na {}".format(secret['botname']))

@bot.command(pass_context=True)
async def ping(ctx):
    embed=discord.Embed(description="Pong! :ping_pong:",color=embedcolor)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def work():
    responses1=[
        "Superb",
        "Phenomenal",
        "Horrendous",
        "Retarded"
    ]
    responses2=[
        "Scraper",
        "Eater",
        "Sleeper"
    ]
    response=random.choice(responses1)+" "+random.choice(responses2)
    embed=discord.Embed(description="Hmn... your job is a **{}**".format(response),color=embedcolor)
    await bot.say(embed=embed)
    localtime = time.localtime(time.time())
    print("User requested command work.")

bot.run(secret['token'])