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
	async def on_message_delete(self, message):
		with open('/root/bot/databases/audit_servers.json', 'r') as f:
			data = json.load(f)
		if str(message.guild.id) in data:
			if "message_delete" in data[str(message.guild.id)]:
				if data[str(message.guild.id)]["message_delete"]["status"] == "on":
					try:
						if len(message.content) >= 1024:
							message_content = "Я не могу воспроизвести это сообщение, поскольку оно содержит больше 1024 символов :("
						else:
							message_content = message.content
						channel = self.bot.get_channel(data[str(message.guild.id)]["message_delete"]["channel_id"])
						embed=discord.Embed(title=f"Сообщение было удалено", color=0xdc143c, timestamp=datetime.datetime.utcnow())
						embed.add_field(name="Удалённое сообщение:", value=message_content, inline=False)
						embed.add_field(name="Автор:", value=message.author.name, inline=False)
						embed.add_field(name="Канал:", value=message.channel.name, inline=False)
						embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)
						embed.set_footer(text=f"ID: {message.id}")
						await channel.send(embed=embed)
					except:
						pass
				else:
					return

def setup(bot):
	bot.add_cog(Event(bot))