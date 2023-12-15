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

	@commands.command(aliases=["panic", "паниковать"])
	@commands.guild_only()
	async def __panic(self, ctx):
		status = check_category(str(ctx.guild.id), "RP")
		if status == 0:
			return
		gifs = ['https://media.tenor.com/images/b662acdf67c17ff904c7cbf9b1c87113/tenor.gif',
				'https://media.tenor.com/images/3d71e67d3f8fb854fc79cbaf9deee7c5/tenor.gif',
				'https://media.tenor.com/images/f36ff89fd0f78f9e6d3d4a27cf3095fe/tenor.gif',
				'https://media.tenor.com/images/554a7dce3d1efa300944cd9842e209ab/tenor.gif',
				'https://media.tenor.com/images/c583f2e73e29c3cbf939f7c5e1709113/tenor.gif']
		embed=discord.Embed(description=f"**{ctx.author.name}** паникует", color=discord.Colour.blue())
		embed.set_image(url=f'{random.choice(gifs)}')
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))