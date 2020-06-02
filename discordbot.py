# -*- coding: utf-8 -*-
from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='k.')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.commands
async def test(ctx):
    await ctx.send('おまんこ')


bot.run(token)
