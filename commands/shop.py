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

	@commands.command(aliases=["shop", "магазин"])
	@commands.guild_only()
	async def __shop(self, ctx, screen: int=None):
		status = check_category(str(ctx.guild.id), "Mini-games")
		if status == 0:
			return
		emoji_coin = self.bot.get_emoji(828277358690959380)
		if screen == None:
			screen = 1
		if screen == 1:
			description = f"""**Оружие**

			***Вилка***
			• +3 урона
			• 100 {emoji_coin}
			• ID: 1

			***Дубинка***
			• +5 урона
			• 450 {emoji_coin}
			• ID: 2

			***Кастет***
			• +8 урона
			• 600 {emoji_coin}
			• ID: 3

			***Кухонный нож***
			• +10 урона
			• 750 {emoji_coin}
			• ID: 4

			***Нож Бабочка***
			• +14 урона
			• 1050 {emoji_coin}
			• ID: 5

			***Мачете***
			• +15 урона
			• 1200 {emoji_coin}
			• ID: 6

			***Пистолет ТТ***
			• +17 урона
			• 1350 {emoji_coin}
			• ID: 7

			***Пистолет Глок-17***
			• +20 урона
			• 1500 {emoji_coin}
			• ID: 8

			***Револьер Taurus Raging Bull***
			• +22 урона
			• 1650 {emoji_coin}
			• ID: 9

			***Автомат М16***
			• +26 урона
			• 1950 {emoji_coin}
			• ID: 10

			***Снайп. винтовка ВСС "Винторез"***
			• +30 урона
			• 2250 {emoji_coin}
			• ID: 11

			***Автомат АК-12***
			• +33 урона
			• 2400 {emoji_coin}
			• ID: 12

			***Гранатомёт 6Г30***
			• +35 урона
			• 2550 {emoji_coin}
			• ID: 13

			***Гранатомёт РПГ-7***
			• +40 урона
			• 2850 {emoji_coin}
			• ID: 14

			***Гранатомёт АГС-40***
			• +45 урона
			• 3000 {emoji_coin}
			• ID: 15"""
			embed=discord.Embed(title="Магазин | Страница 1", description=description, color=discord.Color.blue())
			await ctx.send(embed=embed)
		elif screen == 2:
			description = f"""**Броня**

			***Футболка***
			• +10 здоровья
			• 100 {emoji_coin}
			• ID: 16

			***Плащ***
			• +15 здоровья
			• 480 {emoji_coin}
			• ID: 17

			***Кожаная куртка***
			• +25 здоровья
			• 640 {emoji_coin}
			• ID: 18

			***Курта с металлическими пластинами***
			• +38 здоровья
			• 770 {emoji_coin}
			• ID: 19

			***Форма полиции с лёгким бронежилетом***
			• +42 здоровья
			• 930 {emoji_coin}
			• ID: 20

			***Бронежилет Modular Tactical Vest***
			• +55 здоровья
			• 1370 {emoji_coin}
			• ID: 21

			***Бронежилет Dragon Skin***
			• +57 здоровья
			• 1550 {emoji_coin}
			• ID: 22

			***Бронежилет БКЗ 6/3-6а***
			• +65 здоровья
			• 1660 {emoji_coin}
			• ID: 23

			***Экипировка "Перехватчик"***
			• +70 здоровья
			• 1830 {emoji_coin}
			• ID: 24

			***Экипировка "ФОРТ Росич"***
			• +85 здоровья
			• 2120 {emoji_coin}
			• ID: 25

			***Экипировка "Сотник"***
			• +90 здоровья
			• 2260 {emoji_coin}
			• ID: 26

			***Экипировка NeoFelis***
			• +94 здоровья
			• 2440 {emoji_coin}
			• ID: 27

			***Экипировка Ariele***
			• +105 здоровья
			• 2580 {emoji_coin}
			• ID: 28

			***ЗСК ОРВ-2 "Сокол"***
			• +120 здоровья
			• 2860 {emoji_coin}
			• ID: 29

			***ЗСК "Заслон"***
			• +125 здоровья
			• 3030 {emoji_coin}
			• ID: 30"""
			embed=discord.Embed(title="Магазин | Страница 2", description=description, color=discord.Color.blue())
			await ctx.send(embed=embed)
		elif screen == 3:
			description = f"""**Аптечка**

			***Аптечка***
			• +20 здоровья
			• 300 {emoji_coin}
			• ID: 31"""
			embed=discord.Embed(title="Магазин | Страница 3", description=description, color=discord.Color.blue())
			await ctx.send(embed=embed)
		else:
			emoji = self.bot.get_emoji(744165695662850170)
			embed=discord.Embed(title=f"{emoji} Ошибка!", description="Нет такой страницы!", color=discord.Color.red())
			await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))