# -*- coding: utf-8 -*-
from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='k.')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.command
async def test(message):
    await message.send('p')

bot.run(token)
