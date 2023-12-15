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

async def wait_fight(bot, tick: int, w_member_id, block: int, count):
	try:
		tick1 = bot.get_emoji(828277269482962994)
		tick2 = bot.get_emoji(828277289736208425)
		if tick == 0:
			emojis = [str(tick1), str(tick2)]
		elif tick == 1:
			if count > 0:
				emojis = ['🗡', '🛡', '🩹']
			else:
				emojis = ['🗡', '🛡']
		elif tick == 2:
			if block == 0:
				emojis = ['1️⃣', '2️⃣', '3️⃣']
			elif block == 1:
				emojis = ['2️⃣', '3️⃣']
			elif block == 2:
				emojis = ['1️⃣','3️⃣']
			elif block == 3:
				emojis = ['1️⃣', '2️⃣']
		reaction, member = await bot.wait_for('reaction_add', timeout=30, check=lambda reaction, member: str(reaction.emoji) in emojis and member.id == w_member_id)
		if str(reaction.emoji) == str(tick1):
			return 1
		elif str(reaction.emoji) == str(tick2):
			return 2
		elif str(reaction.emoji) == '1️⃣':
			return 3
		elif str(reaction.emoji) == '2️⃣':
			return 4
		elif str(reaction.emoji) == '3️⃣':
			return 5
		elif str(reaction.emoji) == '🗡':
			return 6
		elif str(reaction.emoji) == '🛡':
			return 7
		elif str(reaction.emoji) == '🩹':
			return 8
	except asyncio.TimeoutError:
		return 0

async def add_money(user1, user2):
	user1id = str(user1.id)
	user2id = str(user2.id)
	with open('/root/bot/databases/fight.json', 'r') as f:
		data = json.load(f)
	if not user1id in data:
		data[user1id] = {}
		data[user1id]["exp"] = 0
		data[user1id]["lvl"] = 1
		data[user1id]["money"] = 0
		data[user1id]["items"] = {}
	data[user1id]["exp"] += 10
	data[user1id]["money"] += 50
	exp = data[user1id]["exp"]
	lvl = data[user1id]["lvl"]
	money = data[user1id]["money"]
	exp_end = lvl * 3 * 60 + 100
	if exp >= exp_end:
		data[user1id]["lvl"] = lvl + 1
		data[user1id]["money"] = money + 100
	if not user2id in data:
		data[user2id] = {}
		data[user2id]["exp"] = 0
		data[user2id]["lvl"] = 1
		data[user2id]["money"] = 0
		data[user2id]["items"] = {}
	data[user2id]["exp"] += 1
	data[user2id]["money"] += 5
	exp = data[user2id]["exp"]
	lvl = data[user2id]["lvl"]
	money = data[user2id]["money"]
	exp_end = lvl * 3 * 60 + 100
	if exp >= exp_end:
		data[user2id]["lvl"] = lvl + 1
		data[user2id]["money"] = money + 100
	with open('/root/bot/databases/fight.json', 'w') as f:
		json.dump(data,f,indent=4)

class Command(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command(aliases=["fight", "битва"])
	@commands.guild_only()
	@commands.cooldown(1, 60, commands.BucketType.user)
	async def __fight(self, ctx, member: discord.Member):
		try:
			status = check_category(str(ctx.guild.id), "Mini-games")
			if status == 0:
				return
			emoji_no = self.bot.get_emoji(785095586671230986)
			if member == ctx.author:
				embed=discord.Embed(title=f"{emoji_no} Ошибка!", description="Вы не можете воевать с самим собой!", color=discord.Color.red())
				await ctx.send(embed=embed)
				return
			if member.bot:
				embed=discord.Embed(title=f"{emoji_no} Ошибка!", description="Вы не можете воевать с ботами!", color=discord.Color.red())
				await ctx.send(embed=embed)
				return
			step = 0
			tick1 = self.bot.get_emoji(828277269482962994)
			tick2 = self.bot.get_emoji(828277289736208425)
			message = await ctx.send(f"{member.mention}, хочешь сразиться с {ctx.author.mention}?")
			await message.add_reaction(tick1)
			await message.add_reaction(tick2)
			w = await wait_fight(bot=self.bot, tick=0, w_member_id=member.id, block=0, count=0)
			if w == 0:
				await ctx.send(f"{member.mention} отказался сражаться с {ctx.author.mention}!")
				return
			elif w == 1:
				pass
			elif w == 2:
				await ctx.send(f"{member.mention} отказался сражаться с {ctx.author.mention}!")
				return
			else:
				end_embed=discord.Embed(title=f"Ошибка!", description=f"Произошла ошибка. Просим уведомить об этом разработчика бота, прописав ```h!bug <описание бага>```, и в поле <описание бага> написать на каком ходу случилась ошибка, какие функции вы выбирали. Спасибо!")
				await ctx.send(embed=end_embed)
				return
			with open('/root/bot/databases/fight.json', 'r') as f:
				data = json.load(f)
			blue_health = 100
			red_health = 100
			blue_block = 0
			red_block = 0
			plus_damage1 = 0
			plus_damage2 = 0
			plus_health1 = 0
			plus_health2 = 0
			if not str(ctx.author.id) in data:
				show_gun_info_blue = 0
			else:
				if len(data[str(ctx.author.id)]["items"]) == 0:
					show_gun_info_blue = 0
				else:
					for item in data[str(ctx.author.id)]["items"]:
						if int(item) in range(1, 16):
							if data[str(ctx.author.id)]["items"][item]["weared"] == True:
								plus_damage1 += data[str(ctx.author.id)]["items"][item]["damage"]
								item = recieve_item_from_id(int(item))
								blue_gun = item[0]
								show_gun_info_blue = 1
						else:
							show_gun_info_blue = 0
			if not str(member.id) in data:
				show_gun_info_red = 0
			else:
				if len(data[str(member.id)]["items"]) == 0:
					show_gun_info_red = 0
				else:
					for item in data[str(member.id)]["items"]:
						if int(item) in range(1, 16):
							if data[str(member.id)]["items"][item]["weared"] == True:
								plus_damage2 += data[str(member.id)]["items"][item]["damage"]
								item = recieve_item_from_id(int(item))
								red_gun = item[0]
								show_gun_info_red = 1
						else:
							show_gun_info_red = 0
			if not str(ctx.author.id) in data:
				show_shield_info_blue = 0
			else:
				if len(data[str(ctx.author.id)]["items"]) == 0:
					show_shield_info_blue = 0
				else:
					for item in data[str(ctx.author.id)]["items"]:
						if int(item) in range(16, 31):
							if data[str(ctx.author.id)]["items"][item]["weared"] == True:
								plus_health1 += data[str(ctx.author.id)]["items"][item]["health"]
								item = recieve_item_from_id(int(item))
								blue_shield = item[0]
								show_shield_info_blue = 1
						else:
							show_shield_info_blue = 0
			if not str(member.id) in data:
				show_shield_info_red = 0
			else:
				if len(data[str(member.id)]["items"]) == 0:
					show_shield_info_red = 0
				else:
					for item in data[str(member.id)]["items"]:
						if int(item) in range(16, 31):
							if data[str(member.id)]["items"][item]["weared"] == True:
								plus_health2 += data[str(member.id)]["items"][item]["health"]
								item = recieve_item_from_id(int(item))
								red_shield = item[0]
								show_shield_info_red = 1
						else:
							show_shield_info_red = 0
			blue_health += plus_health1
			red_health += plus_health2
			try:
				if "31" in data[str(ctx.author.id)]["items"]:
					blue_count = data[str(ctx.author.id)]["items"]["31"]["count"]
				else:
					blue_count = 0
			except KeyError:
				blue_count = 0
			try:
				if "31" in data[str(member.id)]["items"]:
					red_count = data[str(member.id)]["items"]["31"]["count"]
				else:
					red_count = 0
			except KeyError:
				red_count = 0
			try:
				lvl_blue = data[str(ctx.author.id)]["lvl"]
			except KeyError:
				lvl_blue = 1
			try:
				lvl_red = data[str(member.id)]["lvl"]
			except KeyError:
				lvl_red = 1
			#block - если = 1 то голова, 2 - тело, 3 - ноги
			while blue_health or red_health <= 0:
				step += 1
				log_blue_embed=discord.Embed(title=f":blue_square: **СИНИЙ** :blue_square:")
				log_blue_embed.set_author(name=f"Ход: {step}")
				log_blue_embed.add_field(name=f"Имя бойца:", value=f"**{ctx.author.name}**", inline=False)
				log_blue_embed.add_field(name=f"Уровень бойца:", value=f"**{lvl_blue}**", inline=False)
				log_blue_embed.add_field(name=f"Здоровье:", value=f"**{blue_health} HP**", inline=False)
				if show_gun_info_blue != 0:
					log_blue_embed.add_field(name=f"Оружие:", value=f"**{blue_gun}**", inline=False)
				else:
					pass
				if show_shield_info_blue != 0:
					log_blue_embed.add_field(name=f"Броня:", value=f"**{blue_shield}**", inline=False)
				else:
					pass
				log_blue_embed.add_field(name=f"Аптечки:", value=f"**{blue_count}**", inline=False)
				log_blue_embed.add_field(name=f"Действия:", value=f"**Чтобы атаковать, нажмите на 🗡**\n**Чтобы защититься, нажмите на 🛡**\n**Чтобы подлечиться, нажмите на 🩹**", inline=False)
				if step == 1:
					log_msg = await ctx.send(embed=log_blue_embed)
				else:
					await log_msg.edit(embed=log_blue_embed)
				await log_msg.add_reaction("🗡")
				await log_msg.add_reaction("🛡")
				if blue_count != 0:
					await log_msg.add_reaction("🩹")
				w = await wait_fight(bot=self.bot, tick=1, w_member_id=ctx.author.id, block=0, count=blue_count)
				if w == 0:
					emoji_coin = self.bot.get_emoji(828277358690959380)
					end_embed=discord.Embed(title=f"Результаты", description=f"Время игрока **{ctx.author.name}** вышло.\nПобедитель: **{member.name}**")
					end_embed.add_field(name=f"**[ПОБЕДИТЕЛЬ] {member.name}**", value=f"Награда: **+50 {emoji_coin}**\nОпыт: **+10**", inline=False)
					end_embed.add_field(name=f"**{ctx.author.name}**", value=f"Награда: **+5 {emoji_coin}**\nОпыт: **+1**", inline=False)
					await add_money(member, ctx.author)
					await ctx.send(embed=end_embed)
					return
				elif w == 6:
					if step == 1:
						log2_msg = await ctx.send(f"**{ctx.author.name}** решил атаковать!")
					else:
						await log2_msg.edit(content=f"**{ctx.author.name}** решил атаковать!")
					await log_msg.clear_reaction("🗡")
					await log_msg.clear_reaction("🛡")
					await log_msg.clear_reaction("🩹")
					log_blue_attack_embed=discord.Embed(title=f":blue_square: **СИНИЙ** :blue_square:")
					log_blue_attack_embed.set_author(name=f"Ход: {step}")
					log_blue_attack_embed.add_field(name=f"Имя бойца:", value=f"**{ctx.author.name}**", inline=False)
					log_blue_attack_embed.add_field(name=f"Уровень бойца:", value=f"**{lvl_blue}**", inline=False)
					log_blue_attack_embed.add_field(name=f"Здоровье:", value=f"**{blue_health} HP**", inline=False)
					if show_gun_info_blue != 0:
						log_blue_attack_embed.add_field(name=f"Оружие:", value=f"**{blue_gun}**", inline=False)
					else:
						pass
					if show_shield_info_blue != 0:
						log_blue_attack_embed.add_field(name=f"Броня:", value=f"**{blue_shield}**", inline=False)
					else:
						pass
					log_blue_attack_embed.add_field(name=f"Аптечки:", value=f"**{blue_count}**", inline=False)
					log_blue_attack_embed.add_field(name=f"Вы можете атаковать:", value=f":one: - в голову\n:two: - в туловище\n:three: - в ноги", inline=False)
					await log_msg.edit(embed=log_blue_attack_embed)
					if red_block == 1:
						await log_msg.add_reaction("2️⃣")
						await log_msg.add_reaction("3️⃣")
						w = await wait_fight(bot=self.bot, tick=2, w_member_id=ctx.author.id, block=1, count=blue_count)
						if w == 0:
							emoji_coin = self.bot.get_emoji(828277358690959380)
							end_embed=discord.Embed(title=f"Результаты", description=f"Время игрока **{ctx.author.name}** вышло.\nПобедитель: **{member.name}**")
							end_embed.add_field(name=f"**[ПОБЕДИТЕЛЬ] {member.name}**", value=f"Награда: **+50 {emoji_coin}**\nОпыт: **+10**", inline=False)
							end_embed.add_field(name=f"**{ctx.author.name}**", value=f"Награда: **+5 {emoji_coin}**\nОпыт: **+1**", inline=False)
							await ctx.send(embed=end_embed)
							await add_money(member, ctx.author)
							return
						elif w == 4:
							await log_msg.clear_reaction("1️⃣")
							await log_msg.clear_reaction("2️⃣")
							await log_msg.clear_reaction("3️⃣")
							damage = random.randint(5,20)
							red_health = red_health - damage - plus_damage1
							await log2_msg.edit(content=f"**{ctx.author.name}** ударил **{member.name}** в туловище и нанёс **{damage + plus_damage1}** урона! У **{member.name}** осталось **{red_health}** HP!")
							if blue_health <= 0:
								emoji_coin = self.bot.get_emoji(828277358690959380)
								end_embed=discord.Embed(title=f"Результаты", description=f"**{member.name}**, поздравляю тебя, ты победил игрока **{ctx.author.name}**! :tada:")
								end_embed.add_field(name=f"**[ПОБЕДИТЕЛЬ] {member.name}**", value=f"Награда: **+50 {emoji_coin}**\nОпыт: **+10**", inline=False)
								end_embed.add_field(name=f"**{ctx.author.name}**", value=f"Награда: **+5 {emoji_coin}**\nОпыт: **+1**", inline=False)
								await ctx.send(embed=end_embed)
								await add_money(member, ctx.author)
								return
							elif red_health <= 0:
								emoji_coin = self.bot.get_emoji(828277358690959380)
								end_embed=discord.Embed(title=f"Результаты", description=f"**{ctx.author.name}**, поздравляю тебя, ты победил игрока **{member.name}**! :tada:")
								end_embed.add_field(name=f"**[ПОБЕДИТЕЛЬ] {ctx.author.name}**", value=f"Награда: **+50 {emoji_coin}**\nОпыт: **+10**", inline=False)
								end_embed.add_field(name=f"**{member.name}**", value=f"Награда: **+5 {emoji_coin}**\nОпыт: **+1**", inline=False)
								await ctx.send(embed=end_embed)
								await add_money(ctx.author, member)
								return
							else:
								pass
						elif w == 5:
							await log_msg.clear_reaction("1️⃣")
							await log_msg.clear_reaction("2️⃣")
							await log_msg.clear_reaction("3️⃣")
							damage = random.randint(10,15)
							red_health = red_health - damage - plus_damage1
							await log2_msg.edit(content=f"**{ctx.author.name}** ударил **{member.name}** в ноги и нанёс **{damage + plus_damage1}** урона! У **{member.name}** осталось **{red_health}** HP!")
							if blue_health <= 0:
								emoji_coin = self.bot.get_emoji(828277358690959380)
								end_embed=discord.Embed(title=f"Результаты", description=f"**{member.name}**, поздравляю тебя, ты победил игрока **{ctx.author.name}**! :tada:")
								end_embed.add_field(name=f"**[ПОБЕДИТЕЛЬ] {member.name}**", value=f"Награда: **+50 {emoji_coin}**\nОпыт: **+10**", inline=False)
								end_embed.add_field(name=f"**{ctx.author.name}**", value=f"Награда: **+5 {emoji_coin}**\nОпыт: **+1**", inline=False)
								await ctx.send(embed=end_embed)
								await add_money(member, ctx.author)
								return
							elif red_health <= 0:
								emoji_coin = self.bot.get_emoji(828277358690959380)
								end_embed=discord.Embed(title=f"Результаты", description=f"**{ctx.author.name}**, поздравляю тебя, ты победил игрока **{member.name}**! :tada:")
								end_embed.add_field(name=f"**[ПОБЕДИТЕЛЬ] {ctx.author.name}**", value=f"Награда: **+50 {emoji_coin}**\nОпыт: **+10**", inline=False)
								end_embed.add_field(name=f"**{member.name}**", value=f"Награда: **+5 {emoji_coin}**\nОпыт: **+1**", inline=False)
								await ctx.send(embed=end_embed)
								await add_money(ctx.author, member)
								return
							else:
								pass
						else:
							end_embed=discord.Embed(title=f"Ошибка!", description=f"Произошла ошибка. Просим уведомить об этом разработчика бота, прописав ```h!bug <описание бага>```, и в поле <описание бага> написать на каком ходу случилась ошибка, какие функции вы выбирали. Спасибо!")
							await ctx.send(embed=end_embed)
							return
					elif red_block == 2:
						await log_msg.add_reaction("1️⃣")
						await log_msg.add_reaction("3️⃣")
						w = await wait_fight(bot=self.bot, tick=2, w_member_id=ctx.author.id, block=2, count=blue_count)
						if w == 0:
							emoji_coin = self.bot.get_emoji(828277358690959380)
							end_embed=discord.Embed(title=f"Результаты", description=f"Время игрока **{ctx.author.name}** вышло.\nПобедитель: **{member.name}**")
							end_embed.add_field(name=f"**[ПОБЕДИТЕЛЬ] {member.name}**", value=f"Награда: **+50 {emoji_coin}**\nОпыт: **+10**", inline=False)
							end_embed.add_field(name=f"**{ctx.author.name}**", value=f"Награда: **+5 {emoji_coin}**\nОпыт: **+1**", inline=False)
							await ctx.send(embed=end_embed)
							await add_money(member, ctx.author)
							return
						elif w == 3:
							await log_msg.clear_reaction("1️⃣")
							await log_msg.clear_reaction("2️⃣")
							await log_msg.clear_reaction("3️⃣")
							damage = random.randint(15,30)
							red_health = red_health - damage - plus_damage1
							await log2_msg.edit(content=f"**{ctx.author.name}** ударил **{member.name}** в голову и нанёс **{damage + plus_damage1}** урона! У **{member.name}** осталось **{red_health}** HP!")
							if blue_health <= 0:
								emoji_coin = self.bot.get_emoji(828277358690959380)
								end_embed=discord.Embed(title=f"Результаты", description=f"**{member.name}**, поздравляю тебя, ты победил игрока **{ctx.author.name}**! :tada:")
								end_embed.add_field(name=f"**[ПОБЕДИТЕЛЬ] {member.name}**", value=f"Награда: **+50 {emoji_coin}**\nОпыт: **+10**", inline=False)
								end_embed.add_field(name=f"**{ctx.author.name}**", value=f"Награда: **+5 {emoji_coin}**\nОпыт: **+1**", inline=False)
								await ctx.send(embed=end_embed)
								await add_money(member, ctx.author)
								return
							elif red_health <= 0:
								emoji_coin = self.bot.get_emoji(828277358690959380)
								end_embed=discord.Embed(title=f"Результаты", description=f"**{ctx.author.name}**, поздравляю тебя, ты победил игрока **{member.name}**! :tada:")
								end_embed.add_field(name=f"**[ПОБЕДИТЕЛЬ] {ctx.author.name}**", value=f"Награда: **+50 {emoji_coin}**\nОпыт: **+10**", inline=False)
								end_embed.add_field(name=f"**{member.name}**", value=f"Награда: **+5 {emoji_coin}**\nОпыт: **+1**", inline=False)
								await ctx.send(embed=end_embed)
								await add_money(ctx.author, member)
								return
							else:
								pass
						elif w == 5:
							await log_msg.clear_reaction("1️⃣")
							await log_msg.clear_reaction("2️⃣")
							await log_msg.clear_reaction("3️⃣")
							damage = random.randint(10,15)
							red_health = red_health - damage - plus_damage1
							await log2_msg.edit(content=f"**{ctx.author.name}** ударил **{member.name}** в ноги и нанёс **{damage + plus_damage1}** урона! У **{member.name}** осталось **{red_health}** HP!")
							if blue_health <= 0:
								emoji_coin = self.bot.get_emoji(828277358690959380)
								end_embed=discord.Embed(title=f"Результаты", description=f"**{member.name}**, поздравляю тебя, ты победил игрока **{ctx.author.name}**! :tada:")
								end_embed.add_field(name=f"**[ПОБЕДИТЕЛЬ] {member.name}**", value=f"Награда: **+50 {emoji_coin}**\nОпыт: **+10**", inline=False)
								end_embed.add_field(name=f"**{ctx.author.name}**", value=f"Награда: **+5 {emoji_coin}**\nОпыт: **+1**", inline=False)
								await ctx.send(embed=end_embed)
								await add_money(member, ctx.author)
								return
							elif red_health <= 0:
								emoji_coin = self.bot.get_emoji(828277358690959380)
								end_embed=discord.Embed(title=f"Результаты", description=f"**{ctx.author.name}**, поздравляю тебя, ты победил игрока **{member.name}**! :tada:")
								end_embed.add_field(name=f"**[ПОБЕДИТЕЛЬ] {ctx.author.name}**", value=f"Награда: **+50 {emoji_coin}**\nОпыт: **+10**", inline=False)
								end_embed.add_field(name=f"**{member.name}**", value=f"Награда: **+5 {emoji_coin}**\nОпыт: **+1**", inline=False)
								await ctx.send(embed=end_embed)
								await add_money(ctx.author, member)
								return
							else:
								pass
						else:
							end_embed=discord.Embed(title=f"Ошибка!", description=f"Произошла ошибка. Просим уведомить об этом разработчика бота, прописав ```h!bug <описание бага>```, и в поле <описание бага> написать на каком ходу случилась ошибка, какие функции вы выбирали. Спасибо!")
							await ctx.send(embed=end_embed)
							return
					elif red_block == 3:
						await log_msg.add_reaction("1️⃣")
						await log_msg.add_reaction("2️⃣")
						w = await wait_fight(bot=self.bot, tick=2, w_member_id=ctx.author.id, block=3, count=blue_count)
						if w == 0:
							emoji_coin = self.bot.get_emoji(828277358690959380)
							end_embed=discord.Embed(title=f"Результаты", description=f"Время игрока **{ctx.author.name}** вышло.\nПобедитель: **{member.name}**")
							end_embed.add_field(name=f"**[ПОБЕДИТЕЛЬ] {member.name}**", value=f"Награда: **+50 {emoji_coin}**\nОпыт: **+10**", inline=False)
							end_embed.add_field(name=f"**{ctx.author.name}**", value=f"Награда: **+5 {emoji_coin}**\nОпыт: **+1**", inline=False)
							await ctx.send(embed=end_embed)
							await add_money(member, ctx.author)
							return
						elif w == 3:
							await log_msg.clear_reaction("1️⃣")
							await log_msg.clear_reaction("2️⃣")
							await log_msg.clear_reaction("3️⃣")
							damage = random.randint(15,30)
							red_health = red_health - damage - plus_damage1
							await log2_msg.edit(content=f"**{ctx.author.name}** ударил **{member.name}** в голову и нанёс **{damage + plus_damage1}** урона! У **{member.name}** осталось **{red_health}** HP!")
							if blue_health <= 0:
								emoji_coin = self.bot.get_emoji(828277358690959380)
								end_embed=discord.Embed(title=f"Результаты", description=f"**{member.name}**, поздравляю тебя, ты победил игрока **{ctx.author.name}**! :tada:")
								end_embed.add_field(name=f"**[ПОБЕДИТЕЛЬ] {member.name}**", value=f"Награда: **+50 {emoji_coin}**\nОпыт: **+10**", inline=False)
								end_embed.add_field(name=f"**{ctx.author.name}**", value=f"Награда: **+5 {emoji_coin}**\nОпыт: **+1**", inline=False)
								await ctx.send(embed=end_embed)
								await add_money(member, ctx.author)
								return
							elif red_health <= 0:
								emoji_coin = self.bot.get_emoji(828277358690959380)
								end_embed=discord.Embed(title=f"Результаты", description=f"**{ctx.author.name}**, поздравляю тебя, ты победил игрока **{member.name}**! :tada:")
								end_embed.add_field(name=f"**[ПОБЕДИТЕЛЬ] {ctx.author.name}**", value=f"Награда: **+50 {emoji_coin}**\nОпыт: **+10**", inline=False)
								end_embed.add_field(name=f"**{member.name}**", value=f"Награда: **+5 {emoji_coin}**\nОпыт: **+1**", inline=False)
								await ctx.send(embed=end_embed)
								await add_money(ctx.author, member)
								return
							else:
								pass
						elif w == 4:
							await log_msg.clear_reaction("1️⃣")
							await log_msg.clear_reaction("2️⃣")
							await log_msg.clear_reaction("3️⃣")
							damage = random.randint(5,20)
							red_health = red_health - damage - plus_damage1
							await log2_msg.edit(content=f"**{ctx.author.name}** ударил **{member.name}** в туловище и нанёс **{damage + plus_damage1}** урона! У **{member.name}** осталось **{red_health}** HP!")
							if blue_health <= 0:
								emoji_coin = self.bot.get_emoji(828277358690959380)
								end_embed=discord.Embed(title=f"Результаты", description=f"**{member.name}**, поздравляю тебя, ты победил игрока **{ctx.author.name}**! :tada:")
								end_embed.add_field(name=f"**[ПОБЕДИТЕЛЬ] {member.name}**", value=f"Награда: **+50 {emoji_coin}**\nОпыт: **+10**", inline=False)
								end_embed.add_field(name=f"**{ctx.author.name}**", value=f"Награда: **+5 {emoji_coin}**\nОпыт: **+1**", inline=False)
								await ctx.send(embed=end_embed)
								await add_money(member, ctx.author)
								return
							elif red_health <= 0:
								emoji_coin = self.bot.get_emoji(828277358690959380)
								end_embed=discord.Embed(title=f"Результаты", description=f"**{ctx.author.name}**, поздравляю тебя, ты победил игрока **{member.name}**! :tada:")
								end_embed.add_field(name=f"**[ПОБЕДИТЕЛЬ] {ctx.author.name}**", value=f"Награда: **+50 {emoji_coin}**\nОпыт: **+10**", inline=False)
								end_embed.add_field(name=f"**{member.name}**", value=f"Награда: **+5 {emoji_coin}**\nОпыт: **+1**", inline=False)
								await ctx.send(embed=end_embed)
								await add_money(ctx.author, member)
								return
							else:
								pass
						else:
							end_embed=discord.Embed(title=f"Ошибка!", description=f"Произошла ошибка. Просим уведомить об этом разработчика бота, прописав ```h!bug <описание бага>```, и в поле <описание бага> написать на каком ходу случилась ошибка, какие функции вы выбирали. Спасибо!")
							await ctx.send(embed=end_embed)
							return
					else:
						await log_msg.add_reaction("1️⃣")
						await log_msg.add_reaction("2️⃣")
						await log_msg.add_reaction("3️⃣")
						w = await wait_fight(bot=self.bot, tick=2, w_member_id=ctx.author.id, block=0, count=blue_count)
						if w == 0:
							emoji_coin = self.bot.get_emoji(828277358690959380)
							end_embed=discord.Embed(title=f"Результаты", description=f"Время игрока **{ctx.author.name}** вышло.\nПобедитель: **{member.name}**")
							end_embed.add_field(name=f"**[ПОБЕДИТЕЛЬ] {member.name}**", value=f"Награда: **+50 {emoji_coin}**\nОпыт: **+10**", inline=False)
							end_embed.add_field(name=f"**{ctx.author.name}**", value=f"Награда: **+5 {emoji_coin}**\nОпыт: **+1**", inline=False)
							await ctx.send(embed=end_embed)
							await add_money(member, ctx.author)
							return
						elif w == 3:
							await log_msg.clear_reaction("1️⃣")
							await log_msg.clear_reaction("2️⃣")
							await log_msg.clear_reaction("3️⃣")
							damage = random.randint(15,30)
							red_health = red_health - damage - plus_damage1
							await log2_msg.edit(content=f"**{ctx.author.name}** ударил **{member.name}** в голову и нанёс **{damage + plus_damage1}** урона! У **{member.name}** осталось **{red_health}** HP!")
							if blue_health <= 0:
								emoji_coin = self.bot.get_emoji(828277358690959380)
								end_embed=discord.Embed(title=f"Результаты", description=f"**{member.name}**, поздравляю тебя, ты победил игрока **{ctx.author.name}**! :tada:")
								end_embed.add_field(name=f"**[ПОБЕДИТЕЛЬ] {member.name}**", value=f"Награда: **+50 {emoji_coin}**\nОпыт: **+10**", inline=False)
								end_embed.add_field(name=f"**{ctx.author.name}**", value=f"Награда: **+5 {emoji_coin}**\nОпыт: **+1**", inline=False)
								await ctx.send(embed=end_embed)
								await add_money(member, ctx.author)
								return
							elif red_health <= 0:
								emoji_coin = self.bot.get_emoji(828277358690959380)
								end_embed=discord.Embed(title=f"Результаты", description=f"**{ctx.author.name}**, поздравляю тебя, ты победил игрока **{member.name}**! :tada:")
								end_embed.add_field(name=f"**[ПОБЕДИТЕЛЬ] {ctx.author.name}**", value=f"Награда: **+50 {emoji_coin}**\nОпыт: **+10**", inline=False)
								end_embed.add_field(name=f"**{member.name}**", value=f"Награда: **+5 {emoji_coin}**\nОпыт: **+1**", inline=False)
								await ctx.send(embed=end_embed)
								await add_money(ctx.author, member)
								return
							else:
								pass
						elif w == 4:
							await log_msg.clear_reaction("1️⃣")
							await log_msg.clear_reaction("2️⃣")
							await log_msg.clear_reaction("3️⃣")
							damage = random.randint(5,20)
							red_health = red_health - damage - plus_damage1
							await log2_msg.edit(content=f"**{ctx.author.name}** ударил **{member.name}** в туловище и нанёс **{damage + plus_damage1}** урона! У **{member.name}** осталось **{red_health}** HP!")
							if blue_health <= 0:
								emoji_coin = self.bot.get_emoji(828277358690959380)
								end_embed=discord.Embed(title=f"Результаты", description=f"**{member.name}**, поздравляю тебя, ты победил игрока **{ctx.author.name}**! :tada:")
								end_embed.add_field(name=f"**[ПОБЕДИТЕЛЬ] {member.name}**", value=f"Награда: **+50 {emoji_coin}**\nОпыт: **+10**", inline=False)
								end_embed.add_field(name=f"**{ctx.author.name}**", value=f"Награда: **+5 {emoji_coin}**\nОпыт: **+1**", inline=False)
								await ctx.send(embed=end_embed)
								await add_money(member, ctx.author)
								return
							elif red_health <= 0:
								emoji_coin = self.bot.get_emoji(828277358690959380)
								end_embed=discord.Embed(title=f"Результаты", description=f"**{ctx.author.name}**, поздравляю тебя, ты победил игрока **{member.name}**! :tada:")
								end_embed.add_field(name=f"**[ПОБЕДИТЕЛЬ] {ctx.author.name}**", value=f"Награда: **+50 {emoji_coin}**\nОпыт: **+10**", inline=False)
								end_embed.add_field(name=f"**{member.name}**", value=f"Награда: **+5 {emoji_coin}**\nОпыт: **+1**", inline=False)
								await ctx.send(embed=end_embed)
								await add_money(ctx.author, member)
								return
							else:
								pass
						elif w == 5:
							await log_msg.clear_reaction("1️⃣")
							await log_msg.clear_reaction("2️⃣")
							await log_msg.clear_reaction("3️⃣")
							damage = random.randint(10,15)
							red_health = red_health - damage - plus_damage1
							await log2_msg.edit(content=f"**{ctx.author.name}** ударил **{member.name}** в ноги и нанёс **{damage + plus_damage1}** урона! У **{member.name}** осталось **{red_health}** HP!")
							if blue_health <= 0:
								emoji_coin = self.bot.get_emoji(828277358690959380)
								end_embed=discord.Embed(title=f"Результаты", description=f"**{member.name}**, поздравляю тебя, ты победил игрока **{ctx.author.name}**! :tada:")
								end_embed.add_field(name=f"**[ПОБЕДИТЕЛЬ] {member.name}**", value=f"Награда: **+50 {emoji_coin}**\nОпыт: **+10**", inline=False)
								end_embed.add_field(name=f"**{ctx.author.name}**", value=f"Награда: **+5 {emoji_coin}**\nОпыт: **+1**", inline=False)
								await ctx.send(embed=end_embed)
								await add_money(member, ctx.author)
								return
							elif red_health <= 0:
								emoji_coin = self.bot.get_emoji(828277358690959380)
								end_embed=discord.Embed(title=f"Результаты", description=f"**{ctx.author.name}**, поздравляю тебя, ты победил игрока **{member.name}**! :tada:")
								end_embed.add_field(name=f"**[ПОБЕДИТЕЛЬ] {ctx.author.name}**", value=f"Награда: **+50 {emoji_coin}**\nОпыт: **+10**", inline=False)
								end_embed.add_field(name=f"**{member.name}**", value=f"Награда: **+5 {emoji_coin}**\nОпыт: **+1**", inline=False)
								await ctx.send(embed=end_embed)
								await add_money(ctx.author, member)
								return
							else:
								pass
						else:
							end_embed=discord.Embed(title=f"Ошибка!", description=f"Произошла ошибка. Просим уведомить об этом разработчика бота, прописав ```h!bug <описание бага>```, и в поле <описание бага> написать на каком ходу случилась ошибка, какие функции вы выбирали. Спасибо!")
							await ctx.send(embed=end_embed)
							return
				elif w == 7:
					if step == 1:
						log2_msg = await ctx.send(content=f"**{ctx.author.name}** решил защищаться!")
					else:
						await log2_msg.edit(content=f"**{ctx.author.name}** решил защищаться!")
					await log_msg.clear_reaction("🗡")
					await log_msg.clear_reaction("🛡")
					await log_msg.clear_reaction("🩹")
					log_red_attack_embed=discord.Embed(title=f":blue_square: **СИНИЙ** :blue_square:")
					log_red_attack_embed.set_author(name=f"Ход: {step}")
					log_red_attack_embed.add_field(name=f"Имя бойца:", value=f"**{ctx.author.name}**", inline=False)
					log_red_attack_embed.add_field(name=f"Уровень бойца:", value=f"**{lvl_blue}**", inline=False)
					log_red_attack_embed.add_field(name=f"Здоровье:", value=f"**{blue_health} HP**", inline=False)
					if show_gun_info_blue != 0:
						log_red_attack_embed.add_field(name=f"Оружие:", value=f"**{blue_gun}**", inline=False)
					else:
						pass
					if show_shield_info_blue != 0:
						log_red_attack_embed.add_field(name=f"Броня:", value=f"**{blue_shield}**", inline=False)
					else:
						pass
					log_red_attack_embed.add_field(name=f"Аптечки:", value=f"**{blue_count}**", inline=False)
					log_red_attack_embed.add_field(name=f"Вы можете защитить:", value=f":one: - голову\n:two: - туловище\n:three: - ноги", inline=False)
					await log_msg.edit(embed=log_red_attack_embed)
					await log_msg.add_reaction("1️⃣")
					await log_msg.add_reaction("2️⃣")
					await log_msg.add_reaction("3️⃣")
					w = await wait_fight(bot=self.bot, tick=2, w_member_id=ctx.author.id, block=0, count=blue_count)
					if w == 0:
						emoji_coin = self.bot.get_emoji(828277358690959380)
						end_embed=discord.Embed(title=f"Результаты", description=f"Время игрока **{ctx.author.name}** вышло.\nПобедитель: **{member.name}**")
						end_embed.add_field(name=f"**[ПОБЕДИТЕЛЬ] {member.name}**", value=f"Награда: **+50 {emoji_coin}**\nОпыт: **+10**", inline=False)
						end_embed.add_field(name=f"**{ctx.author.name}**", value=f"Награда: **+5 {emoji_coin}**\nОпыт: **+1**", inline=False)
						await ctx.send(embed=end_embed)
						await add_money(member, ctx.author)
						return
					elif w == 3:
						await log_msg.clear_reaction("1️⃣")
						await log_msg.clear_reaction("2️⃣")
						await log_msg.clear_reaction("3️⃣")
						blue_block = 1
						await log2_msg.edit(content=f"**{ctx.author.name}** защитил **голову**")
					elif w == 4:
						await log_msg.clear_reaction("1️⃣")
						await log_msg.clear_reaction("2️⃣")
						await log_msg.clear_reaction("3️⃣")
						blue_block = 2
						await log2_msg.edit(content=f"**{ctx.author.name}** защитил **туловище**")
					elif w == 5:
						await log_msg.clear_reaction("1️⃣")
						await log_msg.clear_reaction("2️⃣")
						await log_msg.clear_reaction("3️⃣")
						blue_block = 3
						await log2_msg.edit(content=f"**{ctx.author.name}** защитил **ноги**")
					else:
						end_embed=discord.Embed(title=f"Ошибка!", description=f"Произошла ошибка. Просим уведомить об этом разработчика бота, прописав ```h!bug <описание бага>```, и в поле <описание бага> написать на каком ходу случилась ошибка, какие функции вы выбирали. Спасибо!")
						await ctx.send(embed=end_embed)
						return
				elif w == 8:
					if step == 1:
						log2_msg = await ctx.send(content=f"**{ctx.author.name}** решил подлечиться!")
					else:
						await log2_msg.edit(content=f"**{ctx.author.name}** решил подлечиться!")
					await log_msg.clear_reaction("🗡")
					await log_msg.clear_reaction("🛡")
					await log_msg.clear_reaction("🩹")
					if data[str(ctx.author.id)]["items"]["31"]["count"] > 0:
						blue_health += 20
						data[str(ctx.author.id)]["items"]["31"]["count"] -= 1
						blue_count -= 1
						with open('/root/bot/databases/fight.json', 'w') as f:
							json.dump(data,f,indent=4)
						await log2_msg.edit(content=f"**{ctx.author.name}** подлечился!")
					else:
						end_embed=discord.Embed(title=f"Ошибка!", description=f"Произошла ошибка. Просим уведомить об этом разработчика бота, прописав ```h!bug <описание бага>```, и в поле <описание бага> написать на каком ходу случилась ошибка, какие функции вы выбирали. Спасибо!")
						await ctx.send(embed=end_embed)
						return
				else:
					emoji_coin = self.bot.get_emoji(828277358690959380)
					end_embed=discord.Embed(title=f"Результаты", description=f"Время игрока **{ctx.author.name}** вышло.\nПобедитель: **{member.name}**")
					end_embed.add_field(name=f"**[ПОБЕДИТЕЛЬ] {member.name}**", value=f"Награда: **+50 {emoji_coin}**\nОпыт: **+10**", inline=False)
					end_embed.add_field(name=f"**{ctx.author.name}**", value=f"Награда: **+5 {emoji_coin}**\nОпыт: **+1**", inline=False)
					await ctx.send(embed=end_embed)
					await add_money(member, ctx.author)
					return
				red_block = 0
				log_blue_embed=discord.Embed(title=f":red_square: **КРАСНЫЙ** :red_square:")
				log_blue_embed.set_author(name=f"Ход: {step}")
				log_blue_embed.add_field(name=f"Имя бойца:", value=f"**{member.name}**", inline=False)
				log_blue_embed.add_field(name=f"Уровень бойца:", value=f"**{lvl_red}**", inline=False)
				log_blue_embed.add_field(name=f"Здоровье:", value=f"**{red_health} HP**", inline=False)
				if show_gun_info_red != 0:
					log_blue_embed.add_field(name=f"Оружие:", value=f"**{red_gun}**", inline=False)
				else:
					pass
				if show_shield_info_red != 0:
					log_blue_embed.add_field(name=f"Броня:", value=f"**{red_shield}**", inline=False)
				else:
					pass
				log_blue_embed.add_field(name=f"Аптечки:", value=f"**{red_count}**", inline=False)
				log_blue_embed.add_field(name=f"Действия:", value=f"**Чтобы атаковать, нажмите на 🗡**\n**Чтобы защититься, нажмите на 🛡**\n**Чтобы подлечиться, нажмите на 🩹**", inline=False)
				await log_msg.edit(embed=log_blue_embed)
				await log_msg.add_reaction("🗡")
				await log_msg.add_reaction("🛡")
				if red_count != 0:
					await log_msg.add_reaction("🩹")
				w = await wait_fight(bot=self.bot, tick=1, w_member_id=member.id, block=0, count=red_count)
				if w == 0:
					emoji_coin = self.bot.get_emoji(828277358690959380)
					end_embed=discord.Embed(title=f"Результаты", description=f"Время игрока **{member.name}** вышло.\nПобедитель: **{ctx.author.name}**")
					end_embed.add_field(name=f"**[ПОБЕДИТЕЛЬ] {ctx.author.name}**", value=f"Награда: **+50 {emoji_coin}**\nОпыт: **+10**", inline=False)
					end_embed.add_field(name=f"**{member.name}**", value=f"Награда: **+5 {emoji_coin}**\nОпыт: **+1**", inline=False)
					await ctx.send(embed=end_embed)
					await add_money(ctx.author, member)
					return
				elif w == 6:
					await log2_msg.edit(content=f"**{member.name}** решил атаковать!")
					await log_msg.clear_reaction("🗡")
					await log_msg.clear_reaction("🛡")
					await log_msg.clear_reaction("🩹")
					log_blue_attack_embed=discord.Embed(title=f":red_square: **КРАСНЫЙ** :red_square:")
					log_blue_attack_embed.set_author(name=f"Ход: {step}")
					log_blue_attack_embed.add_field(name=f"Имя бойца:", value=f"**{member.name}**", inline=False)
					log_blue_attack_embed.add_field(name=f"Уровень бойца:", value=f"**{lvl_red}**", inline=False)
					log_blue_attack_embed.add_field(name=f"Здоровье:", value=f"**{red_health} HP**", inline=False)
					if show_gun_info_red != 0:
						log_blue_attack_embed.add_field(name=f"Оружие:", value=f"**{red_gun}**", inline=False)
					else:
						pass
					if show_shield_info_red != 0:
						log_blue_attack_embed.add_field(name=f"Броня:", value=f"**{red_shield}**", inline=False)
					else:
						pass
					log_blue_attack_embed.add_field(name=f"Аптечки:", value=f"**{red_count}**", inline=False)
					log_blue_attack_embed.add_field(name=f"Вы можете атаковать:", value=f":one: - в голову\n:two: - в туловище\n:three: - в ноги", inline=False)
					await log_msg.edit(embed=log_blue_attack_embed)
					if blue_block == 1:
						await log_msg.add_reaction("2️⃣")
						await log_msg.add_reaction("3️⃣")
						w = await wait_fight(bot=self.bot, tick=2, w_member_id=member.id, block=1, count=red_count)
						if w == 0:
							emoji_coin = self.bot.get_emoji(828277358690959380)
							end_embed=discord.Embed(title=f"Результаты", description=f"Время игрока **{member.name}** вышло.\nПобедитель: **{ctx.author.name}**")
							end_embed.add_field(name=f"**[ПОБЕДИТЕЛЬ] {ctx.author.name}**", value=f"Награда: **+50 {emoji_coin}**\nОпыт: **+10**", inline=False)
							end_embed.add_field(name=f"**{member.name}**", value=f"Награда: **+5 {emoji_coin}**\nОпыт: **+1**", inline=False)
							await ctx.send(embed=end_embed)
							await add_money(ctx.author, member)
							return
						elif w == 4:
							await log_msg.clear_reaction("1️⃣")
							await log_msg.clear_reaction("2️⃣")
							await log_msg.clear_reaction("3️⃣")
							damage = random.randint(5,20)
							blue_health = blue_health - damage - plus_damage2
							await log2_msg.edit(content=f"**{member.name}** ударил **{ctx.author.name}** в туловище и нанёс **{damage + plus_damage2}** урона! У **{ctx.author.name}** осталось **{blue_health}** HP!")
							if blue_health <= 0:
								emoji_coin = self.bot.get_emoji(828277358690959380)
								end_embed=discord.Embed(title=f"Результаты", description=f"**{member.name}**, поздравляю тебя, ты победил игрока **{ctx.author.name}**! :tada:")
								end_embed.add_field(name=f"**[ПОБЕДИТЕЛЬ] {member.name}**", value=f"Награда: **+50 {emoji_coin}**\nОпыт: **+10**", inline=False)
								end_embed.add_field(name=f"**{ctx.author.name}**", value=f"Награда: **+5 {emoji_coin}**\nОпыт: **+1**", inline=False)
								await ctx.send(embed=end_embed)
								await add_money(member, ctx.author)
								return
							elif red_health <= 0:
								emoji_coin = self.bot.get_emoji(828277358690959380)
								end_embed=discord.Embed(title=f"Результаты", description=f"**{ctx.author.name}**, поздравляю тебя, ты победил игрока **{member.name}**! :tada:")
								end_embed.add_field(name=f"**[ПОБЕДИТЕЛЬ] {ctx.author.name}**", value=f"Награда: **+50 {emoji_coin}**\nОпыт: **+10**", inline=False)
								end_embed.add_field(name=f"**{member.name}**", value=f"Награда: **+5 {emoji_coin}**\nОпыт: **+1**", inline=False)
								await ctx.send(embed=end_embed)
								await add_money(ctx.author, member)
								return
							else:
								pass
						elif w == 5:
							await log_msg.clear_reaction("1️⃣")
							await log_msg.clear_reaction("2️⃣")
							await log_msg.clear_reaction("3️⃣")
							damage = random.randint(10,15)
							blue_health = blue_health - damage - plus_damage2
							await log2_msg.edit(content=f"**{member.name}** ударил **{ctx.author.name}** в ноги и нанёс **{damage + plus_damage2}** урона! У **{ctx.author.name}** осталось **{blue_health}** HP!")
							if blue_health <= 0:
								emoji_coin = self.bot.get_emoji(828277358690959380)
								end_embed=discord.Embed(title=f"Результаты", description=f"**{member.name}**, поздравляю тебя, ты победил игрока **{ctx.author.name}**! :tada:")
								end_embed.add_field(name=f"**[ПОБЕДИТЕЛЬ] {member.name}**", value=f"Награда: **+50 {emoji_coin}**\nОпыт: **+10**", inline=False)
								end_embed.add_field(name=f"**{ctx.author.name}**", value=f"Награда: **+5 {emoji_coin}**\nОпыт: **+1**", inline=False)
								await ctx.send(embed=end_embed)
								await add_money(member, ctx.author)
								return
							elif red_health <= 0:
								emoji_coin = self.bot.get_emoji(828277358690959380)
								end_embed=discord.Embed(title=f"Результаты", description=f"**{ctx.author.name}**, поздравляю тебя, ты победил игрока **{member.name}**! :tada:")
								end_embed.add_field(name=f"**[ПОБЕДИТЕЛЬ] {ctx.author.name}**", value=f"Награда: **+50 {emoji_coin}**\nОпыт: **+10**", inline=False)
								end_embed.add_field(name=f"**{member.name}**", value=f"Награда: **+5 {emoji_coin}**\nОпыт: **+1**", inline=False)
								await ctx.send(embed=end_embed)
								await add_money(ctx.author, member)
								return
							else:
								pass
						else:
							end_embed=discord.Embed(title=f"Ошибка!", description=f"Произошла ошибка. Просим уведомить об этом разработчика бота, прописав ```h!bug <описание бага>```, и в поле <описание бага> написать на каком ходу случилась ошибка, какие функции вы выбирали. Спасибо!")
							await ctx.send(embed=end_embed)
							return
					elif blue_block == 2:
						await log_msg.add_reaction("1️⃣")
						await log_msg.add_reaction("3️⃣")
						w = await wait_fight(bot=self.bot, tick=2, w_member_id=member.id, block=2, count=red_count)
						if w == 0:
							emoji_coin = self.bot.get_emoji(828277358690959380)
							end_embed=discord.Embed(title=f"Результаты", description=f"Время игрока **{member.name}** вышло.\nПобедитель: **{ctx.author.name}**")
							end_embed.add_field(name=f"**[ПОБЕДИТЕЛЬ] {ctx.author.name}**", value=f"Награда: **+50 {emoji_coin}**\nОпыт: **+10**", inline=False)
							end_embed.add_field(name=f"**{member.name}**", value=f"Награда: **+5 {emoji_coin}**\nОпыт: **+1**", inline=False)
							await ctx.send(embed=end_embed)
							await add_money(ctx.author, member)
							return
						elif w == 3:
							await log_msg.clear_reaction("1️⃣")
							await log_msg.clear_reaction("2️⃣")
							await log_msg.clear_reaction("3️⃣")
							damage = random.randint(15,30)
							blue_health = blue_health - damage - plus_damage2
							await log2_msg.edit(content=f"**{member.name}** ударил **{ctx.author.name}** в голову и нанёс **{damage + plus_damage2}** урона! У **{ctx.author.name}** осталось **{blue_health}** HP!")
							if blue_health <= 0:
								emoji_coin = self.bot.get_emoji(828277358690959380)
								end_embed=discord.Embed(title=f"Результаты", description=f"**{member.name}**, поздравляю тебя, ты победил игрока **{ctx.author.name}**! :tada:")
								end_embed.add_field(name=f"**[ПОБЕДИТЕЛЬ] {member.name}**", value=f"Награда: **+50 {emoji_coin}**\nОпыт: **+10**", inline=False)
								end_embed.add_field(name=f"**{ctx.author.name}**", value=f"Награда: **+5 {emoji_coin}**\nОпыт: **+1**", inline=False)
								await ctx.send(embed=end_embed)
								await add_money(member, ctx.author)
								return
							elif red_health <= 0:
								emoji_coin = self.bot.get_emoji(828277358690959380)
								end_embed=discord.Embed(title=f"Результаты", description=f"**{ctx.author.name}**, поздравляю тебя, ты победил игрока **{member.name}**! :tada:")
								end_embed.add_field(name=f"**[ПОБЕДИТЕЛЬ] {ctx.author.name}**", value=f"Награда: **+50 {emoji_coin}**\nОпыт: **+10**", inline=False)
								end_embed.add_field(name=f"**{member.name}**", value=f"Награда: **+5 {emoji_coin}**\nОпыт: **+1**", inline=False)
								await ctx.send(embed=end_embed)
								await add_money(ctx.author, member)
								return
							else:
								pass
						elif w == 5:
							await log_msg.clear_reaction("1️⃣")
							await log_msg.clear_reaction("2️⃣")
							await log_msg.clear_reaction("3️⃣")
							damage = random.randint(10,15)
							blue_health = blue_health - damage - plus_damage2
							await log2_msg.edit(content=f"**{member.name}** ударил **{ctx.author.name}** в ноги и нанёс **{damage + plus_damage2}** урона! У **{ctx.author.name}** осталось **{blue_health}** HP!")
							if blue_health <= 0:
								emoji_coin = self.bot.get_emoji(828277358690959380)
								end_embed=discord.Embed(title=f"Результаты", description=f"**{member.name}**, поздравляю тебя, ты победил игрока **{ctx.author.name}**! :tada:")
								end_embed.add_field(name=f"**[ПОБЕДИТЕЛЬ] {member.name}**", value=f"Награда: **+50 {emoji_coin}**\nОпыт: **+10**", inline=False)
								end_embed.add_field(name=f"**{ctx.author.name}**", value=f"Награда: **+5 {emoji_coin}**\nОпыт: **+1**", inline=False)
								await ctx.send(embed=end_embed)
								await add_money(member, ctx.author)
								return
							elif red_health <= 0:
								emoji_coin = self.bot.get_emoji(828277358690959380)
								end_embed=discord.Embed(title=f"Результаты", description=f"**{ctx.author.name}**, поздравляю тебя, ты победил игрока **{member.name}**! :tada:")
								end_embed.add_field(name=f"**[ПОБЕДИТЕЛЬ] {ctx.author.name}**", value=f"Награда: **+50 {emoji_coin}**\nОпыт: **+10**", inline=False)
								end_embed.add_field(name=f"**{member.name}**", value=f"Награда: **+5 {emoji_coin}**\nОпыт: **+1**", inline=False)
								await ctx.send(embed=end_embed)
								await add_money(ctx.author, member)
								return
							else:
								pass
						else:
							end_embed=discord.Embed(title=f"Ошибка!", description=f"Произошла ошибка. Просим уведомить об этом разработчика бота, прописав ```h!bug <описание бага>```, и в поле <описание бага> написать на каком ходу случилась ошибка, какие функции вы выбирали. Спасибо!")
							await ctx.send(embed=end_embed)
							return
					elif blue_block == 3:
						await log_msg.add_reaction("1️⃣")
						await log_msg.add_reaction("2️⃣")
						w = await wait_fight(bot=self.bot, tick=2, w_member_id=member.id, block=3, count=red_count)
						if w == 0:
							emoji_coin = self.bot.get_emoji(828277358690959380)
							end_embed=discord.Embed(title=f"Результаты", description=f"Время игрока **{member.name}** вышло.\nПобедитель: **{ctx.author.name}**")
							end_embed.add_field(name=f"**[ПОБЕДИТЕЛЬ] {ctx.author.name}**", value=f"Награда: **+50 {emoji_coin}**\nОпыт: **+10**", inline=False)
							end_embed.add_field(name=f"**{member.name}**", value=f"Награда: **+5 {emoji_coin}**\nОпыт: **+1**", inline=False)
							await ctx.send(embed=end_embed)
							await add_money(ctx.author, member)
							return
						elif w == 3:
							await log_msg.clear_reaction("1️⃣")
							await log_msg.clear_reaction("2️⃣")
							await log_msg.clear_reaction("3️⃣")
							damage = random.randint(15,30)
							blue_health = blue_health - damage - plus_damage2
							await log2_msg.edit(content=f"**{member.name}** ударил **{ctx.author.name}** в голову и нанёс **{damage + plus_damage2}** урона! У **{ctx.author.name}** осталось **{blue_health}** HP!")
							if blue_health <= 0:
								emoji_coin = self.bot.get_emoji(828277358690959380)
								end_embed=discord.Embed(title=f"Результаты", description=f"**{member.name}**, поздравляю тебя, ты победил игрока **{ctx.author.name}**! :tada:")
								end_embed.add_field(name=f"**[ПОБЕДИТЕЛЬ] {member.name}**", value=f"Награда: **+50 {emoji_coin}**\nОпыт: **+10**", inline=False)
								end_embed.add_field(name=f"**{ctx.author.name}**", value=f"Награда: **+5 {emoji_coin}**\nОпыт: **+1**", inline=False)
								await ctx.send(embed=end_embed)
								await add_money(member, ctx.author)
								return
							elif red_health <= 0:
								emoji_coin = self.bot.get_emoji(828277358690959380)
								end_embed=discord.Embed(title=f"Результаты", description=f"**{ctx.author.name}**, поздравляю тебя, ты победил игрока **{member.name}**! :tada:")
								end_embed.add_field(name=f"**[ПОБЕДИТЕЛЬ] {ctx.author.name}**", value=f"Награда: **+50 {emoji_coin}**\nОпыт: **+10**", inline=False)
								end_embed.add_field(name=f"**{member.name}**", value=f"Награда: **+5 {emoji_coin}**\nОпыт: **+1**", inline=False)
								await ctx.send(embed=end_embed)
								await add_money(ctx.author, member)
								return
							else:
								pass
						elif w == 4:
							await log_msg.clear_reaction("1️⃣")
							await log_msg.clear_reaction("2️⃣")
							await log_msg.clear_reaction("3️⃣")
							damage = random.randint(5,20)
							blue_health = blue_health - damage - plus_damage2
							await log2_msg.edit(content=f"**{member.name}** ударил **{ctx.author.name}** в туловище и нанёс **{damage + plus_damage2}** урона! У **{ctx.author.name}** осталось **{blue_health}** HP!")
							if blue_health <= 0:
								emoji_coin = self.bot.get_emoji(828277358690959380)
								end_embed=discord.Embed(title=f"Результаты", description=f"**{member.name}**, поздравляю тебя, ты победил игрока **{ctx.author.name}**! :tada:")
								end_embed.add_field(name=f"**[ПОБЕДИТЕЛЬ] {member.name}**", value=f"Награда: **+50 {emoji_coin}**\nОпыт: **+10**", inline=False)
								end_embed.add_field(name=f"**{ctx.author.name}**", value=f"Награда: **+5 {emoji_coin}**\nОпыт: **+1**", inline=False)
								await ctx.send(embed=end_embed)
								await add_money(member, ctx.author)
								return
							elif red_health <= 0:
								emoji_coin = self.bot.get_emoji(828277358690959380)
								end_embed=discord.Embed(title=f"Результаты", description=f"**{ctx.author.name}**, поздравляю тебя, ты победил игрока **{member.name}**! :tada:")
								end_embed.add_field(name=f"**[ПОБЕДИТЕЛЬ] {ctx.author.name}**", value=f"Награда: **+50 {emoji_coin}**\nОпыт: **+10**", inline=False)
								end_embed.add_field(name=f"**{member.name}**", value=f"Награда: **+5 {emoji_coin}**\nОпыт: **+1**", inline=False)
								await ctx.send(embed=end_embed)
								await add_money(ctx.author, member)
								return
							else:
								end_embed=discord.Embed(title=f"Ошибка!", description=f"Произошла ошибка. Просим уведомить об этом разработчика бота, прописав ```h!bug <описание бага>```, и в поле <описание бага> написать на каком ходу случилась ошибка, какие функции вы выбирали. Спасибо!")
								await ctx.send(embed=end_embed)
								return
						else:
							end_embed=discord.Embed(title=f"Ошибка!", description=f"Произошла ошибка. Просим уведомить об этом разработчика бота, прописав ```h!bug <описание бага>```, и в поле <описание бага> написать на каком ходу случилась ошибка, какие функции вы выбирали. Спасибо!")
							await ctx.send(embed=end_embed)
							return
					else:
						await log_msg.add_reaction("1️⃣")
						await log_msg.add_reaction("2️⃣")
						await log_msg.add_reaction("3️⃣")
						w = await wait_fight(bot=self.bot, tick=2, w_member_id=member.id, block=0, count=red_count)
						if w == 0:
							emoji_coin = self.bot.get_emoji(828277358690959380)
							end_embed=discord.Embed(title=f"Результаты", description=f"Время игрока **{member.name}** вышло.\nПобедитель: **{ctx.author.name}**")
							end_embed.add_field(name=f"**[ПОБЕДИТЕЛЬ] {ctx.author.name}**", value=f"Награда: **+50 {emoji_coin}**\nОпыт: **+10**", inline=False)
							end_embed.add_field(name=f"**{member.name}**", value=f"Награда: **+5 {emoji_coin}**\nОпыт: **+1**", inline=False)
							await ctx.send(embed=end_embed)
							await add_money(ctx.author, member)
							return
						elif w == 3:
							await log_msg.clear_reaction("1️⃣")
							await log_msg.clear_reaction("2️⃣")
							await log_msg.clear_reaction("3️⃣")
							damage = random.randint(15,30)
							blue_health = blue_health - damage - plus_damage2
							await log2_msg.edit(content=f"**{member.name}** ударил **{ctx.author.name}** в голову и нанёс **{damage + plus_damage2}** урона! У **{ctx.author.name}** осталось **{blue_health}** HP!")
							if blue_health <= 0:
								emoji_coin = self.bot.get_emoji(828277358690959380)
								end_embed=discord.Embed(title=f"Результаты", description=f"**{member.name}**, поздравляю тебя, ты победил игрока **{ctx.author.name}**! :tada:")
								end_embed.add_field(name=f"**[ПОБЕДИТЕЛЬ] {member.name}**", value=f"Награда: **+50 {emoji_coin}**\nОпыт: **+10**", inline=False)
								end_embed.add_field(name=f"**{ctx.author.name}**", value=f"Награда: **+5 {emoji_coin}**\nОпыт: **+1**", inline=False)
								await ctx.send(embed=end_embed)
								await add_money(member, ctx.author)
								return
							elif red_health <= 0:
								emoji_coin = self.bot.get_emoji(828277358690959380)
								end_embed=discord.Embed(title=f"Результаты", description=f"**{ctx.author.name}**, поздравляю тебя, ты победил игрока **{member.name}**! :tada:")
								end_embed.add_field(name=f"**[ПОБЕДИТЕЛЬ] {ctx.author.name}**", value=f"Награда: **+50 {emoji_coin}**\nОпыт: **+10**", inline=False)
								end_embed.add_field(name=f"**{member.name}**", value=f"Награда: **+5 {emoji_coin}**\nОпыт: **+1**", inline=False)
								await ctx.send(embed=end_embed)
								await add_money(ctx.author, member)
								return
							else:
								pass
						elif w == 4:
							await log_msg.clear_reaction("1️⃣")
							await log_msg.clear_reaction("2️⃣")
							await log_msg.clear_reaction("3️⃣")
							damage = random.randint(5,20)
							blue_health = blue_health - damage - plus_damage2
							await log2_msg.edit(content=f"**{member.name}** ударил **{ctx.author.name}** в туловище и нанёс **{damage + plus_damage2}** урона! У **{ctx.author.name}** осталось **{blue_health}** HP!")
							if blue_health <= 0:
								emoji_coin = self.bot.get_emoji(828277358690959380)
								end_embed=discord.Embed(title=f"Результаты", description=f"**{member.name}**, поздравляю тебя, ты победил игрока **{ctx.author.name}**! :tada:")
								end_embed.add_field(name=f"**[ПОБЕДИТЕЛЬ] {member.name}**", value=f"Награда: **+50 {emoji_coin}**\nОпыт: **+10**", inline=False)
								end_embed.add_field(name=f"**{ctx.author.name}**", value=f"Награда: **+5 {emoji_coin}**\nОпыт: **+1**", inline=False)
								await ctx.send(embed=end_embed)
								await add_money(member, ctx.author)
								return
							elif red_health <= 0:
								emoji_coin = self.bot.get_emoji(828277358690959380)
								end_embed=discord.Embed(title=f"Результаты", description=f"**{ctx.author.name}**, поздравляю тебя, ты победил игрока **{member.name}**! :tada:")
								end_embed.add_field(name=f"**[ПОБЕДИТЕЛЬ] {ctx.author.name}**", value=f"Награда: **+50 {emoji_coin}**\nОпыт: **+10**", inline=False)
								end_embed.add_field(name=f"**{member.name}**", value=f"Награда: **+5 {emoji_coin}**\nОпыт: **+1**", inline=False)
								await ctx.send(embed=end_embed)
								await add_money(ctx.author, member)
								return
							else:
								pass
						elif w == 5:
							await log_msg.clear_reaction("1️⃣")
							await log_msg.clear_reaction("2️⃣")
							await log_msg.clear_reaction("3️⃣")
							damage = random.randint(10,15)
							blue_health = blue_health - damage - plus_damage2
							await log2_msg.edit(content=f"**{member.name}** ударил **{ctx.author.name}** в ноги и нанёс **{damage + plus_damage2}** урона! У **{ctx.author.name}** осталось **{blue_health}** HP!")
							if blue_health <= 0:
								emoji_coin = self.bot.get_emoji(828277358690959380)
								end_embed=discord.Embed(title=f"Результаты", description=f"**{member.name}**, поздравляю тебя, ты победил игрока **{ctx.author.name}**! :tada:")
								end_embed.add_field(name=f"**[ПОБЕДИТЕЛЬ] {member.name}**", value=f"Награда: **+50 {emoji_coin}**\nОпыт: **+10**", inline=False)
								end_embed.add_field(name=f"**{ctx.author.name}**", value=f"Награда: **+5 {emoji_coin}**\nОпыт: **+1**", inline=False)
								await ctx.send(embed=end_embed)
								await add_money(member, ctx.author)
								return
							elif red_health <= 0:
								emoji_coin = self.bot.get_emoji(828277358690959380)
								end_embed=discord.Embed(title=f"Результаты", description=f"**{ctx.author.name}**, поздравляю тебя, ты победил игрока **{member.name}**! :tada:")
								end_embed.add_field(name=f"**[ПОБЕДИТЕЛЬ] {ctx.author.name}**", value=f"Награда: **+50 {emoji_coin}**\nОпыт: **+10**", inline=False)
								end_embed.add_field(name=f"**{member.name}**", value=f"Награда: **+5 {emoji_coin}**\nОпыт: **+1**", inline=False)
								await ctx.send(embed=end_embed)
								await add_money(ctx.author, member)
								return
							else:
								pass
						else:
							end_embed=discord.Embed(title=f"Ошибка!", description=f"Произошла ошибка. Просим уведомить об этом разработчика бота, прописав ```h!bug <описание бага>```, и в поле <описание бага> написать на каком ходу случилась ошибка, какие функции вы выбирали. Спасибо!")
							await ctx.send(embed=end_embed)
							return
				elif w == 7:
					await log2_msg.edit(content=f"**{member.name}** решил защищаться!")
					await log_msg.clear_reaction("🗡")
					await log_msg.clear_reaction("🛡")
					await log_msg.clear_reaction("🩹")
					log_red_attack_embed=discord.Embed(title=f":red_square: **КРАСНЫЙ** :red_square:")
					log_red_attack_embed.set_author(name=f"Ход: {step}")
					log_red_attack_embed.add_field(name=f"Имя бойца:", value=f"**{member.name}**", inline=False)
					log_red_attack_embed.add_field(name=f"Уровень бойца:", value=f"**{lvl_red}**", inline=False)
					log_red_attack_embed.add_field(name=f"Здоровье:", value=f"**{red_health} HP**", inline=False)
					if show_gun_info_red != 0:
						log_red_attack_embed.add_field(name=f"Оружие:", value=f"**{red_gun}**", inline=False)
					else:
						pass
					if show_shield_info_red != 0:
						log_red_attack_embed.add_field(name=f"Броня:", value=f"**{red_shield}**", inline=False)
					else:
						pass
					log_red_attack_embed.add_field(name=f"Аптечки:", value=f"**{red_count}**", inline=False)
					log_red_attack_embed.add_field(name=f"Вы можете защитить:", value=f":one: - голову\n:two: - туловище\n:three: - ноги", inline=False)
					await log_msg.edit(embed=log_red_attack_embed)
					await log_msg.add_reaction("1️⃣")
					await log_msg.add_reaction("2️⃣")
					await log_msg.add_reaction("3️⃣")
					w = await wait_fight(bot=self.bot, tick=2, w_member_id=member.id, block=0, count=red_count)
					if w == 0:
						emoji_coin = self.bot.get_emoji(828277358690959380)
						end_embed=discord.Embed(title=f"Результаты", description=f"Время игрока **{member.name}** вышло.\nПобедитель: **{ctx.author.name}**")
						end_embed.add_field(name=f"**[ПОБЕДИТЕЛЬ] {ctx.author.name}**", value=f"Награда: **+50 {emoji_coin}**\nОпыт: **+10**", inline=False)
						end_embed.add_field(name=f"**{member.name}**", value=f"Награда: **+5 {emoji_coin}**\nОпыт: **+1**", inline=False)
						await ctx.send(embed=end_embed)
						await add_money(ctx.author, member)
						return
					elif w == 3:
						await log_msg.clear_reaction("1️⃣")
						await log_msg.clear_reaction("2️⃣")
						await log_msg.clear_reaction("3️⃣")
						red_block = 1
						await log2_msg.edit(content=f"**{member.name}** защитил **голову**")
					elif w == 4:
						await log_msg.clear_reaction("1️⃣")
						await log_msg.clear_reaction("2️⃣")
						await log_msg.clear_reaction("3️⃣")
						red_block = 2
						await log2_msg.edit(content=f"**{member.name}** защитил **туловище**")
					elif w == 5:
						await log_msg.clear_reaction("1️⃣")
						await log_msg.clear_reaction("2️⃣")
						await log_msg.clear_reaction("3️⃣")
						red_block = 3
						await log2_msg.edit(content=f"**{member.name}** защитил **ноги**")
					else:
						end_embed=discord.Embed(title=f"Ошибка!", description=f"Произошла ошибка. Просим уведомить об этом разработчика бота, прописав ```h!bug <описание бага>```, и в поле <описание бага> написать на каком ходу случилась ошибка, какие функции вы выбирали. Спасибо!")
						await ctx.send(embed=end_embed)
						return
				elif w == 8:
					await log2_msg.edit(content=f"**{ctx.author.name}** решил подлечиться!")
					await log_msg.clear_reaction("🗡")
					await log_msg.clear_reaction("🛡")
					await log_msg.clear_reaction("🩹")
					if data[str(member.id)]["items"]["31"]["count"] > 0:
						blue_health += 20
						data[str(member.id)]["items"]["31"]["count"] -= 1
						red_count -= 1
						with open('/root/bot/databases/fight.json', 'w') as f:
							json.dump(data,f,indent=4)
						await log2_msg.edit(content=f"**{member.name}** подлечился!")
					else:
						end_embed=discord.Embed(title=f"Ошибка!", description=f"Произошла ошибка. Просим уведомить об этом разработчика бота, прописав ```h!bug <описание бага>```, и в поле <описание бага> написать на каком ходу случилась ошибка, какие функции вы выбирали. Спасибо!")
						await ctx.send(embed=end_embed)
						return
				else:
					end_embed=discord.Embed(title=f"Ошибка!", description=f"Произошла ошибка. Просим уведомить об этом разработчика бота, прописав ```h!bug <описание бага>```, и в поле <описание бага> написать на каком ходу случилась ошибка, какие функции вы выбирали. Спасибо!")
					await ctx.send(embed=end_embed)
					return
				blue_block = 0
		except Exception as e:
			print(e)

	@__fight.error
	async def fight_error(self, ctx, error):
		with open('/root/bot/databases/prefixes.json', 'r') as f:
			data = json.load(f)
			p = data[str(ctx.guild.id)]
		if isinstance(error, commands.MissingRequiredArgument) or isinstance(error, commands.TooManyArguments) or isinstance(error, commands.BadArgument) or isinstance(error, commands.MemberNotFound) or isinstance(error, commands.UserNotFound) or isinstance(error, commands.MessageNotFound) or isinstance(error, commands.ChannelNotReadable) or isinstance(error, commands.ChannelNotFound)  or isinstance(error, commands.EmojiNotFound) or isinstance(error, commands.PartialEmojiConversionFailure) or isinstance(error, commands.MissingPermissions) or isinstance(error, commands.BotMissingPermissions) or isinstance(error, commands.BadUnionArgument) or isinstance(error, commands.ArgumentParsingError):
			embed=discord.Embed(title=f'Команда **"{p}fight" `||` "{p}битва"**', description="**Сразиться с выбранным юзером**\n\n\n", color=discord.Color.blue(), timestamp=datetime.datetime.utcnow())
			embed.add_field(name="**Использование:**", value=f"`{p}fight <@Юзер>`", inline=False)
			embed.add_field(name=f"**Примеры:**\n`{p}fight @{ctx.guild.owner}`", value=":white_small_square: Начать битву с выбранным юзером", inline=False)
			embed.add_field(name=f"`{p}fight {ctx.guild.owner.id}`", value=":white_small_square: Начать битву с выбранным юзером по его id", inline=False)
			embed.set_footer(text=f'{self.bot.user.name}', icon_url=self.bot.user.avatar_url)
			await ctx.send(embed=embed)
		elif isinstance(error, commands.CommandOnCooldown):
			emoji_no = self.bot.get_emoji(785095586671230986)
			embed=discord.Embed(title=f"{emoji_no} Ошибка!", description=f"Включена задержка!\nПодождите {round(error.retry_after, 1)} секунд", color=discord.Color.red())
			await ctx.send(embed=embed)
			return

def setup(bot):
	bot.add_cog(Command(bot))