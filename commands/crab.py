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

	@commands.command(aliases=["crab", "краб"])
	@commands.guild_only()
	async def __crab(self, ctx):
		status = check_category(str(ctx.guild.id), "Images")
		if status == 0:
			return
		pictures = ['http://komotoz.ru/photo/images/photo_krabov/photo_krabov_03.jpg',
					'https://kartinkin.com/uploads/posts/2021-03/1616081183_31-p-krab-krasivie-foto-32.jpg',
					'https://million-wallpapers.ru/wallpapers/1/62/498819246687812/krasnyj-krab.jpg',
					'https://moi-akvarium.ru/wp-content/uploads/2020/04/Krab-vampir.jpg',
					'https://wallpapershome.ru/images/pages/pic_h/10150.jpg',
					'https://i.ytimg.com/vi/Ct2akSsUZ3g/hqdefault.jpg',
					'https://get.pxhere.com/photo/nature-ocean-food-insect-biology-seafood-colorful-shellfish-fauna-crab-invertebrate-crustacean-legs-sea-life-creepy-amazon-marine-biology-ocypodidae-decapoda-animal-source-foods-fiddler-crab-dungeness-crab-939080.jpg',
					'https://demotivation.ru/wp-content/uploads/2021/02/2048x1365_811218_www.ArtFile.ru_.jpg',
					'https://get.pxhere.com/photo/sea-food-seafood-empty-shellfish-crab-invertebrate-crustacean-arthropod-king-crab-ocypodidae-decapoda-animal-source-foods-dungeness-crab-american-lobster-homarus-spiny-lobster-freshwater-crab-1038219.jpg',
					'https://i.pinimg.com/originals/b1/1e/46/b11e4648ed5b9a510e4ae135572884f1.jpg']
		embed=discord.Embed(title="Краб! 🦀")
		embed.set_image(url=f"{random.choice(pictures)}")
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))