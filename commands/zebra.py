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

	@commands.command(aliases=["zebra", "зебра"])
	@commands.guild_only()
	async def __zebra(self, ctx):
		status = check_category(str(ctx.guild.id), "Images")
		if status == 0:
			return
		pictures = ['https://fb.ru/media/i/1/1/5/7/8/9/6/i/1157896.jpg',
					'https://get.pxhere.com/photo/adventure-wildlife-zoo-africa-mammal-fauna-savanna-zebra-grassland-botswana-safari-horse-like-mammal-738098.jpg',
					'https://placepic.ru/wp-content/uploads/2019/06/s1200-2-11.jpg',
					'https://avatars.mds.yandex.net/get-zen_doc/196516/pub_5ab126eb20ea2b0674a31c93_5ab22ed69e29a233a350e1e7/scale_1200',
					'https://avatars.mds.yandex.net/get-zen_doc/1679483/pub_5da431ee8600e100ae8131c7_5da4370caad43600adaf79f1/scale_1200',
					'https://avatars.mds.yandex.net/get-zen_doc/1936066/pub_5eafd9dbb95e7e69bd2eb5f7_5eafda8e2027132c419e2fb8/scale_1200',
					'https://zeleniymir.org/wp-content/uploads/2019/04/Zebra-59-1024x936.jpg',
					'https://placepic.ru/wp-content/uploads/2019/06/2-zebras.jpg',
					'http://imgtube.ru/images/stories/2013/02/927-zebra/8.jpg',
					'https://i1.wp.com/ic.pics.livejournal.com/shukerearth/25477671/234834/234834_original.jpg']
		embed=discord.Embed(title="Зебра! 🦓")
		embed.set_image(url=f"{random.choice(pictures)}")
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))