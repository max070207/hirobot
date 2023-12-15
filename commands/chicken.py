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

	@commands.command(aliases=["chicken", "курица"])
	@commands.guild_only()
	async def __chicken(self, ctx):
		status = check_category(str(ctx.guild.id), "Images")
		if status == 0:
			return
		pictures = ['https://russkie-perepela.ru/wp-content/uploads/f/6/d/f6dea7536abbc2646731e4cc074300d3.jpeg',
					'https://kartinkin.com/uploads/posts/2021-03/1617189106_42-p-kuritsa-krasivo-42.jpg',
					'https://kartinkin.com/uploads/posts/2020-07/1593750229_17-p-kuritsi-na-svetlikh-fonakh-18.jpg',
					'https://demotivation.ru/wp-content/uploads/2020/06/s1200-116.jpg',
					'https://nashzelenyimir.ru/wp-content/uploads/2015/12/%D0%9A%D1%83%D1%80%D0%B8%D1%86%D0%B0-%D1%81-%D1%86%D1%8B%D0%BF%D0%BB%D1%8F%D1%82%D0%B0%D0%BC%D0%B8-%D1%84%D0%BE%D1%82%D0%BE.jpg',
					'https://demotivation.ru/wp-content/uploads/2020/06/1-335-scaled.jpg',
					'https://russkie-perepela.ru/wp-content/uploads/c/4/d/c4d6c181e2acdd7fb1e7d2fb54553b96.jpeg',
					'https://avatars.mds.yandex.net/get-zen_doc/1349008/pub_5ea1c7ce5e355f55ca82e1ec_5ea1c83b2bf35767fbb2224c/scale_1200',
					'https://russkie-perepela.ru/wp-content/uploads/e/f/a/efa51b69cec8d8a12a2f8d98707054b3.jpeg',
					'https://m-chu.ru/wp-content/uploads/2019/03/water-bird-summer-flow-beak-chicken-fowl-fauna-rooster-poultry-power-galliformes-vertebrate-phasianidae-1003056.jpg']
		embed=discord.Embed(title="Курица! 🐔")
		embed.set_image(url=f"{random.choice(pictures)}")
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))