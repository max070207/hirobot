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

	@commands.command(aliases=["look", "наблюдать"])
	@commands.guild_only()
	async def __look(self, ctx):
		status = check_category(str(ctx.guild.id), "RP")
		if status == 0:
			return
		gifs = ['https://media.tenor.com/images/ca9c28a30d955512c5fd2916291a57a8/tenor.gif',
				'https://media.tenor.com/images/4e83c94d3649bce9a135b4bffe4b4bcc/tenor.gif',
				'https://media1.tenor.com/images/25c519228f732ec2824a7a679b78eed2/tenor.gif?itemid=13281436',
				'https://media.tenor.com/images/13c902007b142dee504fa8939fe3634d/tenor.gif']
		embed=discord.Embed(description=f"**{ctx.author.name}** наблюдает", color=discord.Colour.blue())
		embed.set_image(url=f'{random.choice(gifs)}')
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))