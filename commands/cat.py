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

	@commands.command(aliases=["cat", "кот"])
	@commands.guild_only()
	async def __cat(self, ctx):
		status = check_category(str(ctx.guild.id), "Images")
		if status == 0:
			return
		pictures = ['https://classpic.ru/wp-content/uploads/2017/02/26894/Milye-kotyata-spyat-v-sharfe.jpg',
					'https://kto-chto-gde.ru/wp-content/uploads/2016/11/337496f4e9566cae4d79732057a2016e.jpg',
					'https://proprikol.ru/wp-content/uploads/2019/08/skachat-milye-kartinki-14.jpg',
					'https://2ch.pm/cute/src/120/14141517612451.jpg',
					'https://www.zastavki.com/pictures/originals/2018Animals___Cats_Two_cute_sleeping_kitten_on_a_gray_background_124752_.jpg',
					'https://img5.goodfon.ru/original/3840x2160/4/1f/koshka-glaza-kot-vzgliad-milaia-krovat-portret-razmytost-mor.jpg',
					'https://im0-tub-ru.yandex.net/i?id=7fdfdcea3c25db51cdfaabb1bdbf3b04&ref=rim&n=33&w=480&h=144',
					'https://img1.goodfon.ru/original/1920x1080/2/6a/kotyata-spyat-son-odeyalo-ushi.jpg',
					'https://avatanplus.com/files/resources/original/5be2e66020717166ee53e785.jpg']
		embed=discord.Embed(title="Кот! 🐱")
		embed.set_image(url=f"{random.choice(pictures)}")
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))