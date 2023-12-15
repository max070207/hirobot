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

	@commands.command(aliases=["crocodile", "крокодил"])
	@commands.guild_only()
	async def __crocodile(self, ctx):
		status = check_category(str(ctx.guild.id), "Images")
		if status == 0:
			return
		pictures = ['https://dogcatdog.ru/wp-content/uploads/7/d/5/7d5a601216b394edc1a9217fd9303b4e.jpg',
					'https://foto-zverey.ru/krokodily/krokodil-1.jpg',
					'https://dogcatdog.ru/wp-content/uploads/c/9/8/c98722d9adf556129d961bb1657e3b55.jpe',
					'https://dogcatdog.ru/wp-content/uploads/3/8/a/38ab495a2d7307fdbe55d82291132e0a.jpe',
					'https://kartinkin.com/uploads/posts/2021-03/1616025490_44-p-krokodili-45.jpg',
					'https://icdn.lenta.ru/images/2020/01/27/20/20200127202649864/original_31a831e22540cc10b43c9327817c922c.jpg',
					'https://bestvietnam.ru/wp-content/uploads/2020/06/%D0%9A%D1%80%D0%BE%D0%BA%D0%BE%D0%B4%D0%B8%D0%BB%D1%8B.jpg',
					'https://dogcatdog.ru/wp-content/uploads/4/5/1/4510988675904ef3d86f1d80c410218b.jpe',
					'https://get.pxhere.com/photo/water-nature-leather-animal-cute-wildlife-wild-zoo-green-tropical-natural-africa-mammal-predator-reptile-scale-fauna-mouth-crocodile-alligator-drawing-eye-head-danger-skin-vertebrate-creature-teeth-carnivore-tooth-dangerous-cartoon-croc-crocodilia-american-alligator-nile-crocodile-1230203.jpg',
					'https://fotovmire.ru/wp-content/uploads/2019/06/16807/krokodil-s-otkrytoj-pastju-lezhit-na-trave.jpg']
		embed=discord.Embed(title="Крокодил! 🐊")
		embed.set_image(url=f"{random.choice(pictures)}")
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))