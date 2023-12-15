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

	@commands.command(aliases=["giraffe", "жираф"])
	@commands.guild_only()
	async def __giraffe(self, ctx):
		status = check_category(str(ctx.guild.id), "Images")
		if status == 0:
			return
		pictures = ['http://s2.fotokto.ru/photo/full/534/5348847.jpg',
					'https://picturiadotnet.files.wordpress.com/2016/01/mt-kilimanjaro-tanzania5.jpg',
					'https://pro-selhoz.ru/wp-content/uploads/2017/09/zhiraf_7_13145136.jpg',
					'https://rusinfo.info/wp-content/uploads/5/6/d/56d5e47b80197e42d97a7bd993691e72.jpe',
					'https://petzona.ru/wp-content/uploads/2018/06/zhiraf-i-ego-detyonysh.jpg',
					'https://kipmu.ru/wp-content/uploads/zhrfpr.jpg',
					'https://avatars.mds.yandex.net/get-zen_doc/1705212/pub_5ce78408c64ffc00b23ff3b3_5ce784989676d700b3066ac2/scale_1200',
					'https://i2.wp.com/curious-world.ru/images/content/animals/08-2018/jiraf/6.jpg',
					'https://i1.wallbox.ru/wallpapers/main2/201732/afrika-mama-malys-zirafy.jpg',
					'https://placepic.ru/wp-content/uploads/2018/11/77i5970fbbb14e039.91126291.jpg']
		embed=discord.Embed(title="Жираф! 🦒")
		embed.set_image(url=f"{random.choice(pictures)}")
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))