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

	@commands.command(aliases=["dog", "пёс"])
	@commands.guild_only()
	async def __dog(self, ctx):
		status = check_category(str(ctx.guild.id), "Images")
		if status == 0:
			return
		pictures = ['https://www.zastavki.com/pictures/originals/2019Animals___Dogs_Two_little_golden_retriever_puppies_are_sitting_on_the_ground_132779_.jpg',
					'https://i0.wp.com/hronika.info/wp-content/uploads/2019/08/cropped-pesiki.jpg',
					'https://mirpozitiva.ru/wp-content/uploads/2019/11/1492520059_bigl_milyi_pyatnistyy.jpg',
					'https://trikky.ru/wp-content/blogs.dir/1/files/2020/05/01/sobachki.jpg',
					'https://funart.pro/uploads/posts/2020-03/1584645966_16-p-samie-krasivie-foni-s-zhivotnimi-97.jpg',
					'https://www.sunhome.ru/i/cards/32/otpravit-elektronnuyu-otkritku.orig.jpg',
					'https://hdwallsbox.com/wallpapers/l/1920x1200/4/animals-dogs-puppies-daschund-faces-1920x1200-3946.jpg',
					'https://fb.ru/misc/i/gallery/79677/2359886.jpg',
					'https://cdn.lifehacker.ru/wp-content/uploads/2016/10/dog_muzzle_butterfly_tongue_sticking_out_spring_summer_93617_1920x1200_1477474424.jpg',
					'https://million-wallpapers.ru/wallpapers/3/53/445700175124873/simpatichnye-bigl-shhenka.jpg',
					'https://lu-ua.com.ua/userfiles/image/catalog/photoimg_841806719.jpg']
		embed=discord.Embed(title="Пёс! 🐶")
		embed.set_image(url=f"{random.choice(pictures)}")
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))