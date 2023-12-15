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

	@commands.command(aliases=["kick", "кик"])
	@commands.guild_only()
	@commands.has_permissions(kick_members = True)
	async def __kick(self, ctx, member:discord.Member, *, reason=None):
		status = check_category(str(ctx.guild.id), "Moderation")
		if status == 0:
			return
		membot = ctx.guild.get_member(self.bot.user.id)
		memctx = ctx.guild.get_member(ctx.author.id)
		emoji_no = self.bot.get_emoji(744165695662850170)
		if member == ctx.message.author:
			embed=discord.Embed(title=f"{emoji_no} Ошибка!", description=f"Вы не можете кикнуть себя!", colour=discord.Color.red())
			await ctx.send(embed=embed)
			return
		if reason == None:
			reason = "Причина отсутствует"
		if member.top_role.position >= membot.top_role.position:
			embed=discord.Embed(title=f"{emoji_no} Ошибка!", description=f"Я не могу кикнуть этого юзера, так как его роль выше моей роли!", colour=discord.Color.red())
			await ctx.send(embed=embed)
			return
		if memctx.top_role.position <= member.top_role.position:
			embed=discord.Embed(title=f"{emoji_no} Ошибка!", description=f"Я не могу кикнуть этого юзера, так как твоя роль выше или равна его роли!", colour=discord.Color.red())
			await ctx.send(embed=embed)
			return
		await ctx.guild.kick(member, reason=reason)
		await member.send(f"Вы были кикнуты с сервера **{ctx.guild.name}** по причине: **{reason}**")
		embed = discord.Embed(title='Кик', colour=discord.Color.red())
		embed.set_author(name=member.name, icon_url=member.avatar_url)
		embed.add_field(name=f'Кикнутый юзер: {member.name}', value=f'По причине: **{reason}**')
		embed.set_footer(text=f'Был кикнут модератором {ctx.author.name}', icon_url=ctx.author.avatar_url)
		await ctx.send(embed=embed)

	@__kick.error
	async def kick_error(self, ctx, error):
		with open('/root/bot/databases/prefixes.json', 'r') as f:
			data = json.load(f)
			p = data[str(ctx.guild.id)]
		if isinstance(error, commands.MissingRequiredArgument) or isinstance(error, commands.TooManyArguments) or isinstance(error, commands.BadArgument) or isinstance(error, commands.MemberNotFound) or isinstance(error, commands.UserNotFound) or isinstance(error, commands.MessageNotFound) or isinstance(error, commands.ChannelNotReadable) or isinstance(error, commands.ChannelNotFound)  or isinstance(error, commands.EmojiNotFound) or isinstance(error, commands.PartialEmojiConversionFailure) or isinstance(error, commands.MissingPermissions) or isinstance(error, commands.BotMissingPermissions) or isinstance(error, commands.BadUnionArgument) or isinstance(error, commands.ArgumentParsingError):
			embed=discord.Embed(title=f'Команда **"{p}kick" `||` "{p}кик"**', description="**Кикнуть выбранного юзера**\n\n\n", color=discord.Color.blue(), timestamp=datetime.datetime.utcnow())
			embed.add_field(name="**Необходимые права:**", value="```KICK_MEMBERS```", inline=False)
			embed.add_field(name="**Использование:**", value=f"`{p}kick <@Юзер> [Причина]`", inline=False)
			embed.add_field(name=f"**Примеры:**\n`{p}kick @{ctx.guild.owner}`", value=f":white_small_square: Кикнуть выбранного юзера без причины", inline=False)
			embed.add_field(name=f"`{p}kick @{ctx.guild.owner} Ведёт себя провокационно!`", value=f":white_small_square: Кикнуть выбранного юзера с причиной", inline=False)
			embed.add_field(name=f"`{p}kick {ctx.guild.owner.id} Ведёт себя провокационно!`", value=f":white_small_square: Кикнуть выбранного юзера по id с причиной", inline=False)
			embed.set_footer(text=f'{self.bot.user.name}', icon_url=self.bot.user.avatar_url)
			await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))