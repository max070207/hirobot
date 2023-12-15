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

	@commands.command(aliases=["dolphin", "дельфин"])
	@commands.guild_only()
	async def __dolphin(self, ctx):
		status = check_category(str(ctx.guild.id), "Images")
		if status == 0:
			return
		pictures = ['https://funik.ru/wp-content/uploads/2018/12/907d5713fbecc7a67735.jpeg',
					'https://dogcatdog.ru/wp-content/uploads/f/a/2/fa2a2525440b2a5591bbc2c1993fa929.jpe',
					'https://avatars.mds.yandex.net/get-zen_doc/3704848/pub_5f329de8c426303aa4d459d5_5f32b1aed4bf6f68b107109b/scale_1200',
					'https://memestatic.fjcdn.com/large/pictures/17/f9/17f9bc_6773512.jpg',
					'https://s1.1zoom.ru/b5050/387/407014-sepik_1440x900.jpg',
					'https://dogcatdog.ru/wp-content/uploads/0/6/3/06328a9c7c541963752865182c420d7e.jpe',
					'https://placepic.ru/wp-content/uploads/2019/06/1515142216_delfin_lezgit.jpg',
					'https://placepic.ru/wp-content/uploads/2019/06/01-black-sea-bottlenose-dolphin.jpg',
					'https://dogcatdog.ru/wp-content/uploads/9/a/9/9a9f3c3f393a491b53d03ae1604bcbaf.jpg',
					'https://dogcatdog.ru/wp-content/uploads/2/f/9/2f9688d22b18a91b7b90f9b9eeb946ab.jpe']
		embed=discord.Embed(title="Дельфин! 🐬")
		embed.set_image(url=f"{random.choice(pictures)}")
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))