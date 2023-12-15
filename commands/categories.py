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

categories_list = ["Utilities", "Moderation", "RP", "Images", "Fun", "Mini-games"]

class Command(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command(aliases=["categories", "категории"])
	@commands.guild_only()
	@commands.has_permissions(administrator=True)
	async def __categories(self, ctx, status: str=None, category:str=None):
		emoji_note = self.bot.get_emoji(785095507122978836)
		emoji_yes = self.bot.get_emoji(785095546146652180)
		emoji_no = self.bot.get_emoji(785095586671230986)
		with open('/root/bot/databases/off_categories.json', 'r') as f:
			data = json.load(f)
		if category == None and status == None:
			if not str(ctx.guild.id) in data:
				data[str(ctx.guild.id)] = {}
			embed=discord.Embed(color=0x00FFFF, description=f"{emoji_yes} - Включено\n{emoji_no} - Выключено\n")
			for category in categories_list:
				if not category in data[str(ctx.guild.id)]:
					embed.description += f"\n**{category} ─︎** {emoji_yes}"
				elif data[str(ctx.guild.id)][category]["status"] == "on":
					embed.description += f"\n**{category} ─︎** {emoji_yes}"
				elif data[str(ctx.guild.id)][category]["status"] == "off":
					embed.description += f"\n**{category} ─︎** {emoji_no}"
			await ctx.send(embed=embed)
			return
		if status != "on":
			if status != "off":
				await ctx.send(f"Статус может быть только `on` или `off`!")
				return
		if not category in categories_list:
			await ctx.send(f"Категория `{category}` не обнаружена!")
			return
		async def update_data(data, guild):
			if not guild in data:
				data[guild] = {}
		async def change_status(ctx, data, guild, category, status):
			if not category in data[guild]:
				data[guild][category] = {}
				data[guild][category]["status"] = status
				embed=discord.Embed(title=f"{emoji_yes} Успешно!", color=0x00FFFF, description=f"Категории **`{category}`** присвоен статус **`{status}`**")
				await ctx.send(embed=embed)
			else:
				if status == "off":
					if data[guild][category]["status"] == "off":
						embed=discord.Embed(title=f"{emoji_note} Примечание", color=0x00FFFF, description=f"Категория **`{category}`** уже отключена")
						await ctx.send(embed=embed)
					elif data[guild][category]["status"] == "on":
						embed=discord.Embed(title=f"{emoji_yes} Успешно!", color=0x00FFFF, description=f"Категории **`{category}`** присвоен статус **`{status}`**")
						await ctx.send(embed=embed)
				elif status == "on":
					if data[guild][category]["status"] == "on":
						embed=discord.Embed(title=f"{emoji_note} Примечание", color=0x00FFFF, description=f"Категория **`{category}`** уже включена")
						await ctx.send(embed=embed)
					elif data[guild][category]["status"] == "off":
						embed=discord.Embed(title=f"{emoji_yes} Успешно!", color=0x00FFFF, description=f"Категории **`{category}`** присвоен статус **`{status}`**")
						await ctx.send(embed=embed)
				data[guild][category]["status"] = status
		await update_data(data, str(ctx.guild.id))
		await change_status(ctx, data, str(ctx.guild.id), category, status)
		with open('/root/bot/databases/off_categories.json', 'w') as f:
			json.dump(data,f,indent=4)

	@__categories.error
	async def categories_error(self, ctx, error):
		with open('/root/bot/databases/prefixes.json', 'r') as f:
			data = json.load(f)
			p = data[str(ctx.guild.id)]
		if isinstance(error, commands.MissingRequiredArgument) or isinstance(error, commands.TooManyArguments) or isinstance(error, commands.BadArgument) or isinstance(error, commands.MemberNotFound) or isinstance(error, commands.UserNotFound) or isinstance(error, commands.MessageNotFound) or isinstance(error, commands.ChannelNotReadable) or isinstance(error, commands.ChannelNotFound)  or isinstance(error, commands.EmojiNotFound) or isinstance(error, commands.PartialEmojiConversionFailure) or isinstance(error, commands.MissingPermissions) or isinstance(error, commands.BotMissingPermissions) or isinstance(error, commands.BadUnionArgument) or isinstance(error, commands.ArgumentParsingError):
			embed=discord.Embed(title=f'Команда **"{p}categories" `||` "{p}категории"**', description="**Отключить категории команд для контекстного сервера**\n\n\n", color=discord.Color.blue(), timestamp=datetime.datetime.utcnow())
			embed.add_field(name="**Необходимые права:**", value="```ADMINISTRATOR```", inline=False)
			embed.add_field(name="**Использование:**", value=f"`{p}categories [on | off] [Имя категории]`", inline=False)
			embed.add_field(name="**Доступные имена категорий:**", value=f"`Utilities`\n`Moderation`\n`RP`\n`Images`\n`Fun`\n`Mini-games`", inline=False)
			embed.add_field(name=f"**Примеры:**\n`{p}categories`", value=":white_small_square: Увидеть список включённых и отключённых категорий", inline=False)
			embed.add_field(name=f"`{p}categories off Moderation`", value=":white_small_square: Отключить категорию Модерация", inline=False)
			embed.set_footer(text=f'{self.bot.user.name}', icon_url=self.bot.user.avatar_url)
			await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))