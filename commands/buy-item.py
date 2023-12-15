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

def recieve_item_from_id(item_id:int):
	if item_id in range(1, 16):
		if item_id == 1:
			item_name = "Вилка"
			item_damage = 3
			item_cost = 100
		elif item_id == 2:
			item_name = "Дубинка"
			item_damage = 5
			item_cost = 450
		elif item_id == 3:
			item_name = "Кастет"
			item_damage = 8
			item_cost = 600
		elif item_id == 4:
			item_name = "Кухонный нож"
			item_damage = 10
			item_cost = 750
		elif item_id == 5:
			item_name = "Нож Бабочка"
			item_damage = 14
			item_cost = 1050
		elif item_id == 6:
			item_name = "Мачете"
			item_damage = 15
			item_cost = 1200
		elif item_id == 7:
			item_name = "Пистолет ТТ"
			item_damage = 17
			item_cost = 1350
		elif item_id == 8:
			item_name = "Пистолет Глок-17"
			item_damage = 20
			item_cost = 1500
		elif item_id == 9:
			item_name = "Револьер Taurus Raging Bull"
			item_damage = 22
			item_cost = 1650
		elif item_id == 10:
			item_name = "Автомат М16"
			item_damage = 26
			item_cost = 1950
		elif item_id == 11:
			item_name = "Снайп. винтовка ВСС \"Винторез\""
			item_damage = 30
			item_cost = 2250
		elif item_id == 12:
			item_name = "Автомат АК-12"
			item_damage = 33
			item_cost = 2400
		elif item_id == 13:
			item_name = "Гранатомёт 6Г30"
			item_damage = 35
			item_cost = 2550
		elif item_id == 14:
			item_name = "Гранатомёт РПГ-7"
			item_damage = 40
			item_cost = 2850
		elif item_id == 15:
			item_name = "Гранатомёт АГС-40"
			item_damage = 45
			item_cost = 3000
		return item_name, item_damage, item_cost
	elif item_id in range(16, 31):
		if item_id == 16:
			item_name = "Футболка"
			item_health = 10
			item_cost = 100
		elif item_id == 17:
			item_name = "Плащ"
			item_health = 15
			item_cost = 480
		elif item_id == 18:
			item_name = "Кожаная куртка"
			item_health = 25
			item_cost = 640
		elif item_id == 19:
			item_name = "Курта с металлическими пластинами"
			item_health = 38
			item_cost = 770
		elif item_id == 20:
			item_name = "Форма полиции с лёгким бронежилетом"
			item_health = 42
			item_cost = 930
		elif item_id == 21:
			item_name = "Бронежилет Modular Tactical Vest"
			item_health = 55
			item_cost = 1370
		elif item_id == 22:
			item_name = "Бронежилет Dragon Skin"
			item_health = 57
			item_cost = 1550
		elif item_id == 23:
			item_name = "Бронежилет БКЗ 6/3-6а"
			item_health = 65
			item_cost = 1660
		elif item_id == 24:
			item_name = "Экипировка \"Перехватчик\""
			item_health = 70
			item_cost = 1830
		elif item_id == 25:
			item_name = "Экипировка \"ФОРТ Росич\""
			item_health = 85
			item_cost = 2120
		elif item_id == 26:
			item_name = "Экипировка \"Сотник\""
			item_health = 90
			item_cost = 2260
		elif item_id == 27:
			item_name = "Экипировка NeoFelis"
			item_health = 94
			item_cost = 2440
		elif item_id == 28:
			item_name = "Экипировка Ariele"
			item_health = 105
			item_cost = 2580
		elif item_id == 29:
			item_name = "ЗСК ОРВ-2 \"Сокол\""
			item_health = 120
			item_cost = 2860
		elif item_id == 30:
			item_name = "ЗСК \"Заслон\""
			item_health = 125
			item_cost = 3030
		return item_name, item_health, item_cost
	elif item_id in range(31, 32):
		if item_id == 31:
			item_name = "Аптечка"
			item_heal = 20
			item_cost = 300
		return item_name, item_heal, item_cost

async def add_item(ctx, bot, user, item_id):
	emoji_coin = bot.get_emoji(828277358690959380)
	with open('/root/bot/databases/fight.json', 'r') as f:
		data = json.load(f)
	if not item_id in range(1, 32):
		emoji = bot.get_emoji(744165695662850170)
		embed=discord.Embed(title=f"{emoji} Ошибка!", description="Неверный ID предмета!", color=discord.Color.red())
		await ctx.send(embed=embed)
		return
	lvl = data[str(ctx.author.id)]["lvl"]
	if item_id in range(1, 16):
		if item_id > lvl:
			emoji = bot.get_emoji(744165695662850170)
			embed=discord.Embed(title=f"{emoji} Ошибка!", description=f"Недостаточно уровня для покупки!\nДля покупки нужен {item_id} уровень", color=discord.Color.red())
			await ctx.send(embed=embed)
			return
	elif item_id in range(16, 31):
		if (item_id - 15) > lvl:
			emoji = bot.get_emoji(744165695662850170)
			embed=discord.Embed(title=f"{emoji} Ошибка!", description=f"Недостаточно уровня для покупки!\nДля покупки нужен {item_id - 15} уровень", color=discord.Color.red())
			await ctx.send(embed=embed)
			return
	item = recieve_item_from_id(item_id)
	if not user in data:
		data[user] = {}
		data[user]["exp"] = 0
		data[user]["lvl"] = 1
		data[user]["money"] = 0
		data[user]["items"] = {}
	exp = data[user]["exp"]
	lvl = data[user]["lvl"]
	money = data[user]["money"]
	if item_id in range(1, 31):
		if str(item_id) in data[user]["items"]:
			emoji = bot.get_emoji(744165695662850170)
			embed=discord.Embed(title=f"{emoji} Ошибка!", description="Этот предмет уже куплен!", color=discord.Color.red())
			await ctx.send(embed=embed)
			return
	if money < item[2]:
		emoji = bot.get_emoji(744165695662850170)
		embed=discord.Embed(title=f"{emoji} Ошибка!", description="Недостаточно средств для покупки предмета!", color=discord.Color.red())
		await ctx.send(embed=embed)
		return
	if item_id in range(31, 32):
		if str(item_id) in data[user]["items"]:
			data[user]["items"][str(item_id)]["count"] += 1
		else:
			data[user]["items"][str(item_id)] = {}
			data[user]["items"][str(item_id)]["count"] = 1
			to_do = "heal"
			data[user]["items"][str(item_id)][to_do] = item[1]
		data[user]["exp"] += 50
		data[user]["money"] -= item[2]
	else:
		data[user]["items"][str(item_id)] = {}
		data[user]["items"][str(item_id)]["weared"] = False
		if item_id in range(1, 16):
			to_do = "damage"
		elif item_id in range(16, 31):
			to_do = "health"
		data[user]["items"][str(item_id)][to_do] = item[1]
		data[user]["exp"] += 50
		data[user]["money"] -= item[2]
		exp_end = lvl * 3 * 60 + 100
		if exp >= exp_end:
			data[user]["lvl"] = lvl + 1
			data[user]["money"] = money + 500
	with open('/root/bot/databases/fight.json', 'w') as f:
		json.dump(data,f,indent=4)
	embed=discord.Embed(title=f"Успешно!", description=f"Вы приобрели предмет **{item[0]}** за **{item[2]}** {emoji_coin}!", color=discord.Color.blue())
	await ctx.send(embed=embed)

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

	@commands.command(aliases=["buy-item", "купить-предмет"])
	@commands.guild_only()
	async def __buy_item(self, ctx, item_id: int):
		status = check_category(str(ctx.guild.id), "Mini-games")
		if status == 0:
			return
		await add_item(ctx, self.bot, str(ctx.author.id), item_id)

	@__buy_item.error
	async def buy_item_error(self, ctx, error):
		with open('/root/bot/databases/prefixes.json', 'r') as f:
			data = json.load(f)
			p = data[str(ctx.guild.id)]
		if isinstance(error, commands.MissingRequiredArgument) or isinstance(error, commands.TooManyArguments) or isinstance(error, commands.BadArgument) or isinstance(error, commands.MemberNotFound) or isinstance(error, commands.UserNotFound) or isinstance(error, commands.MessageNotFound) or isinstance(error, commands.ChannelNotReadable) or isinstance(error, commands.ChannelNotFound)  or isinstance(error, commands.EmojiNotFound) or isinstance(error, commands.PartialEmojiConversionFailure) or isinstance(error, commands.MissingPermissions) or isinstance(error, commands.BotMissingPermissions) or isinstance(error, commands.BadUnionArgument) or isinstance(error, commands.ArgumentParsingError):
			embed=discord.Embed(title=f'Команда **"{p}buy-item" `||` "{p}купить-предмет"**', description="**Купить выбранный предмет**\n\n\n", color=discord.Color.blue(), timestamp=datetime.datetime.utcnow())
			embed.add_field(name="**Использование:**", value=f"`{p}buy-item <item_id>`", inline=False)
			embed.add_field(name=f"**Примеры:**\n`{p}buy-item 1`", value=":white_small_square: Купить предмет с ID 1", inline=False)
			embed.set_footer(text=f'{self.bot.user.name}', icon_url=self.bot.user.avatar_url)
			await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))