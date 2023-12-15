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

	@commands.command(aliases=["whale", "кит"])
	@commands.guild_only()
	async def __whale(self, ctx):
		status = check_category(str(ctx.guild.id), "Images")
		if status == 0:
			return
		pictures = ['https://placepic.ru/wp-content/uploads/2018/12/10-5.jpg',
					'https://kipmu.ru/wp-content/uploads/ktvnshnvd.jpg',
					'https://dogcatdog.ru/wp-content/uploads/8/f/a/8faffee979d260dd7752a8eb57aaec66.jpg',
					'https://animalreader.ru/wp-content/uploads/2016/08/gorbatye-kity-zashhishhajut-drugih-zhivotnyh-animalreader.ru-001.jpg',
					'https://yobte.ru/uploads/posts/2019-12/plavanie-s-velichestvennymi-kitami-7.jpg',
					'https://avatars.mds.yandex.net/get-zen_doc/1889495/pub_60786ea14825fd786446e810_6078a449ab0734414f1deb63/scale_1200',
					'https://web-zoopark.ru/wp-content/uploads/2018/06/2-635.jpg',
					'https://i.pinimg.com/736x/ec/b1/95/ecb195c016fd4c2cb2c4022173200643.jpg',
					'https://avatars.mds.yandex.net/get-zen_doc/1064817/pub_5b795942581d1a00a83058df_5b7959776cf6c700aa7e19c1/scale_1200',
					'https://bitoflife.ru/wp-content/uploads/2019/07/s1200-1.jpg']
		embed=discord.Embed(title="Кит! 🐳")
		embed.set_image(url=f"{random.choice(pictures)}")
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))