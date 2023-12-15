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

	@commands.command(aliases=["pat", "погладить"])
	@commands.guild_only()
	async def __pat(self, ctx, member: discord.Member=None):
		status = check_category(str(ctx.guild.id), "RP")
		if status == 0:
			return
		gifs = ['https://media.tenor.com/images/ad8357e58d35c1d63b570ab7e587f212/tenor.gif',
				'https://media.tenor.com/images/bb4471bdc56bb2cf355338059d9fe4a0/tenor.gif',
				'https://media.tenor.com/images/40f454db8d7ee7ccad8998479fbabe69/tenor.gif',
				'https://media.tenor.com/images/e549c61c9bc3d8defdb0559b358b92a7/tenor.gif',
				'https://media.tenor.com/images/3739a516b2f49bdd4b4667f0db7d3a48/tenor.gif',
				'https://media.tenor.com/images/da8431374a530ae516c0cc8f966d1c2b/tenor.gif',
				'https://media.tenor.com/images/a58b340308475e34e324ea437bb40641/tenor.gif',
				'https://media.tenor.com/images/69fb17b3eafe27df334f9f873473d531/tenor.gif',
				'https://media.tenor.com/images/943a52d38d896bda734a6396b1ffca89/tenor.gif',
				'https://media.tenor.com/images/87fc4ab2abde188093f9eb0d42698be2/tenor.gif',
				'https://media.tenor.com/images/b4c1dccb1c11ab8e1e8c1b7f969dfec5/tenor.gif',
				'https://media.tenor.com/images/19c555af496d14808aa5d9bd8277c937/tenor.gif',
				'https://media.tenor.com/images/a671268253717ff877474fd019ef73e9/tenor.gif',
				'https://media.tenor.com/images/6cace20a510db73d9051f301c8707b4e/tenor.gif',
				'https://media.tenor.com/images/89440731dab7b31691c9e035b86c5e62/tenor.gif']
		if member == None:
			member = ctx.author
		if member == ctx.author:
			embed=discord.Embed(description="Самолюбие - не лучшая ваша черта", color=discord.Colour.blue())
			await ctx.send(embed=embed)
		else:
			embed=discord.Embed(description=f"**{member.name}**, тебя погладил(-а) **{ctx.author.name}**!", color=discord.Colour.blue())
			embed.set_image(url=f'{random.choice(gifs)}')
			await ctx.send(embed=embed)

	@__pat.error
	async def pat_error(self, ctx, error):
		with open('/root/bot/databases/prefixes.json', 'r') as f:
			data = json.load(f)
			p = data[str(ctx.guild.id)]
		if isinstance(error, commands.MissingRequiredArgument) or isinstance(error, commands.TooManyArguments) or isinstance(error, commands.BadArgument) or isinstance(error, commands.MemberNotFound) or isinstance(error, commands.UserNotFound) or isinstance(error, commands.MessageNotFound) or isinstance(error, commands.ChannelNotReadable) or isinstance(error, commands.ChannelNotFound)  or isinstance(error, commands.EmojiNotFound) or isinstance(error, commands.PartialEmojiConversionFailure) or isinstance(error, commands.MissingPermissions) or isinstance(error, commands.BotMissingPermissions) or isinstance(error, commands.BadUnionArgument) or isinstance(error, commands.ArgumentParsingError):
			embed=discord.Embed(title=f'Команда **"{p}pat" `||` "{p}погладить"**', description="**Погладить выбранного юзера**\n\n\n", color=discord.Color.blue(), timestamp=datetime.datetime.utcnow())
			embed.add_field(name="**Использование:**", value=f"`{p}pat [@Юзер]`", inline=False)
			embed.add_field(name=f"**Примеры:**\n`{p}pat`", value=":white_small_square: Погладить себя", inline=False)
			embed.add_field(name=f"`{p}pat @{ctx.guild.owner}`", value=":white_small_square: Погладить выбранного юзера", inline=False)
			embed.add_field(name=f"`{p}pat {ctx.guild.owner.id}`", value=":white_small_square: Погладить выбранного юзера по его id", inline=False)
			embed.set_footer(text=f'{self.bot.user.name}', icon_url=self.bot.user.avatar_url)
			await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))