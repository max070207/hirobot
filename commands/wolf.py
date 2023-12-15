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

	@commands.command(aliases=["wolf", "волк"])
	@commands.guild_only()
	async def __wolf(self, ctx):
		status = check_category(str(ctx.guild.id), "Images")
		if status == 0:
			return
		pictures = ['https://vsezhivoe.ru/wp-content/uploads/2017/09/20.jpg',
					'https://pbs.twimg.com/media/E6WweHAWUAE4VV0.jpg',
					'https://funik.ru/wp-content/uploads/2018/11/3775daf26943d820d481.jpg',
					'http://kp-pravda.ru/wp-content/uploads/2021/04/9-92.jpg',
					'https://i.pinimg.com/736x/fa/82/d4/fa82d45c9e5970f207074ec53c2d706c.jpg',
					'https://attuale.ru/wp-content/uploads/2018/11/gray-wolf-oregon-delisting-1220x811.jpg',
					'https://velesovik.ru/images/illness/2814/gallery_699.jpg',
					'https://interesnyefakty.org/wp-content/uploads/seryj-volk.jpg',
					'https://ugo-osetia.ru/wp-content/uploads/%D0%92%D0%9E%D0%9B%D0%9A%D0%98-2.jpg',
					'https://web-zoopark.ru/wp-content/uploads/2018/07/3-147.jpg']
		embed=discord.Embed(title="Волк! 🐺")
		embed.set_image(url=f"{random.choice(pictures)}")
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))