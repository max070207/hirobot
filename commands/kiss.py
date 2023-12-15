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

	@commands.command(aliases=["kiss", "поцеловать"])
	@commands.guild_only()
	async def __kiss(self, ctx, member: discord.Member=None):
		status = check_category(str(ctx.guild.id), "RP")
		if status == 0:
			return
		gifs = ['https://media1.tenor.com/images/ea9a07318bd8400fbfbd658e9f5ecd5d/tenor.gif?itemid=12612515',
				'https://media.tenor.com/images/26aaa1494b424854824019523c7ba631/tenor.gif',
				'https://media.tenor.com/images/912baa6ce415c3a783969c3e63a5b6b9/tenor.gif',
				'https://media.tenor.com/images/a75800a31f350c6a29ef2343931492b2/tenor.gif',
				'https://media.tenor.com/images/b020758888323338c874c549cbca5681/tenor.gif',
				'https://media.tenor.com/images/4b75a7e318cb515156bb7bfe5b3bbe6f/tenor.gif',
				'https://media.tenor.com/images/5f199a951a552d83e49c275d7505c2e6/tenor.gif',
				'https://media.tenor.com/images/dd777838018ab9e97c45ba34596bb8de/tenor.gif',
				'https://media.tenor.com/images/4b75a7e318cb515156bb7bfe5b3bbe6f/tenor.gif',
				'https://media.tenor.com/images/e11e607335c7e9e265d4dbbdbb2bfdf5/tenor.gif',
				'https://media.tenor.com/images/f2795e834ff4b9ed3c8ca6e1b21c3931/tenor.gif',
				'https://media.tenor.com/images/4e9c5f7f9a6008c1502e1c12eb5454f9/tenor.gif',
				'https://media.tenor.com/images/68d59bb29d7d8f7895ce385869989852/tenor.gif',
				'https://media.tenor.com/images/7b50048d76f76a8e5b3d8fc5a3fc6a21/tenor.gif',
				'https://media.tenor.com/images/9fb52dbfd3b7695ae50dfd00f5d241f7/tenor.gif']
		if member == None:
			member = ctx.author
		if member == ctx.author:
			embed=discord.Embed(description="Самолюбие - не лучшая ваша черта", color=discord.Colour.blue())
			await ctx.send(embed=embed)
		else:
			embed=discord.Embed(description=f"**{member.name}**, тебя поцеловал(-а) **{ctx.author.name}**!", color=discord.Colour.blue())
			embed.set_image(url=f'{random.choice(gifs)}')
			await ctx.send(embed=embed)

	@__kiss.error
	async def kiss_error(self, ctx, error):
		with open('/root/bot/databases/prefixes.json', 'r') as f:
			data = json.load(f)
			p = data[str(ctx.guild.id)]
		if isinstance(error, commands.MissingRequiredArgument) or isinstance(error, commands.TooManyArguments) or isinstance(error, commands.BadArgument) or isinstance(error, commands.MemberNotFound) or isinstance(error, commands.UserNotFound) or isinstance(error, commands.MessageNotFound) or isinstance(error, commands.ChannelNotReadable) or isinstance(error, commands.ChannelNotFound)  or isinstance(error, commands.EmojiNotFound) or isinstance(error, commands.PartialEmojiConversionFailure) or isinstance(error, commands.MissingPermissions) or isinstance(error, commands.BotMissingPermissions) or isinstance(error, commands.BadUnionArgument) or isinstance(error, commands.ArgumentParsingError):
			embed=discord.Embed(title=f'Команда **"{p}kiss" `||` "{p}поцеловать"**', description="**Поцеловать выбранного юзера**\n\n\n", color=discord.Color.blue(), timestamp=datetime.datetime.utcnow())
			embed.add_field(name="**Использование:**", value=f"`{p}kiss [@Юзер]`", inline=False)
			embed.add_field(name=f"**Примеры:**\n`{p}kiss`", value=":white_small_square: Поцеловать себя", inline=False)
			embed.add_field(name=f"`{p}kiss @{ctx.guild.owner}`", value=":white_small_square: Поцеловать выбранного юзера", inline=False)
			embed.add_field(name=f"`{p}kiss {ctx.guild.owner.id}`", value=":white_small_square: Поцеловать выбранного юзера по его id", inline=False)
			embed.set_footer(text=f'{self.bot.user.name}', icon_url=self.bot.user.avatar_url)
			await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))