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

async def get_message(bot, ctx, look_for, timeout):
	try:
		msg = await bot.wait_for(look_for, timeout=timeout, check=lambda message: message.author == ctx.author and message.channel == ctx.channel)
		if msg:
			await msg.delete()
			return msg
	except asyncio.TimeoutError:
		return False

class Command(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command(aliases=["embed", "эмбед"])
	@commands.has_permissions(manage_guild=True)
	@commands.guild_only()
	async def __embed(self, ctx):
		status = check_category(str(ctx.guild.id), "Utilities")
		if status == 0:
			return
		embed_color=discord.Embed(title="Укажите цвет панели:", description="**Внимание!**\nУкажите цвета типа **`hex`** без знака **`#`**\nПример: **`FFD700`**\nЕсли вы не хотите выбирать цвет, можете указать **`None`**")
		message1 = await ctx.send(embed=embed_color)
		embed=discord.Embed()
		message_color = await get_message(self.bot, ctx, 'message', 300)
		if message_color == False:
			embed=discord.Embed(description=f"Время истекло!", colour=discord.Color.red())
			await ctx.send(embed=embed)
			return
		if message_color.content != "None":
			msg = "0x" + message_color.content.lower()
			embed.color = int(msg, 0)
		await message1.delete()

		embed_title=discord.Embed(title="Укажите заголовок панели:", description="Если вы не хотите указывать заголовок, можете указать **`None`**")
		message2 = await ctx.send(embed=embed_title)
		message_title = await get_message(self.bot, ctx, 'message', 300)
		if message_title == False:
			embed=discord.Embed(description=f"Время истекло!", colour=discord.Color.red())
			await ctx.send(embed=embed)
			return
		if message_title.content != "None":
			embed.title = message_title.content
		await message2.delete()

		embed_description=discord.Embed(title="Укажите описание панели:", description="Если вы не хотите указывать описание, можете указать **`None`**")
		message11 = await ctx.send(embed=embed_description)
		message_description = await get_message(self.bot, ctx, 'message', 300)
		if message_description == False:
			embed=discord.Embed(description=f"Время истекло!", colour=discord.Color.red())
			await ctx.send(embed=embed)
			return
		if message_description.content != "None":
			embed.description = message_description.content
		await message11.delete()

		embed_author=discord.Embed(title="Укажите автора панели:", description="Если вы не хотите указывать автора, можете указать **`None`**")
		message3 = await ctx.send(embed=embed_author)
		message_author = await get_message(self.bot, ctx, 'message', 300)
		if message_author == False:
			embed=discord.Embed(description=f"Время истекло!", colour=discord.Color.red())
			await ctx.send(embed=embed)
			return
		if message_author.content != "None":
			embed_author_link=discord.Embed(title="Укажите ссылку на автора панели:", description="Если вы не хотите указывать ссылку на автора, можете указать **`None`**")
			message4 = await ctx.send(embed=embed_author_link)
			message_author_link = await get_message(self.bot, ctx, 'message', 300)
			if message_author_link == False:
				embed=discord.Embed(description=f"Время истекло!", colour=discord.Color.red())
				await ctx.send(embed=embed)
				return
			if message_author_link.content != "None":
				embed_author_icon=discord.Embed(title="Укажите ссылку на иконку автора панели:", description="Если вы не хотите указывать ссылку иконку на автора, можете указать **`None`**")
				message5 = await ctx.send(embed=embed_author_icon)
				message_author_icon = await get_message(self.bot, ctx, 'message', 300)
				if message_author_icon == False:
					embed=discord.Embed(description=f"Время истекло!", colour=discord.Color.red())
					await ctx.send(embed=embed)
					return
				if message_author_icon.content != "None":
					embed.set_author(name=message_author.content, url=message_author_link.content, icon_url=message_author_icon.content)
				else:
					embed.set_author(name=message_author.content, url=message_author_link.content)
				await message4.delete()
				await message5.delete()
			else:
				embed_author_icon=discord.Embed(title="Укажите ссылку на иконку автора панели:", description="Если вы не хотите указывать ссылку иконку на автора, можете указать **`None`**")
				message5 = await ctx.send(embed=embed_author_icon)
				message_author_icon = await get_message(self.bot, ctx, 'message', 300)
				if message_author_icon == False:
					embed=discord.Embed(description=f"Время истекло!", colour=discord.Color.red())
					await ctx.send(embed=embed)
					return
				if message_author_icon.content != "None":
					embed.set_author(name=message_author.content, icon_url=message_author_icon.content)
				else:
					embed.set_author(name=message_author.content)
				await message4.delete()
				await message5.delete()
		await message3.delete()

		embed_image=discord.Embed(title="Укажите ссылку на большую картинку для панели:", description="Если вы не хотите указывать ссылку на большую картинку, можете указать **`None`**")
		message6 = await ctx.send(embed=embed_image)
		message_image = await get_message(self.bot, ctx, 'message', 300)
		if message_image == False:
			embed=discord.Embed(description=f"Время истекло!", colour=discord.Color.red())
			await ctx.send(embed=embed)
			return
		if message_image.content != "None":
			embed.set_image(url=message_image.content)
		await message6.delete()

		embed_thumbnail=discord.Embed(title="Укажите ссылку на маленькую картинку для панели:", description="Если вы не хотите указывать ссылку на маленькую картинку, можете указать **`None`**")
		message7 = await ctx.send(embed=embed_thumbnail)
		message_thumnbnail = await get_message(self.bot, ctx, 'message', 300)
		if message_thumnbnail == False:
			embed=discord.Embed(description=f"Время истекло!", colour=discord.Color.red())
			await ctx.send(embed=embed)
			return
		if message_thumnbnail.content != "None":
			embed.set_thumbnail(url=message_thumnbnail.content)
		await message7.delete()

		embed_footer=discord.Embed(title="Укажите текст для нижней части панели:", description="Если вы не хотите указывать текст для нижней части панели, можете указать **`None`**")
		message8 = await ctx.send(embed=embed_footer)
		message_footer = await get_message(self.bot, ctx, 'message', 300)
		if message_footer == False:
			embed=discord.Embed(description=f"Время истекло!", colour=discord.Color.red())
			await ctx.send(embed=embed)
			return
		if message_footer.content != "None":
			embed_footer_icon_url=discord.Embed(title="Укажите ссылку на иконку для нижней части панели:", description="Если вы не хотите указывать ссылку на иконку для нижней части панели, можете указать **`None`**")
			message9 = await ctx.send(embed=embed_footer_icon_url)
			message_footer_icon = await get_message(self.bot, ctx, 'message', 300)
			if message_footer_icon == False:
				embed=discord.Embed(description=f"Время истекло!", colour=discord.Color.red())
				await ctx.send(embed=embed)
				return
			if message_footer_icon.content != "None":
				embed.set_footer(text=message_footer.content, icon_url=message_footer_icon.content)
			else:
				embed.set_footer(text=message_footer.content)
			await message9.delete()
		await message8.delete()


		embed_content=discord.Embed(title="Укажите текст, который будет написан вне панели:", description="Если вы не хотите указывать текст, можете указать **`None`**")
		message10 = await ctx.send(embed=embed_content)
		message_content = await get_message(self.bot, ctx, 'message', 300)
		if message_content == False:
			embed=discord.Embed(description=f"Время истекло!", colour=discord.Color.red())
			await ctx.send(embed=embed)
			return
		try:
			if message_content.content != "None":
				await ctx.send(content=message_content.content, embed=embed)
			else:
				await ctx.send(embed=embed)
		except Exception as e:
			await ctx.send(f"```{e}```")
		await message10.delete()

	@__embed.error
	async def embed_error(self, ctx, error):
		with open('/root/bot/databases/prefixes.json', 'r') as f:
			data = json.load(f)
			p = data[str(ctx.guild.id)]
		if isinstance(error, commands.MissingRequiredArgument) or isinstance(error, commands.TooManyArguments) or isinstance(error, commands.BadArgument) or isinstance(error, commands.MemberNotFound) or isinstance(error, commands.UserNotFound) or isinstance(error, commands.MessageNotFound) or isinstance(error, commands.ChannelNotReadable) or isinstance(error, commands.ChannelNotFound)  or isinstance(error, commands.EmojiNotFound) or isinstance(error, commands.PartialEmojiConversionFailure) or isinstance(error, commands.MissingPermissions) or isinstance(error, commands.BotMissingPermissions) or isinstance(error, commands.BadUnionArgument) or isinstance(error, commands.ArgumentParsingError):
			embed=discord.Embed(title=f'Команда **"{p}embed" `||` "{p}эмбед"**', description="**Бот повторит написанный вами текст с вашей конфигурацией**\n\n\n", color=discord.Color.blue(), timestamp=datetime.datetime.utcnow())
			embed.add_field(name="**Необходимые права:**", value="```MANAGE_GUILD```", inline=False)
			embed.add_field(name="**Использование:**", value=f"`{p}embed`", inline=False)
			embed.add_field(name=f"**Примеры:**\n`{p}embed`", value=":white_small_square: Бот повторит написанный Вами текст\n**Внимание!**\nДалее необходимо выполнить присланные ботом инструкции", inline=False)
			embed.set_footer(text=f'{self.bot.user.name}', icon_url=self.bot.user.avatar_url)
			await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))