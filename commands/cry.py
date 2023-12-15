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

	@commands.command(aliases=["cry", "заплакать"])
	@commands.guild_only()
	async def __cry(self, ctx):
		status = check_category(str(ctx.guild.id), "RP")
		if status == 0:
			return
		gifs = ['https://c.tenor.com/OfYt0T0tgCYAAAAM/anime-cry.gif',
				'https://c.tenor.com/q9V98YHPZX4AAAAM/anime-umaru.gif',
				'https://c.tenor.com/jTei9b9RH0wAAAAM/anime-sad.gif',
				'https://c.tenor.com/ZK3DOFspBAUAAAAM/akko-qq.gif',
				'https://c.tenor.com/dTgqu4CcSKEAAAAM/cry-sad.gif',
				'https://c.tenor.com/NMiID29TUvIAAAAM/hunter-x-hunter-gon-freecs.gif',
				'https://c.tenor.com/AawIsMGnR88AAAAM/llorar1-cry.gif',
				'https://c.tenor.com/otSAwjPqcJsAAAAM/sad-cry.gif']
		embed=discord.Embed(description=f"**{ctx.author.name}** плачет", color=discord.Colour.blue())
		embed.set_image(url=f'{random.choice(gifs)}')
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))