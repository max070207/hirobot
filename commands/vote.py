# -*- coding: utf-8 -*-

import discord
from discord.ext import commands
from discord import utils
from discord.utils import get
import random
import os
import datetime
import time
import math
import platform
import asyncio
from Cybernator import Paginator
import requests
import json
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from discord.ext import tasks
from discord import ActivityType
import ast

class Command(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=["vote", "проголосовать"])
    @commands.guild_only()
    async def __vote(self, ctx):
        embed=discord.Embed(description="**Если вы хотите проголосовать за бота/сервер и подвинуть их в топ, то можете перейти по этим ссылкам:**", color=discord.Color.blue())
        embed.add_field(name="Бот", value="• [Top.gg](https://top.gg/bot/717753722268024833)\n• [Discord Bot List](https://discordbotlist.com/bots/hiro-bot)\n• [Discord Bots](https://discord.bots.gg/bots/717753722268024833)\n• [Discord Boats](https://discord.boats/bot/717753722268024833)\n• [SD.C Bot List](https://bots.server-discord.com/717753722268024833)\n• [Boticord](https://boticord.top/bot/717753722268024833)")
        embed.add_field(name="Сервер", value="• [Disboard](https://disboard.org/ru/server/742412214903767110)\n• [Discord Servers](https://discord-server.com/742412214903767110)\n• [SD.C](https://server-discord.com/742412214903767110)\n• [DiscordServer.info](https://discordserver.info/742412214903767110)")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Command(bot))