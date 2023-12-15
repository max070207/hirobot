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

def check_category(guild, category):
    with open('/root/bot/databases/off_categories.json', 'r') as f:
        data = json.load(f)
    if not guild in data:
        data[guild] = {}
    if not category in data[guild]:
        return 1
    if data[guild][category]["status"] == "off":
        return 0
    else:
        return 1

async def add_money(user):
    userid = str(user.id)
    with open('/root/bot/databases/fight.json', 'r') as f:
        data = json.load(f)
    if not userid in data:
        data[userid] = {}
        data[userid]["exp"] = 0
        data[userid]["lvl"] = 1
        data[userid]["money"] = 0
        data[userid]["items"] = {}
    data[userid]["exp"] += 5
    data[userid]["money"] += 5
    exp = data[userid]["exp"]
    lvl = data[userid]["lvl"]
    money = data[userid]["money"]
    exp_end = lvl * 3 * 60 + 100
    if exp >= exp_end:
        data[userid]["lvl"] = lvl + 1
        data[userid]["money"] = money + 500
    with open('/root/bot/databases/fight.json', 'w') as f:
        json.dump(data,f,indent=4)

class Command(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=["imposter", "предатель"])
    @commands.guild_only()
    async def __imposter(self, ctx):
        status = check_category(str(ctx.guild.id), "Mini-games")
        if status == 0:
            return
        emojired = self.bot.get_emoji(841294255997583361)
        emojiblue= self.bot.get_emoji(841294325164933130)
        emojigreen = self.bot.get_emoji(841294280466890763)
        emojiwhite = self.bot.get_emoji(841294304688603146)
        embed1 = discord.Embed(title="Кто предатель?", description="Найдите предателя, до того, как реактор взорвётся!", color=0xff0000)
        embed1.add_field(name='Красный', value=f'{emojired}', inline=False)
        embed1.add_field(name='Синий', value=f'{emojiblue}', inline=False)
        embed1.add_field(name='Зелёный', value=f'{emojigreen}', inline=False)
        embed1.add_field(name='Белый', value=f'{emojiwhite}', inline=False)
        msg = await ctx.send(embed=embed1)
        imposter = random.randint(1,4)
        if imposter == 1:
            imposter = "**Красный**"
            emoji = str(emojired)
        elif imposter == 2:
            imposter = "**Синий**"
            emoji = str(emojiblue)
        elif imposter == 3:
            imposter = "**Зелёный**"
            emoji = str(emojigreen)
        elif imposter == 4:
            imposter = "**Белый**"
            emoji = str(emojiwhite)
        await msg.add_reaction(emojired)
        await msg.add_reaction(emojiblue)
        await msg.add_reaction(emojigreen)
        await msg.add_reaction(emojiwhite)
        emojis = [str(emojired), str(emojiblue), str(emojigreen), str(emojiwhite)]
        try: 
            reaction, member = await self.bot.wait_for('reaction_add', timeout=30.0, check=lambda reaction, member: str(reaction.emoji) in emojis and member.id == ctx.author.id)
        except TimeoutError:
            embed=discord.Embed(title="Поражение", description=f"Реактор взорвался. {imposter} был предателем.", color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            if str(reaction.emoji) == emoji:
                embed=discord.Embed(title="Победа", description=f"{imposter} был предателем.", color=discord.Color.blue())
                await ctx.send(embed=embed)
                await add_money(ctx.author)
            else:
                embed=discord.Embed(title="Неверно!", description=f"{imposter} был предателем.", color=discord.Color.red())
                await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Command(bot))