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

	@commands.command(aliases=["authors", "авторы"])
	@commands.guild_only()
	async def __authors(self, ctx):
		legend = self.bot.get_user(520473539971776534)
		rick = self.bot.get_user(705886703172452423)
		johnoil = self.bot.get_user(445628494055997441)
		kus = self.bot.get_user(759050638885126144)
		embed=discord.Embed(title="Авторы", color=discord.Color.blue())
		embed.add_field(name="Владелец:", value=f"{legend} ({legend.mention})", inline=False)
		embed.add_field(name="Модератор [Сервер  тех. поддержки]:", value=f"{rick} ({rick.mention})", inline=False)
		embed.add_field(name="Модератор [Сервер  тех. поддержки]:", value=f"{johnoil} ({johnoil.mention})", inline=False)
		embed.add_field(name="Модератор [Сервер  тех. поддержки]:", value=f"{kus} ({kus.mention})", inline=False)
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))