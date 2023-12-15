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

	@commands.command(aliases=["unban", "разбан"])
	@commands.guild_only()
	@commands.has_permissions(manage_guild = True)
	async def __unban(self, ctx, *, member):
		status = check_category(str(ctx.guild.id), "Moderation")
		if status == 0:
			return
		try:
			print(3)
			banned_users = await ctx.guild.bans()
			print(5)
			try:
				member = int(member)
				print(6)
				for ban_entry in banned_users:
					user = ban_entry.user
					if user.id == member:
						await ctx.guild.unban(user)
						await ctx.message.add_reaction("✅")
						print(7)
						return
			except:
				print(8)
				try:
					member_name, member_discriminator = member.split('#')
					print(9)
				except Exception as e:
					print(10)
					emoji_no = self.bot.get_emoji(744165695662850170)
					embed=discord.Embed(title=f"{emoji_no} Ошибка!", description=f"Пользователь не найден!", colour=discord.Color.red())
					await ctx.send(embed=embed)
					print(1)
					print(e)
					print(member)
					return
				print(11)
				for ban_entry in banned_users:
					user = ban_entry.user
					if (user.name, user.discriminator) == (member_name, member_discriminator):
						await ctx.guild.unban(user)
						await ctx.message.add_reaction("✅")
						print(12)
						return
				else:
					print(13)
					emoji_no = self.bot.get_emoji(744165695662850170)
					embed=discord.Embed(title=f"{emoji_no} Ошибка!", description=f"Пользователь не найден!", colour=discord.Color.red())
					await ctx.send(embed=embed)
					print(2)
					print((user.name, user.discriminator))
					print((member_name, member_discriminator))
		except Exception as e:
			print(14)
			channel = self.bot.get_channel(870742823203373086)
			embed=discord.Embed(title="Ошибка! ```h!unban```", description=f"`{str(e)}`", color=discord.Color.red(), timestamp=datetime.datetime.utcnow())
			embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
			embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)
			await channel.send(embed=embed)

	@__unban.error
	async def unban_error(self, ctx, error):
		with open('/root/bot/databases/prefixes.json', 'r') as f:
			data = json.load(f)
			p = data[str(ctx.guild.id)]
		if isinstance(error, commands.MissingRequiredArgument) or isinstance(error, commands.TooManyArguments) or isinstance(error, commands.BadArgument) or isinstance(error, commands.MemberNotFound) or isinstance(error, commands.UserNotFound) or isinstance(error, commands.MessageNotFound) or isinstance(error, commands.ChannelNotReadable) or isinstance(error, commands.ChannelNotFound)  or isinstance(error, commands.EmojiNotFound) or isinstance(error, commands.PartialEmojiConversionFailure) or isinstance(error, commands.MissingPermissions) or isinstance(error, commands.BotMissingPermissions) or isinstance(error, commands.BadUnionArgument) or isinstance(error, commands.ArgumentParsingError):
			embed=discord.Embed(title=f'Команда **"{p}unban" `||` "{p}разбан"**', description="**Разбанить выбранного юзера**\n\n\n", color=discord.Color.blue(), timestamp=datetime.datetime.utcnow())
			embed.add_field(name="**Необходимые права:**", value="```MANAGE_GUILD```", inline=False)
			embed.add_field(name="**Использование:**", value=f"`{p}unban <Юзер>`", inline=False)
			embed.add_field(name=f"**Примеры:**\n`{p}unban {ctx.guild.owner}`", value=f":white_small_square: Разбанить выбранного юзера", inline=False)
			embed.set_footer(text=f'{self.bot.user.name}', icon_url=self.bot.user.avatar_url)
			await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))