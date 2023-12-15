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

	@commands.command(aliases=["owl", "сова"])
	@commands.guild_only()
	async def __owl(self, ctx):
		status = check_category(str(ctx.guild.id), "Images")
		if status == 0:
			return
		pictures = ['https://funik.ru/wp-content/uploads/2018/11/9697877aa33cba31b65b.jpg',
					'https://s3.nat-geo.ru/images/2019/5/16/20b3e00347a8427eaa9e29e749c92a25.max-1200x800.jpg',
					'https://funik.ru/wp-content/uploads/2018/11/c7b93869070a5674a1b0.jpg',
					'https://w-dog.ru/wallpapers/5/8/331894559050171/moxnonogij-sych-nebolshaya-sova-les-derevo-vetki-igolki.jpg',
					'https://pbs.twimg.com/media/EZ00mjgX0AIGU_m.jpg',
					'https://krasivosti.pro/uploads/posts/2021-04/1619084058_21-krasivosti_pro-p-simpatichnaya-sova-ptitsi-krasivo-foto-23.jpg',
					'https://krasivosti.pro/uploads/posts/2021-04/1619084102_9-krasivosti_pro-p-simpatichnaya-sova-ptitsi-krasivo-foto-9.jpg',
					'https://litbro.ru/wp-content/uploads/2021/05/Vidyat-li-sovy-dnem.jpg',
					'https://astromeridian.su/wp-content/uploads/2020/01/ab2973953851afafa888.jpg',
					'https://img4.postila.ru/storage/12704000/12686880/b90ce38f2d476114db52b24b90e61998.jpg']
		embed=discord.Embed(title="Сова! 🦉")
		embed.set_image(url=f"{random.choice(pictures)}")
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))