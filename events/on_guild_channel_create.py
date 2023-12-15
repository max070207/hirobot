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

class Event(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_guild_channel_create(self, channel):
		with open('/root/bot/databases/audit_servers.json', 'r') as f:
			data = json.load(f)
		if str(channel.guild.id) in data:
			if "channel_create" in data[str(channel.guild.id)]:
				if data[str(channel.guild.id)]["channel_create"]["status"] == "on":
					cnl = self.bot.get_channel(data[str(channel.guild.id)]["channel_create"]["channel_id"])
					embed=discord.Embed(title=f"Канал был создан", description=f"Канал **{channel.name}**({channel.mention}) был создан", color=0x7cfc00, timestamp=datetime.datetime.utcnow())
					embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
					embed.set_footer(text=f"ID: {channel.id}")
					await cnl.send(embed=embed)
				else:
					return

def setup(bot):
	bot.add_cog(Event(bot))