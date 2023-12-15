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

	@commands.command(aliases=["horse", "лошадь"])
	@commands.guild_only()
	async def __horse(self, ctx):
		status = check_category(str(ctx.guild.id), "Images")
		if status == 0:
			return
		pictures = ['https://thypix.com/wp-content/uploads/horse-148.jpg',
					'https://kipmu.ru/wp-content/uploads/ksplshd-scaled.jpg',
					'https://i.pinimg.com/736x/ea/40/a7/ea40a794e946fb47d9c51c329c4a2fb9.jpg',
					'https://fermok.ru/wp-content/uploads/2017/08/horse-6-16.jpg',
					'https://mywishboard.com/thumbs/wish/j/a/v/1020x0_ouucsdylvgptsnai_jpg_c1e6.jpg',
					'https://i.pinimg.com/736x/63/b6/7c/63b67c010e4ed2d7dcbf45699eb55e42.jpg',
					'https://fb.ru/misc/i/gallery/53349/3202885.jpg',
					'https://s.mediasole.ru/images/619/619317/6.jpg',
					'https://thypix.com/wp-content/uploads/horse-71.jpg',
					'https://s1.1zoom.ru/b5050/659/Horses_Three_3_507391_3840x2400.jpg']
		embed=discord.Embed(title="Лошадь! 🐴")
		embed.set_image(url=f"{random.choice(pictures)}")
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))