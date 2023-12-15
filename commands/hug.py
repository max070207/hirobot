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

	@commands.command(aliases=["hug", "обнять"])
	@commands.guild_only()
	async def __hug(self, ctx, member: discord.Member):
		status = check_category(str(ctx.guild.id), "RP")
		if status == 0:
			return
		gifs = ['https://media.tenor.com/images/bb67bef5f54d0191b7e2d3c1fd6e4bd3/tenor.gif',
				'https://media.tenor.com/images/a9bb4d55724484be94d13dd94721a8d9/tenor.gif',
				'https://media.tenor.com/images/52866345d463488b3425fb1068ac3d01/tenor.gif',
				'https://media.tenor.com/images/77ea5be350828ec04edcbe4865285a77/tenor.gif',
				'https://media.tenor.com/images/6083ba11631dd577bcc271268d010832/tenor.gif',
				'https://media.tenor.com/images/7265a624272e13d0950518a9654ce976/tenor.gif',
				'https://media.tenor.com/images/ca682cecd6bff521e400f984502f370c/tenor.gif',
				'https://media.tenor.com/images/f97e14429cf53cf3b822c9cea35375ef/tenor.gif',
				'https://media.tenor.com/images/9fe95432f2d10d7de2e279d5c10b9b51/tenor.gif',
				'https://media.tenor.com/images/15c39a7d6b03267941a87b24483ab696/tenor.gif',
				'https://media.tenor.com/images/778282e02d511fbc061e1439a5105c6f/tenor.gif',
				'https://media.tenor.com/images/8f44c083c55620c02f59c6bea378dca4/tenor.gif',
				'https://media.tenor.com/images/a9730f44f28d959abb4c5b31edc77de8/tenor.gif',
				'https://media.tenor.com/images/6d1a742c873d58af4c492903c79af623/tenor.gif',
				'https://media.tenor.com/images/73f2117d26096fbd804c739af0c06257/tenor.gif',
				'https://media.tenor.com/images/daed52a4ee85e276e1099ac77d1539c3/tenor.gif']
		if member == ctx.author:
			embed=discord.Embed(description="Самолюбие - не лучшая ваша черта", color=discord.Colour.blue())
			await ctx.send(embed=embed)
		else:
			embed=discord.Embed(description=f"**{member.name}**, тебя обнял(-а) **{ctx.author.name}**!", color=discord.Colour.blue())
			embed.set_image(url=f'{random.choice(gifs)}')
			await ctx.send(embed=embed)

	@__hug.error
	async def hug_error(self, ctx, error):
		with open('/root/bot/databases/prefixes.json', 'r') as f:
			data = json.load(f)
			p = data[str(ctx.guild.id)]
		if isinstance(error, commands.MissingRequiredArgument) or isinstance(error, commands.TooManyArguments) or isinstance(error, commands.BadArgument) or isinstance(error, commands.MemberNotFound) or isinstance(error, commands.UserNotFound) or isinstance(error, commands.MessageNotFound) or isinstance(error, commands.ChannelNotReadable) or isinstance(error, commands.ChannelNotFound)  or isinstance(error, commands.EmojiNotFound) or isinstance(error, commands.PartialEmojiConversionFailure) or isinstance(error, commands.MissingPermissions) or isinstance(error, commands.BotMissingPermissions) or isinstance(error, commands.BadUnionArgument) or isinstance(error, commands.ArgumentParsingError):
			embed=discord.Embed(title=f'Команда **"{p}hug" `||` "{p}обнять"**', description="**Обнять выбранного юзера**\n\n\n", color=discord.Color.blue(), timestamp=datetime.datetime.utcnow())
			embed.add_field(name="**Использование:**", value=f"`{p}hug <@Юзер>`", inline=False)
			embed.add_field(name=f"**Примеры:**\n`{p}hug @{ctx.guild.owner}`", value=":white_small_square: Обнять выбранного юзера", inline=False)
			embed.add_field(name=f"`{p}hug {ctx.guild.owner.id}`", value=":white_small_square: Обнять выбранного юзера по его id", inline=False)
			embed.set_footer(text=f'{self.bot.user.name}', icon_url=self.bot.user.avatar_url)
			await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))