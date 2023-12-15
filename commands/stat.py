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

class Command(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command(aliases=["stat", "стат"])
	@commands.guild_only()
	async def __stat(self, ctx):
		wait = self.bot.latency * 1000
		pythonVersion = platform.python_version()
		dpyVersion = discord.__version__
		serverCount = len(self.bot.guilds)
		channelCount = len(set(self.bot.get_all_channels()))
		memberCount = 0
		for guild in self.bot.guilds:
				memberCount += len(guild.members)
		embed=discord.Embed(title="Статистика", color=discord.Color.blue())
		embed.add_field(name=f"Серверов:", value=f"{serverCount}", inline=True)
		embed.add_field(name=f"Пользователей:", value=f"{memberCount}", inline=True)
		embed.add_field(name=f"Каналов:", value=f"{channelCount}", inline=True)
		embed.add_field(name=f"Python версия:", value=f"{pythonVersion}", inline=False)
		embed.add_field(name=f"Discord.py версия:", value=f"{dpyVersion}", inline=True)
		embed.add_field(name=f"Задержка:", value=f'{round(wait, 0)}мс', inline=False)
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))