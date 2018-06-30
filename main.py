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
redditbot=praw.Reddit('bot1')
secrets_file=open("secrets.json")
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
    work_responses1=[
        "Superb",
        "Phenomenal",
        "Horrendous",
        "Retarded"
    ]
    work_responses2=[
        "Scraper",
        "Eater",
        "Sleeper"
    ]
    work_response=random.choice(work_responses1)+" "+random.choice(work_responses2)
    embed=discord.Embed(description="Hmn... your job is a **{}**".format(work_response),color=embedcolor)
    await bot.say(embed=embed)
    localtime = time.localtime(time.time())
    print("User requested command work.")

@bot.command(pass_context=True)
async def redditpopular(ctx,arg):
    subreddit = reddit.subreddit(arg)
    for submission in subreddit.hot(limit=1):
        embed=discord.Embed(title=submission.title,description=submission.selftext,color=embedcolor)
        embed=add_field(name="Points",value=submission.score)
        await bot.say(embed=embed)

bot.run(secret['token'])