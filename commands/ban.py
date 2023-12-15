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

	@commands.command(aliases=["ban", "бан"])
	@commands.guild_only()
	@commands.has_permissions(ban_members = True)
	async def __ban(self, ctx, member:discord.Member, delete_message_days=None, *, reason=None):
		status = check_category(str(ctx.guild.id), "Moderation")
		if status == 0:
			return
		try:
			membot = ctx.guild.get_member(self.bot.user.id)
			memctx = ctx.guild.get_member(ctx.author.id)
			member = ctx.guild.get_member(member.id)
			try:
				delete_message_days = int(delete_message_days)
			except:
				pass
			if type(delete_message_days) != type(ctx.author.id):
				reason = delete_message_days
				delete_message_days = 0
			else:
				if 0 > delete_message_days > 8:
					reason = delete_message_days
					delete_message_days = 0
			if member == ctx.message.author:
				emoji_no = self.bot.get_emoji(744165695662850170)
				embed=discord.Embed(title=f"{emoji_no} Ошибка!", description=f"Вы не можете забанить себя!", colour=discord.Color.red())
				await ctx.send(embed=embed)
				return
			if member.bot:
				emoji_no = self.bot.get_emoji(744165695662850170)
				embed=discord.Embed(title=f"{emoji_no} Ошибка!", description=f"Не надо банить ботов <3", colour=discord.Color.red())
				await ctx.send(embed=embed)
				return
			if reason == None:
				reason = "Причина отсутствует"
			if member.top_role.position >= membot.top_role.position:
				emoji_no = self.bot.get_emoji(744165695662850170)
				embed=discord.Embed(colour=discord.Color.red())
				embed.add_field(name=f"{emoji_no} Ошибка!", value=f"Я не могу забанить этого юзера, так как его роль выше моей роли!", inline=False)
				await ctx.send(embed=embed)
				return
			if memctx.top_role.position <= member.top_role.position:
				emoji_no = self.bot.get_emoji(744165695662850170)
				embed=discord.Embed(colour=discord.Color.red())
				embed.add_field(name=f"{emoji_no} Ошибка!", value=f"Я не могу забанить этого юзера, так как твоя роль выше или равна его роли!", inline=False)
				await ctx.send(embed=embed)
				return
			await ctx.guild.ban(user=member, reason=reason, delete_message_days=delete_message_days)
			await member.send(f"Вы были забанены на сервере **{ctx.guild.name}** по причине: **{reason}**")
			embed = discord.Embed(title='Бан', colour=discord.Color.red())
			embed.set_author(name=member.name, icon_url=member.avatar_url)
			embed.add_field(name=f'Забаненный юзер: {member.name}', value=f'По причине: **{reason}**')
			embed.set_footer(text=f'Был забанен модератором {ctx.author.name}', icon_url=ctx.author.avatar_url)
			await ctx.send(embed=embed)
		except Exception as e:
			channel = self.bot.get_channel(870742823203373086)
			embed=discord.Embed(title="Ошибка! ```h!ban```", description=f"`{str(e)}`", color=discord.Color.red(), timestamp=datetime.datetime.utcnow())
			embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
			embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)
			await channel.send(embed=embed)
	@__ban.error
	async def ban_error(self, ctx, error):
		with open('/root/bot/databases/prefixes.json', 'r') as f:
			data = json.load(f)
			p = data[str(ctx.guild.id)]
		if isinstance(error, commands.MissingRequiredArgument) or isinstance(error, commands.TooManyArguments) or isinstance(error, commands.BadArgument) or isinstance(error, commands.MemberNotFound) or isinstance(error, commands.UserNotFound) or isinstance(error, commands.MessageNotFound) or isinstance(error, commands.ChannelNotReadable) or isinstance(error, commands.ChannelNotFound)  or isinstance(error, commands.EmojiNotFound) or isinstance(error, commands.PartialEmojiConversionFailure) or isinstance(error, commands.MissingPermissions) or isinstance(error, commands.BotMissingPermissions) or isinstance(error, commands.BadUnionArgument) or isinstance(error, commands.ArgumentParsingError):
			embed=discord.Embed(title=f'Команда **"{p}ban" `||` "{p}бан"**', description="**Забанить выбранного юзера**\n\n\n", color=discord.Color.blue(), timestamp=datetime.datetime.utcnow())
			embed.add_field(name="**Необходимые права:**", value="```BAN_MEMBERS```", inline=False)
			embed.add_field(name="**Использование:**", value=f"`{p}ban <@Юзер> [Причина]`", inline=False)
			embed.add_field(name=f"**Примеры:**\n`{p}ban @{ctx.guild.owner}`", value=f":white_small_square: Забанить выбранного юзера без причины", inline=False)
			embed.add_field(name=f"`{p}ban @{ctx.guild.owner} Ведёт себя провокационно!`", value=f":white_small_square: Забанить выбранного юзера с причиной", inline=False)
			embed.add_field(name=f"`{p}ban {ctx.guild.owner.id} Ведёт себя провокационно!`", value=f":white_small_square: Забанить выбранного юзера по id с причиной", inline=False)
			embed.set_footer(text=f'{self.bot.user.name}', icon_url=self.bot.user.avatar_url)
			await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))