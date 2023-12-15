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

def crop(pfp, s):
	w, h = pfp.size
	k = w / s[0] - h / s[1]
	if k > 0: pfp = pfp.crop(((w - h) / 2, 0, (w + h) / 2, h))
	elif k < 0: pfp = pfp.crop((0, (h - w) / 2, w, (h + w) / 2))
	return pfp.resize(s, Image.ANTIALIAS)

class Event(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_message(self, message):
		with open('/root/bot/databases/prefixes.json', 'r') as f:
			data = json.load(f)

		if not str(message.guild.id) in data:
			data[str(message.guild.id)] = "h!"

		with open('/root/bot/databases/prefixes.json', 'w') as f:
			json.dump(data,f,indent=4)

		if message.content == "<@717753722268024833>":

			with open('/root/bot/databases/prefixes.json', 'r') as f:
				data = json.load(f)

			if str(message.guild.id) in data:
				prefix = data[str(message.guild.id)]
			else:
				async def update_data(data,guild,prefix):
					data[guild] = prefix

				await update_data(data,str(message.guild.id),str("h!"))

				with open('/root/bot/databases/prefixes.json', 'w') as f:
					json.dump(data,f,indent=4)
				prefix = 'h!'
			await message.channel.send(f"Мой префикс: `{prefix}`")
		with open('/root/bot/databases/off_leveling.json', 'r') as file:
			switch = json.load(file)

		if message.guild.id == 379768693519024139:
			if message.channel.id == 688473461852733481:
				size = (256, 256)
				img = Image.open("/root/bot/supports/white.png")
				draw = ImageDraw.Draw(img)
				av = ctx.author.avatar_url_as(size=1024)
				data = BytesIO(await av.read())
				pfp = Image.open(data)
				pfp = crop(pfp, size)
				pfp = img.paste(pfp, (0,0))
				img.save('/root/bot/supports/welcome_card_edit.png')
				with open('/root/bot/supports/welcome_card_edit.png', 'rb') as image:
					f = image.read()
					b = bytearray(f)
				ava = bytes(str(img), "UTF-8")
				channel = self.bot.get_channel(825997579928993792)
				webhook = await channel.create_webhook(name=message.author.name, avatar=b)
				await webhook.send(message.content)
				await webhook.delete()
"""
		with open('/root/bot/databases/lvl.json', 'r') as f:
			users = json.load(f)

		async def update_data(switch,guild,users,user):
			if guild in switch:
				if switch[guild]["status"] == "off":
					return
			if not user in users:
				users[user] = {}
				users[user]["exp"] = 0
				users[user]["lvl"] = 1
				users[user]["last_message"] = 0
		async def add_exp(switch,guild,users,user,exp):
			if guild in switch:
				if switch[guild]["status"] == "off":
					return
			if message.author.bot == True:
				return
			if message.channel.type == discord.ChannelType.text or discord.ChannelType.news or discord.ChannelType.store:
				if time.time() - users[user]["last_message"] > 30:
					users[user]["exp"] += exp
					users[user]["last_message"] = time.time()
				else:
					return
			else:
				return
		async def add_lvl(switch,guild,users,user):
			if guild in switch:
				if switch[guild]["status"] == "off":
					return
			emoji_giveaway = self.bot.get_emoji(772830814017683486)
			exp = users[user]["exp"]
			lvl = users[user]["lvl"]
			exp_end = lvl ** 3 * 6 + 100
			if exp >= exp_end:
				users[user]["lvl"] = lvl + 1
				lvl_end = users[user]["lvl"]
				embed=discord.Embed(title="Новый уровень", description=f"**{message.author.mention}**, поздравляю тебя с новым **{lvl_end}** уровнем! {emoji_giveaway}", colour=discord.Color.blue(), timestamp=datetime.datetime.utcnow())
				try:
					await message.channel.send(embed=embed)
				except:
					pass
		try:
			await update_data(switch,str(message.guild.id),users,str(message.author.id))
		except:
			pass
		try:
			await add_exp(switch,str(message.guild.id),users,str(message.author.id),random.randint(10,15))
		except:
			pass
		try:
			await add_lvl(switch,str(message.guild.id),users,str(message.author.id))
		except:
			pass
		with open('/root/bot/databases/lvl.json', 'w') as f:
			json.dump(users,f,indent=4)
"""

def setup(bot):
	bot.add_cog(Event(bot))