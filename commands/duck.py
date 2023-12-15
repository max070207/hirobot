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

	@commands.command(aliases=["duck", "утка"])
	@commands.guild_only()
	async def __duck(self, ctx):
		status = check_category(str(ctx.guild.id), "Images")
		if status == 0:
			return
		pictures = ['https://cdn.pixabay.com/photo/2017/02/01/00/31/duck-2028587_1280.jpg',
					'https://cdn.pixabay.com/photo/2017/03/02/16/22/duck-2111721_960_720.jpg',
					'https://sklad.freeimg.ru/rsynced_images/drake-2028573_1280.jpg',
					'https://get.pxhere.com/photo/nature-grass-bird-animal-male-wildlife-beak-fauna-poultry-duck-goose-vertebrate-waterfowl-water-bird-mallard-canard-ducks-geese-and-swans-1199012.jpg',
					'https://7kyr.ru/wp-content/uploads/2015/08/selezen.jpg',
					'https://cepia.ru/images/u/pages/1476/9.jpg',
					'https://cdn.pixabay.com/photo/2016/12/07/18/16/duck-1890085_960_720.jpg',
					'https://placepic.ru/wp-content/uploads/2021/05/4694402.jpg',
					'https://my-fasenda.ru/wp-content/uploads/2020/09/%D1%83%D1%82%D0%BA%D0%B8.jpg',
					'https://get.pxhere.com/photo/bird-wildlife-beak-fowl-fauna-poultry-duck-vertebrate-waterfowl-water-bird-mallard-canard-ducks-geese-and-swans-137597.jpg']
		embed=discord.Embed(title="Утка! 🦆")
		embed.set_image(url=f"{random.choice(pictures)}")
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))