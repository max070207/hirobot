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

	@commands.command(aliases=["reload", "перезагрузить"])
	@commands.guild_only()
	@commands.is_owner()
	async def __reload(self, ctx, typ: str, extension: str):
		try:
			if typ == "command":
				self.bot.unload_extension(f"commands.{extension}")
				self.bot.load_extension(f"commands.{extension}")
				await ctx.send(f"```{extension} cog reloaded```")
			elif typ == "event":
				self.bot.unload_extension(f"events.{extension}")
				self.bot.load_extension(f"events.{extension}")
				await ctx.send(f"```{extension} cog reloaded```")
		except Exception as e:
			await ctx.send(e)

def setup(bot):
	bot.add_cog(Command(bot))