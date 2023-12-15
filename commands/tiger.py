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

	@commands.command(aliases=["tiger", "тигр"])
	@commands.guild_only()
	async def __tiger(self, ctx):
		status = check_category(str(ctx.guild.id), "Images")
		if status == 0:
			return
		pictures = ['http://faunazoo.ru/wp-content/uploads/2019/03/%D0%A2%D0%B8%D0%B3%D1%80.jpg',
					'https://dogcatdog.ru/wp-content/uploads/0/4/2/042ad1f6ee2d951878bcb3c0c5b8d718.jpg',
					'https://lookw.ru/1/184/1380317248-172227.jpg',
					'https://w-dog.ru/wallpapers/5/9/450840564158180/tigr-zver-vzglyad-zelen.jpg',
					'https://dogcatdog.ru/wp-content/uploads/3/7/0/37084d126e96275ecac85dcb42b71fbb.jpg',
					'https://masyamba.ru/%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B8-%D1%82%D0%B8%D0%B3%D1%80%D0%B0/59-%D0%BA%D0%B0%D1%80%D1%82%D0%B8%D0%BD%D0%BA%D0%B8-%D1%82%D0%B8%D0%B3%D1%80%D1%8B-%D0%BA%D1%80%D0%B0%D1%81%D0%B8%D0%B2%D1%8B%D0%B5.jpg',
					'https://placepic.ru/wp-content/uploads/2018/11/2-1.jpg',
					'https://s1.1zoom.ru/b5250/394/Tigers_Grass_565301_2048x2732.jpg',
					'https://i.artfile.ru/2560x1600_643081_[www.ArtFile.ru].jpg',
					'https://dogcatdog.ru/wp-content/uploads/d/5/2/d522202c4361c743bc60155c97106550.jpg']
		embed=discord.Embed(title="Тигр! 🐯")
		embed.set_image(url=f"{random.choice(pictures)}")
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))