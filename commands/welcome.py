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

	@commands.command(aliases=["welcome", "приветствия"])
	@commands.guild_only()
	@commands.has_permissions(administrator=True)
	async def __welcome(self, ctx, status:str, channel_id:int=None):
		emoji_yes = self.bot.get_emoji(785095546146652180)
		with open('/root/bot/databases/welcome_servers.json', 'r') as f:
			data = json.load(f)
		if status != "on":
			if status != "off":
				await ctx.send(f"Статус может быть только `on` или `off`!")
				return
		if channel_id != None:
			cid = channel_id
		else:
			if not str(ctx.guild.id) in data:
				data[str(ctx.guild.id)] = {}
			if not "channel_id" in data[str(ctx.guild.id)]:
				await ctx.send(f"Вы забыли указать id канала для отправки сообщений!")
				return
			else:
				cid = data[str(ctx.guild.id)]["channel_id"]
		if not self.bot.get_channel(cid) in ctx.guild.text_channels:
			await ctx.send(f"Такого канала не существует!")
			return
		async def update_data(data, guild):
			if not guild in data:
				data[guild] = {}
		async def change_status(ctx, data, guild, status):
			data[guild]["status"] = status
			data[guild]["channel_id"] = cid
			channel = self.bot.get_channel(cid)
			embed=discord.Embed(title=f"{emoji_yes} Успешно!", color=0x00FFFF, description=f"Приветственным сообщениям присвоен статус **`{status}`**.\nКанал для приветствий: {channel.mention}")
			await ctx.send(embed=embed)
		await update_data(data, str(ctx.guild.id))
		await change_status(ctx, data, str(ctx.guild.id), status)
		with open('/root/bot/databases/welcome_servers.json', 'w') as f:
			json.dump(data,f,indent=4)

	@__welcome.error
	async def welcome_error(self, ctx, error):
		with open('/root/bot/databases/prefixes.json', 'r') as f:
			data = json.load(f)
			p = data[str(ctx.guild.id)]
		if isinstance(error, commands.MissingRequiredArgument) or isinstance(error, commands.TooManyArguments) or isinstance(error, commands.BadArgument) or isinstance(error, commands.MemberNotFound) or isinstance(error, commands.UserNotFound) or isinstance(error, commands.MessageNotFound) or isinstance(error, commands.ChannelNotReadable) or isinstance(error, commands.ChannelNotFound)  or isinstance(error, commands.EmojiNotFound) or isinstance(error, commands.PartialEmojiConversionFailure) or isinstance(error, commands.MissingPermissions) or isinstance(error, commands.BotMissingPermissions) or isinstance(error, commands.BadUnionArgument) or isinstance(error, commands.ArgumentParsingError):
			embed=discord.Embed(title=f'Команда **"{p}welcome" `||` "{p}приветствия"**', description="**Отключить или включить приветствия для вашего сервера**\n\n\n", color=discord.Color.blue(), timestamp=datetime.datetime.utcnow())
			embed.add_field(name="**Необходимые права:**", value="```ADMINISTRATOR```", inline=False)
			embed.add_field(name="**Использование:**", value=f"`{p}welcome <on | off> [Канал_айди]`", inline=False)
			embed.add_field(name=f"**Примеры:**\n`{p}welcome on 742412216309121077`", value=":white_small_square: Включить приветствия в канале", inline=False)
			embed.add_field(name=f"`{p}welcome off`", value=":white_small_square: Отключить приветствия", inline=False)
			embed.set_footer(text=f'{self.bot.user.name}', icon_url=self.bot.user.avatar_url)
			await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))