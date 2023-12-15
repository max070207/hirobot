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

	@commands.command(aliases=["cow", "корова"])
	@commands.guild_only()
	async def __cow(self, ctx):
		status = check_category(str(ctx.guild.id), "Images")
		if status == 0:
			return
		pictures = ['https://dommovik.ru/sites/default/files/field/image/korova_0.jpg',
					'https://get.pxhere.com/photo/grass-white-field-farm-meadow-wildlife-rural-young-food-cow-cattle-pasture-grazing-brown-mammal-agriculture-beef-fauna-calf-close-up-australia-paddock-bull-face-stock-vertebrate-queensland-horns-dairy-cow-cattle-like-mammal-cow-goat-family-texas-longhorn-940960.jpg',
					'https://agrovitex.ru/files/uploads/articles/korova-lug.jpg',
					'https://get.pxhere.com/photo/nature-grass-field-farm-meadow-prairie-flower-animal-wildlife-rural-cow-pasture-grazing-mammal-agriculture-beef-fauna-calf-graze-face-eyes-grassland-head-mammals-coupling-habitat-ox-rural-area-milk-cow-simmental-cattle-dairy-cow-cattle-like-mammal-texas-longhorn-543970.jpg',
					'https://proza.ru/pics/2016/02/22/546.jpg',
					'https://get.pxhere.com/photo/landscape-grass-meadow-prairie-animal-wildlife-horn-cow-pasture-grazing-clean-mammal-health-fauna-calf-stroll-bull-grassland-vertebrate-pretty-dairy-cow-yellow-cattle-artistic-conception-cattle-like-mammal-cow-goat-family-texas-longhorn-1363449.jpg',
					'https://cdn.pixabay.com/photo/2017/09/24/23/24/cow-2783568_1280.jpg',
					'https://petnaobed.ru/wp-content/uploads/2021/01/cow-941951_1280.jpg',
					'https://avatars.mds.yandex.net/get-zen_doc/1574327/pub_5cd90383bd085200b36d56a6_5cd903e677f0d500b351492d/scale_1200',
					'https://cdn.pixabay.com/photo/2015/10/11/21/34/cow-983119_1280.jpg']
		embed=discord.Embed(title="Корова! 🐮")
		embed.set_image(url=f"{random.choice(pictures)}")
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))