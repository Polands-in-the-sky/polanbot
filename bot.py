#!/usr/bin/python
import praw
import pdb
import re
import os
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import time
import rethinkdb as r
import json
import modules.voice
import modules.games
reddit=praw.Reddit('bot1')
secrets_file=open("secrets.json")
secrets=secrets_file.read()
secret=json.loads(secrets)
embedcolor=0x64C13F
bot = commands.Bot(command_prefix=secret['command_prefix'])
print("Oi you wot")
@bot.event
async def on_ready():
    print ("huehuehue")
    print ("I am running on " + bot.user.name)
    print ("With the ID: " + bot.user.id)
    conn=r.connect(port=8015,db="db")

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
    embed.add_field(name="Money earned",value=":moneybag: You earned ${} from that. :moneybag:".format(random.randint(1,1000)))
    await bot.say(embed=embed)
    localtime = time.localtime(time.time())
    print("User requested command work.")
#Reddit related functionalities

@bot.command(pass_context=True)
async def redditpopular(ctx,arg):
    subreddit = reddit.subreddit(arg)
    for submission in subreddit.hot(limit=1):
        embed=discord.Embed(title=submission.title,description=submission.selftext,color=embedcolor)
        embed.add_field(name="Points",value=submission.score)
        await bot.say(embed=embed)
#info
@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    embed = discord.Embed(title="{}\'s info".format(user.display_name),description="Hi",color=embedcolor)
    embed.add_field(name="User ID",value="{}".format(user.id),inline=True)
    embed.add_field(name="Status",value="{}".format(user.status),inline=True)
    embed.add_field(name="User's highest role",value="{}".format(user.top_role),inline=True)
    embed.add_field(name="Date of joining the server",value="{}".format(user.joined_at))
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)
    print("User has requested the info of {}.".format(user.name))

@bot.command(pass_context=True)
async def serverinfo(ctx):
    embed = discord.Embed(name="{}'s info".format(ctx.message.server.name), description="Here's what I could find.", color=embedcolor)
    embed.set_author(name="polanbot")
    embed.add_field(name="Name", value=ctx.message.server.name, inline=True)
    embed.add_field(name="ID", value=ctx.message.server.id, inline=True)
    embed.add_field(name="Roles", value=len(ctx.message.server.roles), inline=True)
    embed.add_field(name="Members", value=len(ctx.message.server.members))
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)
    print("User has requested server info.")


bot.run(secret['token'])