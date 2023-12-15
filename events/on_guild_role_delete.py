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
	async def on_guild_role_delete(self, role):
		with open('/root/bot/databases/audit_servers.json', 'r') as f:
			data = json.load(f)
		if str(role.guild.id) in data:
			if "role_delete" in data[str(role.guild.id)]:
				if data[str(role.guild.id)]["role_delete"]["status"] == "on":
					channel = self.bot.get_channel(data[str(role.guild.id)]["role_delete"]["channel_id"])
					embed=discord.Embed(title=f"Роль была удалена", description=f"Роль **{role.name}** была удалена", color=0xdc143c, timestamp=datetime.datetime.utcnow())
					embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
					embed.set_footer(text=f"ID: {role.id}")
					await channel.send(embed=embed)
				else:
					return

def setup(bot):
	bot.add_cog(Event(bot))