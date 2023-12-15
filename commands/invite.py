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

	@commands.command(aliases=["invite", "пригласить"])
	async def __invite(self, ctx):
		embed=discord.Embed(title="Пригласить бота", color=discord.Color.blue())
		embed.add_field(name=f"Пригласить бота на свой сервер:", value=f"[Буп!](https://discord.com/api/oauth2/authorize?client_id=717753722268024833&permissions=8&scope=bot)", inline=False)
		embed.add_field(name=f"Сервер тех. поддержки бота:", value=f"[Бип!](https://discord.gg/YUzE6rB)", inline=False)
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))