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

	@commands.command(aliases=["panda", "панда"])
	@commands.guild_only()
	async def __panda(self, ctx):
		status = check_category(str(ctx.guild.id), "Images")
		if status == 0:
			return
		pictures = ['https://placepic.ru/wp-content/uploads/2019/06/meng-meng-zoo-berlin-2017-5951171171eed-1.jpg',
					'https://doseng.org/uploads/posts/2015-05/1431314591_57_955c21c24a3846e334925e7c97d01cda.jpg',
					'https://avatars.mds.yandex.net/get-zen_doc/4368340/pub_601e4da0f2a56f0eaa36a77e_601e9ea75fadcc22a9eec234/scale_1200',
					'https://turism.boltai.com/wp-content/uploads/sites/34/2020/01/1310.jpg',
					'https://placepic.ru/wp-content/uploads/2019/06/2011-04-29-Zoo-Madrid-Po-De-De-045-1.jpg',
					'https://cdn.pixabay.com/photo/2018/11/12/14/27/panda-3810951_1280.jpg',
					'https://avatars.mds.yandex.net/get-zen_doc/1687249/pub_5e9a8833c03183795a1530c7_5e9a88fc38c82369f4d8186e/scale_1200',
					'https://cameralabs.org/media/lab15/may/07-2/57_d0fa56a235a4ebc7c56965a801d3480c.jpg',
					'https://placepic.ru/wp-content/uploads/2019/06/4165166933b5aae5cf9338c084f0a821-1.jpg',
					'https://static.wikia.nocookie.net/disney-animals/images/e/e8/Panda_lunlun_ZA_8142-b.jpg/revision/latest?cb=20171205021050',
					'https://i.pinimg.com/originals/25/74/59/2574592eb2e43d2dd26bb9c226bb1f11.jpg',
					'https://i.pinimg.com/736x/96/bf/d7/96bfd78e225363a076ba8c71421dca7b.jpg',
					'https://finedays.ru/wp-content/uploads/2019/07/kogda-ty-prekrasna-i-ne-vidish-smysl-skryvat-eto-1.jpg',
					'https://i.artfile.ru/2000x1501_1191912_[www.ArtFile.ru].jpg',
					'http://komotoz.ru/photo/zhivotnye/images/panda/panda_08.jpg']
		embed=discord.Embed(title="Панда! 🐼")
		embed.set_image(url=f"{random.choice(pictures)}")
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))