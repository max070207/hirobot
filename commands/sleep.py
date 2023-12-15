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

	@commands.command(aliases=["sleep", "спать"])
	@commands.guild_only()
	async def __sleep(self, ctx):
		status = check_category(str(ctx.guild.id), "RP")
		if status == 0:
			return
		gifs = ['https://media.tenor.com/images/a73553b8ace1398eadfb0031f6613b86/tenor.gif',
				'https://media.tenor.com/images/2fe8733129b953c779bbdf80a3a141a4/tenor.gif',
				'https://media.tenor.com/images/780e4cba49678f3dc553b88f1e3e0708/tenor.gif',
				'https://media.tenor.com/images/0a5cca428c321853b52eb7fe08169dae/tenor.gif',
				'https://media.tenor.com/images/9bef625db38856933776df9a4c2dac04/tenor.gif']
		embed=discord.Embed(description=f"**{ctx.author.name}** спит", color=discord.Colour.blue())
		embed.set_image(url=f'{random.choice(gifs)}')
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))