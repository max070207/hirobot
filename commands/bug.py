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

class Command(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command(aliases=["bug", "баг"])
	@commands.guild_only()
	async def __bug(self, ctx, *, bug):
		channel = self.bot.get_channel(803620761184370688)
		embed=discord.Embed()
		embed.add_field(name="Баг", value=f"{bug}", inline=False)
		embed.set_footer(text=f'Баг был найден пользователем {ctx.author}({ctx.author.id})', icon_url = ctx.author.avatar_url)
		await channel.send(embed=embed)
		await ctx.message.add_reaction("✅")

	@__bug.error
	async def bug_error(self, ctx, error):
		with open('/root/bot/databases/prefixes.json', 'r') as f:
			data = json.load(f)
			p = data[str(ctx.guild.id)]
		if isinstance(error, commands.MissingRequiredArgument) or isinstance(error, commands.TooManyArguments) or isinstance(error, commands.BadArgument) or isinstance(error, commands.MemberNotFound) or isinstance(error, commands.UserNotFound) or isinstance(error, commands.MessageNotFound) or isinstance(error, commands.ChannelNotReadable) or isinstance(error, commands.ChannelNotFound)  or isinstance(error, commands.EmojiNotFound) or isinstance(error, commands.PartialEmojiConversionFailure) or isinstance(error, commands.MissingPermissions) or isinstance(error, commands.BotMissingPermissions) or isinstance(error, commands.BadUnionArgument) or isinstance(error, commands.ArgumentParsingError):
			embed=discord.Embed(title=f'Команда **"{p}bug" `||` "{p}баг"**', description="**Послать информацию о найденном баге**\n\n\n", color=discord.Color.blue(), timestamp=datetime.datetime.utcnow())
			embed.add_field(name="**Использование:**", value=f"`{p}bug <Баг>`", inline=False)
			embed.add_field(name=f"**Примеры:**\n`{p}bug Команда бота не работает`", value=f":white_small_square: Послать информацию о найденном баге", inline=False)
			embed.set_footer(text=f'{self.bot.user.name}', icon_url=self.bot.user.avatar_url)
			await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))