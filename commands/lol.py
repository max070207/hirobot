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

	@commands.command(aliases=["lol", "лол"])
	@commands.guild_only()
	async def __lol(self, ctx):
		status = check_category(str(ctx.guild.id), "RP")
		if status == 0:
			return
		gifs = ['https://imgur.com/s6ooWXn.gif',
			   'https://imgur.com/WNUoj0T.gif',
			   'https://cdn.discordapp.com/attachments/717635575951392790/729267584922550323/171122_4692_1.gif',
			   'https://cdn.discordapp.com/attachments/717635575951392790/729268612694802472/171122_2546_1.gif',
			   'https://cdn.discordapp.com/attachments/717635575951392790/729318748905013348/171114_7474.gif',
			   'https://i.gifer.com/ZPwg.gif',
				]
		embed=discord.Embed(description=f"**{ctx.author.name}** смеётся!", color=discord.Colour.blue())
		embed.set_image(url=f'{random.choice(gifs)}')
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))