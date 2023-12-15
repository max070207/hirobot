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

	@commands.command(aliases=["compliment", "похвалить"])
	@commands.guild_only()
	async def __compliment(self, ctx, member: discord.Member):
		status = check_category(str(ctx.guild.id), "RP")
		if status == 0:
			return
		gifs = ['https://c.tenor.com/XRCtdGIAWbsAAAAS/precure-hibiki.gif',
				'https://c.tenor.com/-SIywyATmagAAAAS/naruto-thumbsup.gif',
				'https://c.tenor.com/hp3yzLDp6d8AAAAM/makise-kurise-steins-gate.gif',
				'https://c.tenor.com/_LumrGir11AAAAAM/thumbs-up-good.gif',
				'https://c.tenor.com/KDu5g3XZyVYAAAAM/subaru-like.gif',
				'https://c.tenor.com/jEgWCr8PzV4AAAAM/lucky-star-cute.gif',
				'https://c.tenor.com/KgTaOloE588AAAAM/anime-like.gif']
		if member == ctx.author:
			embed=discord.Embed(description="Самолюбие - не лучшая ваша черта", color=discord.Colour.blue())
			await ctx.send(embed=embed)
		else:
			embed=discord.Embed(description=f"**{member.name}**, тебя похвалил(-а) **{ctx.author.name}**!", color=discord.Colour.blue())
			embed.set_image(url=f'{random.choice(gifs)}')
			await ctx.send(embed=embed)

	@__compliment.error
	async def compliment_error(self, ctx, error):
		with open('/root/bot/databases/prefixes.json', 'r') as f:
			data = json.load(f)
			p = data[str(ctx.guild.id)]
		if isinstance(error, commands.MissingRequiredArgument) or isinstance(error, commands.TooManyArguments) or isinstance(error, commands.BadArgument) or isinstance(error, commands.MemberNotFound) or isinstance(error, commands.UserNotFound) or isinstance(error, commands.MessageNotFound) or isinstance(error, commands.ChannelNotReadable) or isinstance(error, commands.ChannelNotFound)  or isinstance(error, commands.EmojiNotFound) or isinstance(error, commands.PartialEmojiConversionFailure) or isinstance(error, commands.MissingPermissions) or isinstance(error, commands.BotMissingPermissions) or isinstance(error, commands.BadUnionArgument) or isinstance(error, commands.ArgumentParsingError):
			embed=discord.Embed(title=f'Команда **"{p}compliment" `||` "{p}похвалить"**', description="**Похвалить выбранного юзера**\n\n\n", color=discord.Color.blue(), timestamp=datetime.datetime.utcnow())
			embed.add_field(name="**Использование:**", value=f"`{p}compliment <@Юзер>`", inline=False)
			embed.add_field(name=f"**Примеры:**\n`{p}compliment @{ctx.guild.owner}`", value=":white_small_square: Похвалить выбранного юзера", inline=False)
			embed.add_field(name=f"`{p}compliment {ctx.guild.owner.id}`", value=":white_small_square: Похвалить выбранного юзера по его id", inline=False)
			embed.set_footer(text=f'{self.bot.user.name}', icon_url=self.bot.user.avatar_url)
			await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))