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

	@commands.command(aliases=["monkey", "обезьяна"])
	@commands.guild_only()
	async def __monkey(self, ctx):
		status = check_category(str(ctx.guild.id), "Images")
		if status == 0:
			return
		pictures = ['https://naked-science.ru/wp-content/uploads/2016/11/images_ss-140615-at-15.today-ss-slide-desktop.jpg',
					'https://lookw.ru/9/980/1566944536-1-38.jpg',
					'https://lookw.ru/9/980/1566944545-1-52.jpg',
					'https://suseky.com/wp-content/uploads/2015/10/32.jpg',
					'https://i.pinimg.com/originals/4f/24/fa/4f24fad32270f039abe0e76db6b9b521.jpg',
					'https://i1.wallbox.ru/wallpapers/main/201631/ebde09c0917a5b2.jpg',
					'https://lookw.ru/9/980/1566944515-1-17.jpg',
					'https://www.fonstola.ru/pic/201912/1280x800/fonstola.ru-360950.jpg',
					'https://live.staticflickr.com/6119/6260422263_5371fac424_b.jpg',
					'https://masyamba.ru/%D1%84%D0%BE%D1%82%D0%BE-%D0%BE%D0%B1%D0%B5%D0%B7%D1%8C%D1%8F%D0%BD/21-%D1%81%D0%BA%D0%B0%D1%87%D0%B0%D1%82%D1%8C-%D1%84%D0%BE%D1%82%D0%BE-%D0%BE%D0%B1%D0%B5%D0%B7%D1%8C%D1%8F%D0%BD%D1%8B.jpg']
		embed=discord.Embed(title="Обезьяна! 🐵")
		embed.set_image(url=f"{random.choice(pictures)}")
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))