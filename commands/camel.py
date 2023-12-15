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

	@commands.command(aliases=["camel", "верблюд"])
	@commands.guild_only()
	async def __camel(self, ctx):
		status = check_category(str(ctx.guild.id), "Images")
		if status == 0:
			return
		pictures = ['https://pic.rutube.ru/video/c3/89/c389fbb58a67d872b5436b21c68ca212.jpg',
					'https://avatars.mds.yandex.net/get-zen_doc/4338516/pub_60621aea3ebe7f2d784b369f_60621b350bfe8b31339262b4/scale_1200',
					'https://pic.rutube.ru/video/98/9e/989e470c9ef833e083e770f42a00bd62.jpg',
					'https://avatars.mds.yandex.net/get-zen_doc/4491962/pub_6096b15f87bf2977fc85fcf2_6096b18ab8f34b04d2b189d1/scale_1200',
					'https://nashzelenyimir.ru/wp-content/uploads/2015/10/%D0%9E%D0%B4%D0%BD%D0%BE%D0%B3%D0%BE%D1%80%D0%B1%D1%8B%D0%B9-%D0%B2%D0%B5%D1%80%D0%B1%D0%BB%D1%8E%D0%B4-%D0%B4%D1%80%D0%BE%D0%BC%D0%B5%D0%B4%D0%B0%D1%80-%D0%B4%D1%80%D0%BE%D0%BC%D0%B0%D0%B4%D0%B5%D1%80-%D1%84%D0%BE%D1%82%D0%BE.jpg',
					'http://oukrai.kolos.obr55.ru/wp-content/uploads/2021/02/dfdv_ztv4aaqq4k.jpg',
					'https://funart.pro/uploads/posts/2021-07/1626759181_3-funart-pro-p-krasivii-verblyud-zhivotnie-krasivo-foto-3.jpg',
					'https://web-zoopark.ru/wp-content/uploads/2018/07/1-kopiya-8.jpg',
					'https://filed4-9.my.mail.ru/pic?url=https%3A%2F%2Fsites.google.com%2Fsite%2Fmirokzhivotnyh%2F_%2Frsrc%2F1455643981075%2Fhome%2Fverblud%2Fd3f946ec2c83a9aec48cebf563fac2dc.jpg&mw=&mh=&sig=6dfade8d659d9d24f070975595fe8987',
					'https://im0-tub-ru.yandex.net/i?id=1ef5d36cbc3cd234ede77168d1b1b73b-l&n=13']
		embed=discord.Embed(title="Верблюд! 🐪")
		embed.set_image(url=f"{random.choice(pictures)}")
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))