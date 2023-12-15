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

	@commands.command(aliases=["kangaroo", "кенгуру"])
	@commands.guild_only()
	async def __kangaroo(self, ctx):
		status = check_category(str(ctx.guild.id), "Images")
		if status == 0:
			return
		pictures = ['https://famt.ru/wp-content/uploads/2019/03/videt-vo-sne-kenguru-znachenie-dlya-zhenschiny-ili-devushki.jpg',
					'https://100-faktov.ru/wp-content/uploads/2017/05/8cdada40ded61b078e61.jpg',
					'https://potokmedia.ru/wp-content/uploads/2021/06/DIm-oRXWsAA0Kbu.jpg',
					'https://kartinkin.com/uploads/posts/2015-11/1448623751_51.jpg',
					'https://i04.fotocdn.net/s125/48b3d3d630f0c8cf/public_pin_l/2854965233.jpg',
					'https://funart.pro/uploads/posts/2020-02/1582403709_11-p-kenguru-yevgenii-84.jpg',
					'https://avatars.mds.yandex.net/get-zen_doc/1118263/pub_5b7ab1d40034bc00a9f456e5_5b7ab35dda8c9200a957e101/scale_1200',
					'https://cdn.fishki.net/upload/post/2016/07/07/2005176/cb81aa1feb245733a8f2be76f97a4459.jpg',
					'https://placepic.ru/wp-content/uploads/2018/11/31acc_0_adb73_8430a4b5_orig.jpg',
					'https://placepic.ru/wp-content/uploads/2018/11/31acc_0_adb75_c66e542c_orig.jpg']
		embed=discord.Embed(title="Кенгуру! 🦘")
		embed.set_image(url=f"{random.choice(pictures)}")
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))