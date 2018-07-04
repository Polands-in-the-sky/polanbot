import asyncio
import rethinkdb as r

@bot.command(pass_context=True)
async def xpregister(ctx):
    embed=discord.Embed(title="Registered",value="You are registered in our XP database. Now you can play games with the bot.")
    await bot.say(embed=embed)