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

	@commands.command(aliases=["frog", "лягушка"])
	@commands.guild_only()
	async def __frog(self, ctx):
		status = check_category(str(ctx.guild.id), "Images")
		if status == 0:
			return
		pictures = ['https://dogcatdog.ru/wp-content/uploads/d/d/c/ddc68b1d4f2571119b3277be49fbba81.jpg',
					'https://demotivation.ru/wp-content/uploads/2020/07/Frogs_Water_545686_2048x2732-scaled.jpg',
					'https://proprikol.ru/wp-content/uploads/2020/09/kartinki-lyagushki-17.jpg',
					'https://bugaga.ru/uploads/posts/2016-11/1480074689_lyagushki-tanto-yensena-28.jpg',
					'https://get.pxhere.com/photo/water-nature-animal-pond-wildlife-green-frog-toad-amphibian-garden-close-fauna-vertebrate-creature-frogs-garden-pond-lacerta-water-frog-bullfrog-ranidae-emydidae-lacertidae-743843.jpg',
					'https://proprikol.ru/wp-content/uploads/2020/09/kartinki-lyagushki-52.jpg',
					'https://photocentra.ru/images/main35/356714_main.jpg',
					'https://proprikol.ru/wp-content/uploads/2020/09/kartinki-lyagushki-38.jpg',
					'https://million-wallpapers.ru/wallpapers/5/17/506145212308241/zelenaya-lyagushka-s-oranzhevymi-glazami.jpg',
					'http://s2.fotokto.ru/photo/full/312/3124562.jpg']
		embed=discord.Embed(title="Лягушка! 🐸")
		embed.set_image(url=f"{random.choice(pictures)}")
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))