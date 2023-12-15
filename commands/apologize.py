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

	@commands.command(aliases=["apologize", "извиниться"])
	@commands.guild_only()
	async def __apologize(self, ctx):
		status = check_category(str(ctx.guild.id), "RP")
		if status == 0:
			return
		gifs = ['https://c.tenor.com/APIsjPJxtAUAAAAM/anime-sorry.gif',
			   'https://c.tenor.com/4s5VdBQUAj8AAAAM/imsorry-sorry.gif',
			   'https://c.tenor.com/VPrLvXeZEW4AAAAM/anime-sad-anime-pout.gif',
			   'https://c.tenor.com/EZsmE8l33TcAAAAM/anime-anime-cry.gif',
			   'https://c.tenor.com/6PMCyJTUgsgAAAAM/meirocho-iam.gif',
			   'https://c.tenor.com/d2ohcwGU2FkAAAAM/anime-beg.gif',
			   'https://c.tenor.com/J5o8KL1ktNoAAAAM/im-sorry-sad.gif',
			   'https://c.tenor.com/YTPLqiB6gLsAAAAM/sowwy-sorry.gif',
			   'https://c.tenor.com/i9UkjLlNlt4AAAAM/anime-sorry.gif']
		embed=discord.Embed(description=f"**{ctx.author.name}** извиняется", color=discord.Colour.blue())
		embed.set_image(url=f'{random.choice(gifs)}')
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))