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
	async def on_member_remove(self, member):
		with open('/root/bot/databases/bye_servers.json', 'r') as f:
			data = json.load(f)
		if str(member.guild.id) in data:
			if data[str(member.guild.id)]["status"] == "on":
				gifs = ["https://media.tenor.com/images/251d736302c3dcdb755b9aa59174556d/tenor.gif",
						"https://media.tenor.com/images/8489d1bac66f45104779bd25b5997deb/tenor.gif",
						"https://media.tenor.com/images/824a5c6fb0eff4de202d0cd4da1e6692/tenor.gif",
						"https://media1.tenor.com/images/aa6d975cb5318886db35f27f692d09d3/tenor.gif?itemid=144954610",
						"https://media1.tenor.com/images/cd5ee7f75777c5483cdbd403c97c7405/tenor.gif?itemid=8138029",
						"https://media1.tenor.com/images/4342f7f6a01cfe0a274cda0b63e096ff/tenor.gif?itemid=16856505",
						"https://media.tenor.com/images/408866348c81c86db4c33a6daff2e6eb/tenor.gif"]
				channel = self.bot.get_channel(data[str(member.guild.id)]["channel_id"])
				embed=discord.Embed(title=f"Пока...", description=f"Количество участников: {len(member.guild.members)}", color=discord.Color.red(), timestamp=datetime.datetime.utcnow())
				embed.set_author(name=member.name, icon_url=member.avatar_url)
				embed.set_thumbnail(url=member.avatar_url)
				embed.set_image(url=f'{random.choice(gifs)}')
				embed.set_footer(text=f'{member.guild.name}', icon_url=member.guild.icon_url)
				await channel.send(embed=embed)
		with open('/root/bot/databases/audit_servers.json', 'r') as f:
			data = json.load(f)
		if str(member.guild.id) in data:
			if "member_remove" in data[str(member.guild.id)]:
				if data[str(member.guild.id)]["member_remove"]["status"] == "on":
					channel = self.bot.get_channel(data[str(member.guild.id)]["member_remove"]["channel_id"])
					embed=discord.Embed(title=f"Пользователь **{member.name}** покинул сервер", description=f"Количество участников: {len(member.guild.members)}", color=discord.Color.red(), timestamp=datetime.datetime.utcnow())
					embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar_url)
					await channel.send(embed=embed)
				else:
					return

def setup(bot):
	bot.add_cog(Event(bot))