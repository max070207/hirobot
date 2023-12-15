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

def recieve_work_from_id(work_id:int):
    if work_id == 1:
        work_name = "Дворник"
        work_need_lvl = 5
        work_salary = 250
    elif work_id == 2:
        work_name = "Сторож"
        work_need_lvl = 7
        work_salary = 500
    elif work_id == 3:
        work_name = "Уборщик"
        work_need_lvl = 9
        work_salary = 750
    elif work_id == 4:
        work_name = "Врач"
        work_need_lvl = 11
        work_salary = 800
    elif work_id == 5:
        work_name = "Учитель"
        work_need_lvl = 13
        work_salary = 900
    elif work_id == 6:
        work_name = "Кассир"
        work_need_lvl = 15
        work_salary = 1000
    elif work_id == 7:
        work_name = "Водитель"
        work_need_lvl = 17
        work_salary = 1100
    elif work_id == 8:
        work_name = "Грузчик"
        work_need_lvl = 19
        work_salary = 1200
    elif work_id == 9:
        work_name = "Повар"
        work_need_lvl = 21
        work_salary = 1300
    elif work_id == 10:
        work_name = "Менеджер по продажам"
        work_need_lvl = 23
        work_salary = 1400
    elif work_id == 11:
        work_name = "Оператор колл-центра"
        work_need_lvl = 25
        work_salary = 1500
    elif work_id == 12:
        work_name = "Курьер"
        work_need_lvl = 27
        work_salary = 1750
    elif work_id == 13:
        work_name = "Репетитор"
        work_need_lvl = 29
        work_salary = 2000
    elif work_id == 14:
        work_name = "Программист"
        work_need_lvl = 31
        work_salary = 2500
    elif work_id == 15:
        work_name = "Администратор"
        work_need_lvl = 33
        work_salary = 3000
    return work_name, work_need_lvl, work_salary

class Command(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command(aliases=["profile", "профиль"])
	@commands.guild_only()
	async def __profile(self, ctx, member: discord.Member=None):
		status = check_category(str(ctx.guild.id), "Mini-games")
		if status == 0:
			return
		if member == None:
			member = ctx.author
		with open('/root/bot/databases/fight.json', 'r') as f:
			data = json.load(f)
		if not str(member.id) in data:
			emoji = self.bot.get_emoji(744165695662850170)
			embed=discord.Embed(title=f"{emoji} Ошибка!", description="Пользователь ещё ни разу не учавствовал в битвах!", color=discord.Color.red())
			await ctx.send(embed=embed)
			return
		exp = data[str(member.id)]["exp"]
		lvl = data[str(member.id)]["lvl"]
		money = data[str(member.id)]["money"]
		exp_to_new_lvl = lvl * 3 * 60 + 100
		embed=discord.Embed(title=f"Информация о пользователе {member.name}:", color=discord.Color.blue())
		embed.add_field(name="Опыт:", value=f"```python\n{exp}/{exp_to_new_lvl}```", inline=True)
		embed.add_field(name="Уровень:", value=f"```python\n{lvl}```", inline=True)
		embed.add_field(name="Монеты:", value=f"```python\n{money}```", inline=True)
		if "work" in data[str(member.id)]:
			if data[str(member.id)]["work"]["type"] == "fired":
				pass
			else:
				work = recieve_work_from_id(data[str(member.id)]["work"]["name"])
				embed.add_field(name="Работа:", value=f"```python\n{work[0]}```", inline=False)
		if len(data[str(member.id)]["items"]) != 0:
			for item in data[str(member.id)]["items"]:
				if int(item) in range(1, 31):
					if data[str(member.id)]["items"][item]["weared"] == True:
						weared = "Да"
					else:
						weared = "Нет"
					item1 = recieve_item_from_id(int(item))
					embed.add_field(name=item1[0], value=f"Надето?: **{weared}**", inline=False)
				else:
					item1 = recieve_item_from_id(int(item))
					count = data[str(member.id)]["items"][item]["count"]
					embed.add_field(name=item1[0], value=f"Количество: **{count}**", inline=False)
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))