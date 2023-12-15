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

def check_category(guild, category):
	with open('/root/bot/databases/off_categories.json', 'r') as f:
		data = json.load(f)
	if not guild in data:
		data[guild] = {}
	if not category in data[guild]:
		return 1
	if data[guild][category]["status"] == "off":
		return 0
	else:
		return 1

class Command(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command(aliases=["channelinfo", "каналинфо"])
	@commands.guild_only()
	async def __channelinfo(self, ctx, channel: discord.TextChannel=None):
		status = check_category(str(ctx.guild.id), "Utilities")
		if status == 0:
			return
		if channel == None:
			channel = ctx.channel
		if channel.type == discord.ChannelType.text:
			cType = "Текстовый канал"
		elif channel.type == discord.ChannelType.voice:
			cType = "Голосовой канал"
		elif channel.type == discord.ChannelType.news:
			cType = "Новостной канал"
		elif channel.type == discord.ChannelType.store:
			cType = "Магазин"
		if channel.is_nsfw() == True:
			nsfw = "Да"
		else:
			nsfw = "Нет"
		if channel.is_news() == True:
			news = "Да"
		else:
			news = "Нет"
		members = len(channel.members)
		embed=discord.Embed(colour=discord.Color.blue())
		embed.add_field(name=f"Название канала:", value=f"{channel.name}({channel.mention})", inline=False)
		embed.add_field(name=f"Название сервера:", value=f"{ctx.guild.name}", inline=False)
		embed.add_field(name=f"Создан:", value=f"{channel.created_at.strftime('%d/%m/%Y %H:%M:%S')} UTC", inline=False)
		embed.add_field(name=f"Слоумод:", value=f"{channel.slowmode_delay}", inline=False)
		embed.add_field(name=f"Тип:", value=f"{cType}", inline=False)
		embed.add_field(name=f"Юзеры видящие канал:", value=f"{members}", inline=False)
		embed.add_field(name=f"NSFW?:", value=f"{nsfw}", inline=False)
		embed.add_field(name=f"Новостной?:", value=f"{news}", inline=False)
		embed.add_field(name=f"ID:", value=f"{channel.id}", inline=False)
		await ctx.send(embed=embed)

	@__channelinfo.error
	async def channelinfo_error(self, ctx, error):
		with open('/root/bot/databases/prefixes.json', 'r') as f:
			data = json.load(f)
			p = data[str(ctx.guild.id)]
		if isinstance(error, commands.MissingRequiredArgument) or isinstance(error, commands.TooManyArguments) or isinstance(error, commands.BadArgument) or isinstance(error, commands.MemberNotFound) or isinstance(error, commands.UserNotFound) or isinstance(error, commands.MessageNotFound) or isinstance(error, commands.ChannelNotReadable) or isinstance(error, commands.ChannelNotFound)  or isinstance(error, commands.EmojiNotFound) or isinstance(error, commands.PartialEmojiConversionFailure) or isinstance(error, commands.MissingPermissions) or isinstance(error, commands.BotMissingPermissions) or isinstance(error, commands.BadUnionArgument) or isinstance(error, commands.ArgumentParsingError):
			embed=discord.Embed(title=f'Команда **"{p}channelinfo" `||` "{p}каналинфо"**', description="**Увидеть информацию о выбранном канале**\n\n\n", color=discord.Color.blue(), timestamp=datetime.datetime.utcnow())
			embed.add_field(name="**Использование:**", value=f"`{p}channelinfo <#Канал>`", inline=False)
			embed.add_field(name=f"**Примеры:**\n`{p}channelinfo`", value=f":white_small_square: Увидеть информацию о контекстном канале", inline=False)
			embed.add_field(name=f"`{p}channelinfo #{ctx.channel}`", value=f":white_small_square: Увидеть информацию о выбранном канале", inline=False)
			embed.add_field(name=f"`{p}channelinfo #{ctx.channel.id}`", value=f":white_small_square: Увидеть информацию о выбранном канале по id", inline=False)
			embed.set_footer(text=f'{self.bot.user.name}', icon_url=self.bot.user.avatar_url)
			await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))