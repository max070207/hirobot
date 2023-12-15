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

	@commands.command(aliases=["penguin", "пингвин"])
	@commands.guild_only()
	async def __penguin(self, ctx):
		status = check_category(str(ctx.guild.id), "Images")
		if status == 0:
			return
		pictures = ['https://avatars.mds.yandex.net/get-zen_doc/48747/pub_5cf71f27c0dc5700afbb9e69_5cf71fbee24ab100bce1b7b3/scale_1200',
					'http://poznanie21.ru/wp-content/uploads/2019/09/s12001.jpg',
					'https://4lapki.com/wp-content/uploads/2019/01/4-11.jpg',
					'https://national-travel.ru/wp-content/uploads/wtt-images/2021/04/pingvin-23023.jpg',
					'https://im0-tub-ru.yandex.net/i?id=db7dd24f7e2fa422e3b713e463ca6c2e-l&n=13',
					'http://hellotraveler.ru/wp-content/uploads/2015/02/Emperor-penguins-in-Antarctica-9.jpg',
					'https://avatars.mds.yandex.net/get-zen_doc/3418917/pub_5f00f9a6f6d6522ad12af265_5f00fa0b1958ab3d4207b2fb/scale_1200',
					'https://100zaitsev.ru/wp-content/uploads/512710.jpg',
					'https://bitoflife.ru/wp-content/uploads/2021/04/s1200.jpg',
					'https://avatars.mds.yandex.net/get-zen_doc/1336031/pub_5b0055323dceb7c9dbe153e9_5b0057e3a936f4e52e30b605/scale_1200']
		embed=discord.Embed(title="Пингвин! 🐧")
		embed.set_image(url=f"{random.choice(pictures)}")
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))