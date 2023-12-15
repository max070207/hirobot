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

	@commands.command(aliases=["smell", "понюхать"])
	@commands.guild_only()
	async def __smell(self, ctx, member: discord.Member):
		status = check_category(str(ctx.guild.id), "RP")
		if status == 0:
			return
		gifs = ['https://c.tenor.com/wHMAF-t9a_sAAAAM/sniff-anime.gif',
				'https://c.tenor.com/ppaZYw55uusAAAAM/anime-stink.gif',
				'https://c.tenor.com/rP3XMYGBlVAAAAAM/anime-ew.gif',
				'https://c.tenor.com/t_yiRkS2xDwAAAAM/mike-zacharias-zacharius.gif']
		if member == ctx.author:
			embed=discord.Embed(description="Самолюбие - не лучшая ваша черта", color=discord.Colour.blue())
			await ctx.send(embed=embed)
		else:
			embed=discord.Embed(description=f"**{member.name}**, тебя понюхал(-а) **{ctx.author.name}**!", color=discord.Colour.blue())
			embed.set_image(url=f'{random.choice(gifs)}')
			await ctx.send(embed=embed)

	@__smell.error
	async def smell_error(self, ctx, error):
		with open('/root/bot/databases/prefixes.json', 'r') as f:
			data = json.load(f)
			p = data[str(ctx.guild.id)]
		if isinstance(error, commands.MissingRequiredArgument) or isinstance(error, commands.TooManyArguments) or isinstance(error, commands.BadArgument) or isinstance(error, commands.MemberNotFound) or isinstance(error, commands.UserNotFound) or isinstance(error, commands.MessageNotFound) or isinstance(error, commands.ChannelNotReadable) or isinstance(error, commands.ChannelNotFound)  or isinstance(error, commands.EmojiNotFound) or isinstance(error, commands.PartialEmojiConversionFailure) or isinstance(error, commands.MissingPermissions) or isinstance(error, commands.BotMissingPermissions) or isinstance(error, commands.BadUnionArgument) or isinstance(error, commands.ArgumentParsingError):
			embed=discord.Embed(title=f'Команда **"{p}smell" `||` "{p}понюхать"**', description="**Понюхать выбранного юзера**\n\n\n", color=discord.Color.blue(), timestamp=datetime.datetime.utcnow())
			embed.add_field(name="**Использование:**", value=f"`{p}smell <@Юзер>`", inline=False)
			embed.add_field(name=f"**Примеры:**\n`{p}smell @{ctx.guild.owner}`", value=":white_small_square: Понюхать выбранного юзера", inline=False)
			embed.add_field(name=f"`{p}smell {ctx.guild.owner.id}`", value=":white_small_square: Понюхать выбранного юзера по его id", inline=False)
			embed.set_footer(text=f'{self.bot.user.name}', icon_url=self.bot.user.avatar_url)
			await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))