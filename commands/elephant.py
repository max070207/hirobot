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

	@commands.command(aliases=["elephant", "слон"])
	@commands.guild_only()
	async def __elephant(self, ctx):
		status = check_category(str(ctx.guild.id), "Images")
		if status == 0:
			return
		pictures = ['https://stihi.ru/pics/2020/05/11/6339.jpg',
					'https://img3.goodfon.ru/wallpaper/nbig/d/a2/zhivotnye-slon-bivni-slony.jpg',
					'https://regnum.ru/uploads/pictures/news/2018/03/12/regnum_picture_1520840885253630_normal.jpg',
					'https://web-zoopark.ru/wp-content/uploads/2018/07/11-47-768x463-4.jpg',
					'https://vsezhivoe.ru/wp-content/uploads/2017/09/maxresdefault-6-1024x640.jpg',
					'https://grandgames.net/puzzle/f1200/slon_2.jpg',
					'https://ds05.infourok.ru/uploads/ex/06c3/0016d69a-0d3e4fac/hello_html_m1130b308.jpg',
					'https://funart.pro/uploads/posts/2021-04/1618131903_5-p-bolshoi-slon-zhivotnie-krasivo-foto-6.jpg',
					'https://petzona.ru/wp-content/uploads/2018/08/Africa-elephants-cub_1920x1080.jpg',
					'https://top10a.ru/wp-content/uploads/2020/01/1-42.jpg']
		embed=discord.Embed(title="Слон! 🐘")
		embed.set_image(url=f"{random.choice(pictures)}")
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))