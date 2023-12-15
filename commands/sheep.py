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

	@commands.command(aliases=["sheep", "овца"])
	@commands.guild_only()
	async def __sheep(self, ctx):
		status = check_category(str(ctx.guild.id), "Images")
		if status == 0:
			return
		pictures = ['https://cdn.pixabay.com/photo/2015/10/11/21/45/sheep-983137_1280.jpg',
					'https://wallbox.ru/resize/1680x1050/wallpapers/main2/201815/lug-skvorcy-zivotno-e-barany.jpg',
					'https://прорабофф.рф/wp-content/uploads/e/f/6/ef6814ad451cd6e77495d425d8deb3f6.jpg',
					'https://domstrousam.ru/wp-content/webp-express/webp-images/doc-root/wp-content/uploads/2021/04/domashnie_givotnie12.jpg.webp',
					'https://zagadki-dlya-detej.ru/wp-content/uploads/2020/12/ovca.jpg',
					'https://ya-fab.ru/wp-content/uploads/2021/01/img_16110127778092-1-1024x576.png',
					'https://get.pxhere.com/photo/grass-meadow-pasture-grazing-sheep-mammal-fauna-lamb-goats-grassland-look-vertebrate-sheeps-cow-goat-family-1213326.jpg',
					'https://cdn.pixabay.com/photo/2017/06/12/09/09/sheep-2394931_1280.jpg',
					'https://imya-sonnik.ru/wp-content/uploads/2019/10/13-34.jpg',
					'https://get.pxhere.com/photo/grass-farm-meadow-flock-wildlife-horn-fur-herd-pasture-grazing-livestock-sheep-mammal-wool-fauna-flock-of-sheep-animals-vertebrate-sheeps-cow-goat-family-772408.jpg']
		embed=discord.Embed(title="Овца! 🐑")
		embed.set_image(url=f"{random.choice(pictures)}")
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))