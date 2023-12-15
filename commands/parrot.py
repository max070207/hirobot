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

	@commands.command(aliases=["parrot", "попугай"])
	@commands.guild_only()
	async def __parrot(self, ctx):
		status = check_category(str(ctx.guild.id), "Images")
		if status == 0:
			return
		pictures = ['https://astromeridian.su/wp-content/uploads/2020/08/parrot-2909835_1280.jpg',
					'https://w-dog.ru/wallpapers/5/9/304922762479902/pticy-popugaj-ara.jpg',
					'https://img3.goodfon.ru/wallpaper/nbig/a/78/kakadu-mnogocvetnyy-loriket.jpg',
					'https://avatars.mds.yandex.net/get-zen_doc/1880741/pub_5edbd76ce8e24e636af4f632_5edbed29dc508b6b0949e298/scale_1200',
					'https://www.sunhome.ru/i/wallpapers/146/popugai-kartinka-oboi.xxl.jpg',
					'https://avatars.mds.yandex.net/get-zen_doc/3636601/pub_600fef98052efe27dff2bf85_600ff0cbcd098e46b1f2a975/scale_1200',
					'http://pm1.narvii.com/7532/a56c379fa6fa2e968f0d4f18e528529e81bb2e13r1-1200-1800v2_uhq.jpg',
					'https://krasivosti.pro/uploads/posts/2021-04/1618941120_30-krasivosti_pro-p-glyantsevii-popugai-ptitsi-krasivo-foto-33.jpg',
					'https://stihi.ru/pics/2021/01/03/6658.jpg',
					'https://avatars.mds.yandex.net/get-zen_gallery/2784445/pub_5f93270798e57704a125ac9d_5f932725a81c50318ef39aa7/scale_1200']
		embed=discord.Embed(title="Попугай! 🦜")
		embed.set_image(url=f"{random.choice(pictures)}")
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))