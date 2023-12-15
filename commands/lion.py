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

	@commands.command(aliases=["lion", "лев"])
	@commands.guild_only()
	async def __lion(self, ctx):
		status = check_category(str(ctx.guild.id), "Images")
		if status == 0:
			return
		pictures = ['https://zhivotnyeplanety.ru/wp-content/uploads/2020/12/lev-48.jpg',
					'https://trikky.ru/wp-content/blogs.dir/1/files/2020/06/02/2020-06-02-05-59-44.jpg',
					'https://fotovmire.ru/wp-content/uploads/2019/03/9853/korol-lev-lezhit-na-trave-vozle-kamnja.jpg',
					'http://fototelegraf.ru/wp-content/uploads/2015/08/lev-10-1.jpg',
					'http://fototelegraf.ru/wp-content/uploads/2015/08/lev-10-2.jpg',
					'https://zhivotnyeplanety.ru/wp-content/uploads/2020/12/lev-52.jpg',
					'https://avatars.mds.yandex.net/get-zen_doc/3469057/pub_5eff760c18b22c5b071d1661_5eff7658314c9869ab3e3add/scale_1200',
					'https://w-dog.ru/wallpapers/5/15/515900918860041/afrika-lev-kusty.jpg',
					'https://kartinkin.com/uploads/posts/2021-03/thumbs/1616080251_33-p-lvov-krasivie-foto-35.jpg',
					'https://tourjournal.ru/wp-content/uploads/lev.jpg']
		embed=discord.Embed(title="Лев! 🦁")
		embed.set_image(url=f"{random.choice(pictures)}")
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))