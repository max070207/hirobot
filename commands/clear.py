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

	@commands.command(aliases=["clear", "очистить"])
	@commands.guild_only()
	@commands.has_permissions(manage_messages = True)
	async def __clear(self, ctx, amount : int):
		status = check_category(str(ctx.guild.id), "Moderation")
		if status == 0:
			return
		if 0 < amount < 1001:
			await ctx.message.delete(delay=0)
			await ctx.channel.purge(limit=amount)
			emoji_yes = self.bot.get_emoji(785095546146652180)
			embed=discord.Embed(title=f"{emoji_yes} Успешно!", color=discord.Color.green(), description=f"Было очищено `{amount}` сообщений")
			await ctx.send(embed=embed)
		else:
			emoji_no = self.bot.get_emoji(744165695662850170)
			embed=discord.Embed(title=f"{emoji_no} Ошибка!", description=f"Значение не может быть меньше 1 или больше 1000!", colour=discord.Color.red())
			await ctx.send(embed=embed)

	@__clear.error
	async def clear_error(self, ctx, error):
		with open('/root/bot/databases/prefixes.json', 'r') as f:
			data = json.load(f)
			p = data[str(ctx.guild.id)]
		if isinstance(error, commands.MissingRequiredArgument) or isinstance(error, commands.TooManyArguments) or isinstance(error, commands.BadArgument) or isinstance(error, commands.MemberNotFound) or isinstance(error, commands.UserNotFound) or isinstance(error, commands.MessageNotFound) or isinstance(error, commands.ChannelNotReadable) or isinstance(error, commands.ChannelNotFound)  or isinstance(error, commands.EmojiNotFound) or isinstance(error, commands.PartialEmojiConversionFailure) or isinstance(error, commands.MissingPermissions) or isinstance(error, commands.BotMissingPermissions) or isinstance(error, commands.BadUnionArgument) or isinstance(error, commands.ArgumentParsingError):
			embed=discord.Embed(title=f'Команда **"{p}clear" `||` "{p}очистить"**', description="**Удалить выбранное количество сообщений в контекстном канале**\n\n\n", color=discord.Color.blue(), timestamp=datetime.datetime.utcnow())
			embed.add_field(name="**Необходимые права:**", value="```MANAGE_MESSAGES```", inline=False)
			embed.add_field(name="**Использование:**", value=f"`{p}clear <Число>`", inline=False)
			embed.add_field(name=f"**Примеры:**\n`{p}clear 5`", value=f":white_small_square: Удалить 5 сообщений в контекстном канале", inline=False)
			embed.set_footer(text=f'{self.bot.user.name}', icon_url=self.bot.user.avatar_url)
			await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))