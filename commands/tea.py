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

	@commands.command(aliases=["tea", "чай"])
	@commands.guild_only()
	async def __tea(self, ctx):
		status = check_category(str(ctx.guild.id), "RP")
		if status == 0:
			return
		gifs = ['https://media1.tenor.com/images/730ab3a10667838c866c8d50d159be68/tenor.gif?itemid=19983352',
				'https://media.tenor.com/images/c40f0b44e24d07bbffa8313e708b2008/tenor.gif',
				'https://media.tenor.com/images/68b3a09752b0cacb60c208f70e4b5011/tenor.gif',
				'https://media1.tenor.com/images/c79c9bd32807e3925be3627288238d4e/tenor.gif?itemid=15778933',
				'https://media.tenor.com/images/569fc9214da2937e494948c97c33f8f3/tenor.gif',
				'https://media1.tenor.com/images/d94029ff4bee5edbe381d2f72aa45155/tenor.gif?itemid=19740466']
		embed=discord.Embed(description=f"**{ctx.author.name}** пьёт чай", color=discord.Colour.blue())
		embed.set_image(url=f'{random.choice(gifs)}')
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))