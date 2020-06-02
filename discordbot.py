# -*- coding: utf-8 -*-
from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='k.')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.event
async def on_message(message):
    try:
        if message.author.bot:
            return
        await bot.process_commands(message)
    except Exception:
        await message.channel.send(f'```\n{traceback.format_exc()}\n```')


@bot.commands
async def test(ctx):
    await ctx.send('おまんこ')


bot.run(token)
