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

	@commands.command(aliases=["rabbit", "заяц"])
	@commands.guild_only()
	async def __rabbit(self, ctx):
		status = check_category(str(ctx.guild.id), "Images")
		if status == 0:
			return
		pictures = ['https://cdn.fishki.net/upload/post/2016/07/08/2006567/21470467411-455e323764-k.jpg',
					'https://autogear.ru/misc/i/gallery/23144/2263645.jpg',
					'https://happypik.ru/wp-content/uploads/2019/09/foto-zaytsev11.jpg',
					'https://placepic.ru/wp-content/uploads/2019/04/s1200-9-2.jpg',
					'https://popugy.ru/wp-content/uploads/zayac-rusak-okraska.jpg',
					'https://placepic.ru/wp-content/uploads/2019/04/649-e1414684385806-1024x766.jpg',
					'https://placepic.ru/wp-content/uploads/2019/04/zayats-morda-ushi-lapi.jpg',
					'https://zelenyjmir.ru/wp-content/uploads/2017/06/Zayats-36.jpg',
					'https://www.syl.ru/misc/i/ai/383301/2498585.jpg',
					'https://get.pxhere.com/photo/nature-grass-wildlife-portrait-mammal-fauna-rabbit-hare-whiskers-animals-vertebrate-domestic-rabbit-rabits-and-hares-wood-rabbit-695117.jpg']
		embed=discord.Embed(title="Заяц! 🐇")
		embed.set_image(url=f"{random.choice(pictures)}")
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))