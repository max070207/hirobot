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

class Command(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command(aliases=["daily", "ежедн"])
	@commands.guild_only()
	@commands.cooldown(1, 86400, commands.BucketType.user)
	async def __daily(self, ctx):
		status = check_category(str(ctx.guild.id), "Mini-games")
		if status == 0:
			return
		try:
			with open('/root/bot/databases/fight.json', 'r') as f:
				data = json.load(f)
			num = random.randint(10,50)
			emoji_coin = self.bot.get_emoji(828277358690959380)
			if not str(ctx.author.id) in data:
				data[str(ctx.author.id)] = {}
				data[str(ctx.author.id)]["exp"] = 0
				data[str(ctx.author.id)]["lvl"] = 1
				data[str(ctx.author.id)]["money"] = 0
				data[str(ctx.author.id)]["items"] = {}
			data[str(ctx.author.id)]["money"] += num
			with open('/root/bot/databases/fight.json', 'w') as f:
				json.dump(data,f,indent=4)
			embed=discord.Embed(description=f"Сегодня Ваше вознаграждение составило **{num}** {emoji_coin}!", timestamp=datetime.datetime.utcnow())
			embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
			msg = await ctx.send(embed=embed)
			list_colors = ["0xff0000", "0xff2200", "0xff4400", "0xff6600", "0xff8800", "0xffaa00", "0xffcc00", "0xffee00", "0xeeff00", "0xccff00", "0xaaff00", "0x88ff00", "0x66ff00", "0x44ff00", "0x22ff00", "0x00ff00", "0x00ff22", "0x00ff44", "0x00ff66", "0x00ff88", "0x00ffaa", "0x00ffcc", "0x00ffee", "0x00eeff", "0x00ccff", "0x00aaff", "0x0088ff", "0x0066ff", "0x0044ff", "0x0022ff", "0x0000ff", "0x2200ff", "0x4400ff", "0x6600ff", "0x8800ff", "0xaa00ff", "0xcc00ff", "0xee00ff", "0xff00ee", "0xff00cc", "0xff00aa", "0xff0088", "0xff0066", "0xff0044", "0xff0022", "0xff0000"]
			c = 0
			while c < 46:
				embed.color = int(list_colors[c], 0)
				await msg.edit(embed=embed)
				time.sleep(0.01)
				c += 1
		except Exception as e:
			channel = self.bot.get_channel(870742823203373086)
			embed=discord.Embed(title="Ошибка! ```h!daily```", description=f"`{str(e)}`", color=discord.Color.red(), timestamp=datetime.datetime.utcnow())
			embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
			embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)
			await channel.send(embed=embed)

	@__daily.error
	async def daily_error(self, ctx, error):
		with open('/root/bot/databases/prefixes.json', 'r') as f:
			data = json.load(f)
			p = data[str(ctx.guild.id)]
		if isinstance(error, commands.CommandOnCooldown):
			emoji_no = self.bot.get_emoji(785095586671230986)
			time_to_retry = round(error.retry_after)
			embed=discord.Embed(title=f"{emoji_no} Ошибка!", description=f"Действует задержка!\nПопробуйте позже через `{time_to_retry}` секунд", color=discord.Color.red())
			await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))