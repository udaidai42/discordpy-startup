from discord.ext import commands
from PIL import Image
width = 500
height = 500
import os
import traceback

bot = commands.Bot(command_prefix='k.')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def test(message):
    if message.author.bot:
        return
    await message.channel.send('うい')

bot.run(token)
