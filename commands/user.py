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

	@commands.command(aliases=["user", "юзер"])
	@commands.guild_only()
	async def __user(self, ctx, user: discord.User):
		status = check_category(str(ctx.guild.id), "Utilities")
		if status == 0:
			return
		"""
		with open('/root/bot/databases/lvl.json', 'r') as f:
			users = json.load(f)
		"""
		emoji_online = self.bot.get_emoji(746038919249920020)
		emoji_idle = self.bot.get_emoji(746038147573481512)
		emoji_dnd = self.bot.get_emoji(746038248446492782)
		emoji_offline = self.bot.get_emoji(746038507595628625)
		emoji_mobile = self.bot.get_emoji(828277333298642994)
		emoji_computer = self.bot.get_emoji(828277519333195786)
		if user == None:
			user = ctx.author
		try:
			member = ctx.guild.get_member(user.id)
			if member.nick == None:
				name = member.name
			else:
				name = f"{member.name} || {member.nick}"
			if member.status == discord.Status.online:
				status = f"{emoji_online} Онлайн"
			elif member.status == discord.Status.idle:
				status = f"{emoji_idle} Не активен"
			elif member.status == discord.Status.dnd:
				status = f"{emoji_dnd} Не беспокоить"
			else:
				status = f"{emoji_offline} Оффлайн"
			if member.is_on_mobile() == True:
				emoji_device = emoji_mobile
				mobile = "Телефон"
			else:
				emoji_device = emoji_computer
				mobile = "Компьютер"
			embed=discord.Embed(title=f"Информация о пользователе {name}:", colour=discord.Color.blue(), timestamp=datetime.datetime.utcnow())
			embed.set_thumbnail(url=f'{member.avatar_url}')
			embed.add_field(name="Имя:", value=f'{member.name}#{member.discriminator}', inline=True)
			embed.add_field(name="ID:", value=f'{member.id}', inline=True)
			embed.add_field(name="Статус:", value=f'{status}', inline=False)
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
			embed.add_field(name="Устройство:", value=f'{emoji_device} {mobile}', inline=True)
			embed.add_field(name="\u200b", value="\u200b", inline=True)
			embed.add_field(name="Зарегистрировался:", value=f'{member.created_at.strftime("%d/%m/%Y %H:%M:%S")} UTC', inline=False)
			embed.add_field(name="Присоединился:", value=f'{member.joined_at.strftime("%d/%m/%Y %H:%M:%S")} UTC', inline=True)
			embed.add_field(name="\u200b", value="\u200b", inline=True)
			embed.add_field(name="Ролей:", value=f'{len(member.roles) - 1}', inline=False)
			embed.add_field(name="Высшая роль:", value=f'{member.top_role.mention}', inline=True)
			embed.add_field(name="\u200b", value="\u200b", inline=True)
			await ctx.send(embed=embed)
		except:
			embed=discord.Embed(title=f"Информация о пользователе {user.name}:", colour=discord.Color.blue(), timestamp=datetime.datetime.utcnow())
			embed.set_thumbnail(url=f'{user.avatar_url}')
			embed.add_field(name="Имя:", value=f'{user.name}#{user.discriminator}', inline=True)
			embed.add_field(name="ID:", value=f'{user.id}', inline=True)
			embed.add_field(name="Зарегистрировался:", value=f'{user.created_at.strftime("%d/%m/%Y %H:%M:%S")} UTC', inline=False)
			embed.add_field(name="\u200b", value="\u200b", inline=True)
			await ctx.send(embed=embed)
		"""
		async def get_lvl(users,user):
			try:
				lvl = users[user]["lvl"]
				embed.add_field(name="Уровень:", value=f'```python\n{lvl}```', inline=True)
			except KeyError:
				embed.add_field(name="Уровень:", value=f'```python\n0```', inline=True)
		await get_lvl(users,str(member.id))
		async def get_exp(users,user):
			try:
				exp = users[user]["exp"]
				lvl = users[user]["lvl"]
				embed.add_field(name="Опыт:", value=f'```python\n{exp}/{lvl ** 3 * 6 + 100}```', inline=True)
			except KeyError:
				embed.add_field(name="Опыт:", value=f'```python\n0/100```', inline=True)
		await get_exp(users,str(member.id))
		"""

	@__user.error
	async def user_error(self, ctx, error):
		with open('/root/bot/databases/prefixes.json', 'r') as f:
			data = json.load(f)
			p = data[str(ctx.guild.id)]
		if isinstance(error, commands.MissingRequiredArgument) or isinstance(error, commands.TooManyArguments) or isinstance(error, commands.BadArgument) or isinstance(error, commands.MemberNotFound) or isinstance(error, commands.UserNotFound) or isinstance(error, commands.MessageNotFound) or isinstance(error, commands.ChannelNotReadable) or isinstance(error, commands.ChannelNotFound)  or isinstance(error, commands.EmojiNotFound) or isinstance(error, commands.PartialEmojiConversionFailure) or isinstance(error, commands.MissingPermissions) or isinstance(error, commands.BotMissingPermissions) or isinstance(error, commands.BadUnionArgument) or isinstance(error, commands.ArgumentParsingError):
			embed=discord.Embed(title=f'Команда **"{p}user" `||` "{p}юзер"**', description="**Увидеть информацию о выбранном юзере**\n\n\n", color=discord.Color.blue(), timestamp=datetime.datetime.utcnow())
			embed.add_field(name="**Использование:**", value=f"`{p}user [@Юзер]`", inline=False)
			embed.add_field(name=f"**Примеры:**\n`{p}user`", value=f":white_small_square: Увидеть информацию о себе", inline=False)
			embed.add_field(name=f"`{p}user @{ctx.guild.owner}`", value=f":white_small_square: Увидеть информацию о выбранном юзере", inline=False)
			embed.set_footer(text=f'{self.bot.user.name}', icon_url=self.bot.user.avatar_url)
			await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))