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
import nekos
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

	@commands.command(aliases=["smoke", "курить"])
	@commands.guild_only()
	async def __smoke(self, ctx):
		status = check_category(str(ctx.guild.id), "RP")
		if status == 0:
			return
		gifs = ['https://media1.tenor.com/images/2992fb9c44cdc817e6cbc0782fbc6276/tenor.gif?itemid=17324366',
				'https://media1.tenor.com/images/9b0512087948a11e7cdc058de72ac33b/tenor.gif?itemid=15630140',
				'https://media1.tenor.com/images/7bde0953487bacb0ae11990c0bf9681c/tenor.gif?itemid=17104895',
				'https://media1.tenor.com/images/0489b067e03c7e5a13d11d10a0095690/tenor.gif?itemid=14705180',
				'https://media1.tenor.com/images/f5c9686501a2a2cdd2397dffbe6554ae/tenor.gif?itemid=10174890',
				'https://media1.tenor.com/images/6372c4bf64b83c056c01cd05ba41aa3a/tenor.gif?itemid=16414439']
		embed=discord.Embed(description=f"**{ctx.author.name}** курит", color=discord.Colour.blue())
		embed.set_image(url=f'{random.choice(gifs)}')
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))