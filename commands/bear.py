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

	@commands.command(aliases=["bear", "медведь"])
	@commands.guild_only()
	async def __bear(self, ctx):
		status = check_category(str(ctx.guild.id), "Images")
		if status == 0:
			return
		pictures = ['https://yandex.ru/images/_crpd/1PGCB8316/c638bdqx4/S67RdBamk61R4G_JvdOQ-au5Gm9nZYZkzU4SrURNvyuOFuMs3tyfYoSssqinKeGtYhEyx3_uitR48PFgKefBbA6_-VxrnoaVWakK2fwW8PiGkDc2B2DSCeAjWvU5Ea9r5z-zEDONnyO17dftAynNqR6tmksGMmcIoR093IWOiBAL-v0lY85rC',
					'https://avatars.mds.yandex.net/get-pdb/2113766/2821d0df-42ec-4a95-9a06-71e3870403b7/s1200?webp=false',
					'https://masyamba.ru/%D0%B1%D1%83%D1%80%D1%8B%D0%B9-%D0%BC%D0%B5%D0%B4%D0%B2%D0%B5%D0%B4%D1%8C/24-%D0%B1%D1%83%D1%80%D1%8B%D0%B9-%D0%BC%D0%B5%D0%B4%D0%B2%D0%B5%D0%B4%D1%8C-%D1%84%D0%BE%D1%82%D0%BE.jpg',
					'https://masyamba.ru/%D0%B1%D1%83%D1%80%D1%8B%D0%B9-%D0%BC%D0%B5%D0%B4%D0%B2%D0%B5%D0%B4%D1%8C/74-%D0%B1%D1%83%D1%80%D1%8B%D0%B9-%D0%BC%D0%B5%D0%B4%D0%B2%D0%B5%D0%B4%D1%8C-%D1%84%D0%BE%D1%82%D0%BE.jpg',
					'https://www.newsler.ru/data/content/2018/70899/69be69fed2dc474b404d10d4a8ab5c2a.jpg',
					'https://avatars.mds.yandex.net/get-zen_doc/1895227/pub_5e20ab35b477bf00adcdee2c_5e20abfb5d636200acbcf8f4/scale_1200',
					'https://sovetclub.ru/tim/90d97408615b368a1205f64d3cf16512.jpg',
					'https://wallpaperscave.ru/images/original/18/07-27/animals-bear-70731.jpg',
					'https://wallpaperscave.ru/images/original/18/05-06/animals-bear-48765.jpg',
					'https://avatars.mds.yandex.net/get-zen_doc/1895227/pub_5df244a9027a1500b0e9feaa_5df244cebd639600b1013fee/scale_1200',
					'https://s3.nat-geo.ru/images/2019/5/15/39e8eee980dc4da184f13a1cac6ca892.max-1200x800.jpg',
					'https://i.pinimg.com/736x/ad/fb/14/adfb14fb9ac69294baa90017d134ea01--nature-animals-wild-animals.jpg',
					'https://i1.wallbox.ru/wallpapers/main/201614/dcb04510de3c7bc.jpg',
					'https://avatars.mds.yandex.net/get-pdb/2092521/21ec1c67-3b2e-43f6-86d2-970b140a2720/s1200?webp=false']
		embed=discord.Embed(title="Медведь! 🐻")
		embed.set_image(url=f"{random.choice(pictures)}")
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))