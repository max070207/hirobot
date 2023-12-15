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

	@commands.command(aliases=["punch", "ударить"])
	@commands.guild_only()
	async def __punch(self, ctx, member: discord.Member=None):
		status = check_category(str(ctx.guild.id), "RP")
		if status == 0:
			return
		gifs = ['https://media.tenor.com/images/00a3cca756b4bbae191ac33ccc6d7bcf/tenor.gif',
				'https://media.tenor.com/images/9c14d2d5dd918471954e5946166f3632/tenor.gif',
				'https://media.tenor.com/images/8a79543998d6878be573aab94ae86456/tenor.gif',
				'https://media.tenor.com/images/eb379f98c7ced6d43a16e78dc25ae864/tenor.gif',
				'https://media.tenor.com/images/bef50761d75e855c95cb94139c8c292f/tenor.gif',
				'https://media.tenor.com/images/b11c79cf158d8c9bd6e721676b06ad73/tenor.gif',
				'https://media.tenor.com/images/2162843deef9dda23eff63dc4b32dabc/tenor.gif',
				'https://media.tenor.com/images/5b668436338971d42469d7348a5340e5/tenor.gif',
				'https://media.tenor.com/images/bdd77613427552c73ba0a7ba82b21787/tenor.gif',
				'https://media.tenor.com/images/359a3a05dbde06a89cdcf494ad62bb5d/tenor.gif',
				'https://media.tenor.com/images/04f62b7819a22210c0ba411ddb2636a5/tenor.gif',
				'https://media.tenor.com/images/fc6b5d5e1c9de50273ca8c0ae003829f/tenor.gif',
				'https://i.imgur.com/4yIN8Y4.gif',
				'https://i.imgur.com/Oqg8FnR.gif']
		if member == None:
			member = ctx.author
		if member == ctx.author:
			embed=discord.Embed(description="Самолюбие - не лучшая ваша черта", color=discord.Colour.blue())
			await ctx.send(embed=embed)
		else:
			embed=discord.Embed(description=f"**{member.name}**, тебя ударил(-а) **{ctx.author.name}**!", color=discord.Colour.blue())
			embed.set_image(url=f'{random.choice(gifs)}')
			await ctx.send(embed=embed)

	@__punch.error
	async def punch_error(self, ctx, error):
		with open('/root/bot/databases/prefixes.json', 'r') as f:
			data = json.load(f)
			p = data[str(ctx.guild.id)]
		if isinstance(error, commands.MissingRequiredArgument) or isinstance(error, commands.TooManyArguments) or isinstance(error, commands.BadArgument) or isinstance(error, commands.MemberNotFound) or isinstance(error, commands.UserNotFound) or isinstance(error, commands.MessageNotFound) or isinstance(error, commands.ChannelNotReadable) or isinstance(error, commands.ChannelNotFound)  or isinstance(error, commands.EmojiNotFound) or isinstance(error, commands.PartialEmojiConversionFailure) or isinstance(error, commands.MissingPermissions) or isinstance(error, commands.BotMissingPermissions) or isinstance(error, commands.BadUnionArgument) or isinstance(error, commands.ArgumentParsingError):
			embed=discord.Embed(title=f'Команда **"{p}punch" `||` "{p}ударить"**', description="**Ударить выбранного юзера**\n\n\n", color=discord.Color.blue(), timestamp=datetime.datetime.utcnow())
			embed.add_field(name="**Использование:**", value=f"`{p}punch [@Юзер]`", inline=False)
			embed.add_field(name=f"**Примеры:**\n`{p}punch`", value=":white_small_square: Ударить себя", inline=False)
			embed.add_field(name=f"`{p}punch @{ctx.guild.owner}`", value=":white_small_square: Ударить выбранного юзера", inline=False)
			embed.add_field(name=f"`{p}punch {ctx.guild.owner.id}`", value=":white_small_square: Ударить выбранного юзера по его id", inline=False)
			embed.set_footer(text=f'{self.bot.user.name}', icon_url=self.bot.user.avatar_url)
			await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))