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

	@commands.command(aliases=["status", "статус"])
	@commands.guild_only()
	async def __status(self, ctx, member: discord.Member=None):
		status = check_category(str(ctx.guild.id), "Utilities")
		if status == 0:
			return
		if member == None:
			member = ctx.message.author
		embed=discord.Embed(title="Статусы", color=discord.Color.blue())
		if member.activity == None:
			activity = "-"
		else:
			activity = member.activity
			if activity.type == discord.ActivityType.playing:
				embed.add_field(name="Играет в:", value=f"{activity.name}", inline=True)
			elif activity.type == discord.ActivityType.streaming:
				embed.add_field(name=f"Стримит на {activity.platform}:", value=f"[{activity.name}]({activity.url})", inline=True)
			elif activity.type == discord.ActivityType.listening:
				embed.add_field(name=f"Слушает:", value=f"{activity.name}", inline=True)
			elif activity.type == discord.ActivityType.watching:
				embed.add_field(name=f"Смотрит:", value=f"{activity.name}", inline=True)
			else:
				embed.add_field(name="Пользовательский статус:", value=f'{activity.name}', inline=True)
		await ctx.send(embed=embed)

	@__status.error
	async def status_error(self, ctx, error):
		with open('/root/bot/databases/prefixes.json', 'r') as f:
			data = json.load(f)
			p = data[str(ctx.guild.id)]
		if isinstance(error, commands.MissingRequiredArgument) or isinstance(error, commands.TooManyArguments) or isinstance(error, commands.BadArgument) or isinstance(error, commands.MemberNotFound) or isinstance(error, commands.UserNotFound) or isinstance(error, commands.MessageNotFound) or isinstance(error, commands.ChannelNotReadable) or isinstance(error, commands.ChannelNotFound)  or isinstance(error, commands.EmojiNotFound) or isinstance(error, commands.PartialEmojiConversionFailure) or isinstance(error, commands.MissingPermissions) or isinstance(error, commands.BotMissingPermissions) or isinstance(error, commands.BadUnionArgument) or isinstance(error, commands.ArgumentParsingError):
			embed=discord.Embed(title=f'Команда **"{p}status" `||` "{p}статус"**', description="**Увидеть статус выбранного юзера**\n\n\n", color=discord.Color.blue(), timestamp=datetime.datetime.utcnow())
			embed.add_field(name="**Использование:**", value=f"`{p}status <@Юзер>`", inline=False)
			embed.add_field(name=f"**Примеры:**\n`{p}status @{ctx.guild.owner}`", value=":white_small_square: Увидеть статус выбранного юзера", inline=False)
			embed.add_field(name=f"`{p}status {ctx.guild.owner.id}`", value=":white_small_square: Увидеть статус выбранного юзера по его id", inline=False)
			embed.set_footer(text=f'{self.bot.user.name}', icon_url=self.bot.user.avatar_url)
			await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))