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

	@commands.command(aliases=["star", "звезда"])
	@commands.guild_only()
	async def __star(self, ctx, member: discord.Member=None):
		status = check_category(str(ctx.guild.id), "RP")
		if status == 0:
			return
		if member == None:
			member = ctx.author
		if member == ctx.author:
			embed=discord.Embed(description=f"**{ctx.author.name}**, ты подарил(-а) себе ⭐️!", color=discord.Colour.blue())
			embed.set_image(url='https://images-ext-2.discordapp.net/external/i7QBYxdQgd0sul2vTGO3dh2XrLjME8oT3R5wH_m2xpo/https/imgur.com/aJVFhoD.jpg')
			await ctx.send(embed=embed)
		else:
			embed1=discord.Embed(description=f"**{member.name}**, ты получил(-а) звезду от **{ctx.author.name}**!", color=discord.Colour.blue())
			embed1.set_image(url='https://images-ext-2.discordapp.net/external/_qzdzvhht5QzhQLh7fQ5-EUZMYzQh1i9CAam4YWrJEk/https/imgur.com/QvBZUyu.jpg')
			await ctx.send(embed=embed1)

	@__star.error
	async def star_error(self, ctx, error):
		with open('/root/bot/databases/prefixes.json', 'r') as f:
			data = json.load(f)
			p = data[str(ctx.guild.id)]
		if isinstance(error, commands.MissingRequiredArgument) or isinstance(error, commands.TooManyArguments) or isinstance(error, commands.BadArgument) or isinstance(error, commands.MemberNotFound) or isinstance(error, commands.UserNotFound) or isinstance(error, commands.MessageNotFound) or isinstance(error, commands.ChannelNotReadable) or isinstance(error, commands.ChannelNotFound)  or isinstance(error, commands.EmojiNotFound) or isinstance(error, commands.PartialEmojiConversionFailure) or isinstance(error, commands.MissingPermissions) or isinstance(error, commands.BotMissingPermissions) or isinstance(error, commands.BadUnionArgument) or isinstance(error, commands.ArgumentParsingError):
			embed=discord.Embed(title=f'Команда **"{p}star" `||` "{p}звезда"**', description="**Подарить звезду выбранному юзеру**\n\n\n", color=discord.Color.blue(), timestamp=datetime.datetime.utcnow())
			embed.add_field(name="**Использование:**", value=f"`{p}star [@Юзер]`", inline=False)
			embed.add_field(name=f"**Примеры:**\n`{p}star`", value=":white_small_square: Подарить себе звезду", inline=False)
			embed.add_field(name=f"`{p}star @{ctx.guild.owner}`", value=":white_small_square: Подарить звезду выбранному юзеру", inline=False)
			embed.add_field(name=f"`{p}star {ctx.guild.owner.id}`", value=":white_small_square: Подарить звезду выбранному юзеру по его id", inline=False)
			embed.set_footer(text=f'{self.bot.user.name}', icon_url=self.bot.user.avatar_url)
			await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))