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

	@commands.command(aliases=["roleinfo", "рольинфо"])
	@commands.guild_only()
	async def __roleinfo(self, ctx, role: discord.Role):
		status = check_category(str(ctx.guild.id), "Utilities")
		if status == 0:
			return
		if role.hoist == True:
			hoist = "Да"
		else:
			hoist = "Нет"
		if role.mentionable == True:
			mentionable = "Да"
		else:
			mentionable = "Нет"
		if role.is_default() == True:
			default = "Да"
		else:
			default = "Нет"
		members = len(role.members)
		embed=discord.Embed(colour=discord.Color.blue())
		embed.add_field(name=f"Название роли:", value=f"{role.name}({role.mention})", inline=False)
		embed.add_field(name=f"Название сервера:", value=f"{role.guild}", inline=False)
		embed.add_field(name=f"Создана:", value=f"{role.created_at.strftime('%d/%m/%Y %H:%M:%S')} UTC", inline=False)
		embed.add_field(name=f"Участников с ролью:", value=f"{members}", inline=False)
		embed.add_field(name=f"Показывается отдельно?", value=f"{hoist}", inline=False)
		embed.add_field(name=f"Пингуется?:", value=f"{mentionable}", inline=False)
		embed.add_field(name=f"Дефолтная?:", value=f"{default}", inline=False)
		embed.add_field(name=f"ID:", value=f"{role.id}", inline=False)
		await ctx.send(embed=embed)

	@__roleinfo.error
	async def roleinfo_error(self, ctx, error):
		with open('/root/bot/databases/prefixes.json', 'r') as f:
			data = json.load(f)
			p = data[str(ctx.guild.id)]
		if isinstance(error, commands.MissingRequiredArgument) or isinstance(error, commands.TooManyArguments) or isinstance(error, commands.BadArgument) or isinstance(error, commands.MemberNotFound) or isinstance(error, commands.UserNotFound) or isinstance(error, commands.MessageNotFound) or isinstance(error, commands.ChannelNotReadable) or isinstance(error, commands.ChannelNotFound)  or isinstance(error, commands.EmojiNotFound) or isinstance(error, commands.PartialEmojiConversionFailure) or isinstance(error, commands.MissingPermissions) or isinstance(error, commands.BotMissingPermissions) or isinstance(error, commands.BadUnionArgument) or isinstance(error, commands.ArgumentParsingError):
			embed=discord.Embed(title=f'Команда **"{p}roleinfo" `||` "{p}рольинфо"**', description="**Увидеть информацию о выбранной роли**\n\n\n", color=discord.Color.blue(), timestamp=datetime.datetime.utcnow())
			embed.add_field(name="**Использование:**", value=f"`{p}roleinfo <@Роль>`", inline=False)
			embed.add_field(name=f"**Примеры:**\n`{p}roleinfo @{ctx.author.top_role.name}`", value=f":white_small_square: Увидеть информацию о выбранной роли", inline=False)
			embed.add_field(name=f"`{p}roleinfo {ctx.author.top_role.id}`", value=f":white_small_square: Увидеть информацию о выбранной роли по id", inline=False)
			embed.set_footer(text=f'{self.bot.user.name}', icon_url=self.bot.user.avatar_url)
			await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))