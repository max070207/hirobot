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

	@commands.command(aliases=["pig", "свинья"])
	@commands.guild_only()
	async def __pig(self, ctx):
		status = check_category(str(ctx.guild.id), "Images")
		if status == 0:
			return
		pictures = ['https://proroslo.ru/wp-content/uploads/2020/03/svinja-na-alpijskom-lugu_result.jpg',
					'https://astromeridian.su/wp-content/uploads/2020/03/khaj-svinya.jpg',
					'https://sciencepop.ru/wp-content/uploads/2017/10/pig-214349_1280.jpg',
					'https://vladimir.pk-izhsintez.ru/upload/iblock/6b7/6b71fe2c4549150eb0207bbadce6ee57.jpg',
					'http://veterikom.ru/wp-content/uploads/2020/10/pig1.jpg',
					'https://tatarstan.ru/file/news/1281_n1871739_big.jpg',
					'https://solreg.ru/upload/iblock/67d/67d8083151545e3fcd37503fe0de0a1e.jpg',
					'https://1tulatv.ru/sites/default/files/og0je63.jpg',
					'https://fb.ru/misc/i/gallery/52858/2552674.jpg',
					'http://ivanovsinsky.ru/thumb/2/AePwvlfaE2ostGurmOXsXg/1920r/d/kormovyye_dobavki_dlya_otkorma_sviney_porosyat_gumat_kupit.jpg']
		embed=discord.Embed(title="Свинья! 🐷")
		embed.set_image(url=f"{random.choice(pictures)}")
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))