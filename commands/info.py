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

VERSION = "6.5.0"

class Command(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command(aliases=["info", "инфо"])
	@commands.guild_only()
	async def __info(self, ctx):
		with open('/root/bot/databases/prefixes.json', 'r') as f:
			data = json.load(f)
			p = data[str(ctx.guild.id)]
		pythonVersion = platform.python_version()
		dpyVersion = discord.__version__
		embed=discord.Embed(title="Информация", color=discord.Color.blue())
		embed.add_field(name=f"Мой префикс: `{p}`", value=f"Пропиши команду `{p}help` для большей информации.", inline=False)
		embed.add_field(name="Бот создан:", value="03.06.2020", inline=False)
		embed.add_field(name="Версия бота:", value=VERSION, inline=False)
		embed.add_field(name="Мой создатель:", value="<@520473539971776534>",  inline=False)
		embed.add_field(name="Сервер тех. поддержки:", value="[Присоединиться](https://discord.gg/YUzE6rB)", inline=False)
		embed.add_field(name="Пригласить бота на свой сервер:", value="[Пригласить](https://discord.com/api/oauth2/authorize?client_id=717753722268024833&permissions=8&scope=bot)", inline=False)
		embed.add_field(name="Python версия:", value=f"{pythonVersion}", inline=False)
		embed.add_field(name="Discord.py версия:", value=f"{dpyVersion}")
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))