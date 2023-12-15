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

	@commands.command(aliases=["help", "h", "хелп", "х"])
	@commands.guild_only()
	async def __help(self, ctx, screen: int=None):
		with open('/root/bot/databases/prefixes.json', 'r') as f:
			data = json.load(f)
			p = data[str(ctx.guild.id)]
		emoji1 = self.bot.get_emoji(839894675208142858)
		emoji2 = self.bot.get_emoji(839894726404210708)
		emoji3 = self.bot.get_emoji(839894794058334298)
		emoji4 = self.bot.get_emoji(839894635014520842)
		emoji5 = self.bot.get_emoji(839894700978208776)
		emoji6 = self.bot.get_emoji(839894765410844672)
		emoji7 = self.bot.get_emoji(839894846131011584)
		test_msg = f"На данный момент идёт бета-тестирование новых возможностей на наличие багов и ошибок. Если вы нашли баг или ошибку, помогите нам, написав **{p}bug <Описание бага>**\n\n"
		if screen == None:
			embed=discord.Embed(title=f"{emoji1} Помощь || Общее", description=f"{test_msg}**┏** `{p}help 1` **─︎** Команды модуля информация\n**┣** `{p}help 2` **─︎** Команды модуля сетап\n**┣** `{p}help 3` **─︎** Команды модуля утилиты\n**┣** `{p}help 4` **─︎** Команды модуля модерация\n**┣** `{p}help 5` **─︎** Команды модуля РП\n**┣** `{p}help 6` **─︎** Команды модуля картинки\n**┣** `{p}help 7` **─︎** Команды модуля фан\n**┗** `{p}help 8` **─︎** Команды модуля мини-игры\n", color=discord.Color.blue())
		elif screen == 1:
			embed=discord.Embed(title=f"{emoji1} Информация", description=f"{test_msg}**┏** `{p}help` **─︎** Информация о командах бота\n**┣** `{p}info` **─︎** Информация о боте\n**┣** `{p}stat` **─︎** Статистика бота\n**┣** `{p}authors` **─︎** Авторы бота\n**┣** `{p}vote` **─︎** Поддержать бота\n**┣** `{p}invite` **─︎** Пригласить бота\n**┗** `{p}support` **─︎** Сервер тех.поддержки бота", color=discord.Color.blue())	
		elif screen == 2:
			embed=discord.Embed(title=f"{emoji2} Сетап", description=f"{test_msg}**┏** `{p}set-prefix` **─︎** Изменить префикс бота\n**┣** `{p}categories` **─︎** Управлять категориями\n**┣** `{p}welcome` **─︎** вкл./откл. приветствия\n**┣** `{p}bye` **─︎** вкл./откл. прощания\n**┗** `{p}audit` **─︎** вкл./откл. аудит", color=discord.Color.blue())
		elif screen == 3:
			embed=discord.Embed(title=f"{emoji3} Утилиты", description=f"{test_msg}**┏** `{p}user` **─︎** Информация о юзере\n**┣** `{p}server` **─︎** Информация о сервере\n**┣** `{p}inviteinfo` **─︎** Информация об инвайте\n**┣** `{p}roleinfo` **─︎** Информация о роли\n**┣** `{p}channelinfo` **─︎** Информация о канале\n**┣** `{p}avatar` **─︎** Аватар выбранного юзера\n**┣** `{p}bug` **─︎** Информировать о баге\n**┣** `{p}rand` **─︎** Рандомное число\n**┣** `{p}status` **─︎** Увидеть статус юзера\n**┗** `{p}weather` **─︎** Информация о погоде", color=discord.Color.blue())
		elif screen == 4:
			embed=discord.Embed(title=f"{emoji2} Модерация", description=f"{test_msg}**┏** `{p}clear` **─︎** Очистка сообщений\n**┣** `{p}kick` **─︎** Кик выбранного юзера\n**┣** `{p}ban` **─︎** Бан выбранного юзера\n**┣** `{p}unban` **─︎** Разбан выбранного юзера\n**┣** `{p}nuke` **─︎** Удалить все сообщения в канале\n**┗** `{p}slowmode` **─︎** Установить слоумод", color=discord.Color.blue())
		elif screen == 5:
			embed=discord.Embed(title=f"{emoji4} RP команды", description=f"{test_msg}**┏** `{p}star` **─︎** Подарить юзеру звезду\n**┣** `{p}lol` **─︎** Посмеяться\n**┣** `{p}smoke` **─︎** Курить\n**┣** `{p}tea` **─︎** Пить чай\n**┣** `{p}look` **─︎** Наблюдать\n**┣** `{p}panic` **─︎** Паниковать\n**┣** `{p}sleep` **─︎** Спать\n**┣** `{p}tickle` **─︎** Пощекотать\n**┣** `{p}feed` **─︎** Покормить\n**┣** `{p}poke` **─︎** Тыкнуть\n**┣** `{p}kiss` **─︎** Поцеловать юзера\n**┣** `{p}pat` **─︎** Погладить юзера\n**┣** `{p}punch` **─︎** Ударить юзера\n**┣** `{p}hug` **─︎** Обнять юзера\n**┣** `{p}high-five` **─︎** Дать пять юзеру\n**┣** `{p}scare` **─︎** Испугаться\n**┣** `{p}apologize` **─︎** Извиниться перед юзером\n**┣** `{p}bite` **─︎** Укусить юзера\n**┣** `{p}lick` **─︎** Лизнуть юзера\n**┣** `{p}congratulate` **─︎** Поздравить юзера\n**┣** `{p}shake-hand` **─︎** Пожать руку юзеру\n**┣** `{p}compliment` **─︎** Похвалить юзера\n**┣** `{p}smell` **─︎** Понюхать юзера\n**┣** `{p}pinch` **─︎** Ущипнуть юзера\n**┗** `{p}cry` **─︎** Заплакать", color=discord.Color.blue())
		elif screen == 6:
			embed=discord.Embed(title=f"{emoji5} Картинки", description=f"{test_msg}**┏** `{p}bird` **─︎** Картинка птицы\n**┣** `{p}dog` **─︎** Картинка собаки\n**┣** `{p}cat` **─︎** картинка кота\n**┣** `{p}fox` **─︎** Картинка лисы\n**┣** `{p}bear` **─︎** Картинка медведя\n**┣** `{p}panda` **─︎** Картинка панды\n**┣** `{p}parrot` **─︎** Картинка попугая\n**┣** `{p}sheep` **─︎** Картинка овцы\n**┣** `{p}kangaroo` **─︎** Картинка кенгуру\n**┣** `{p}giraffe` **─︎** Картинка жирафа\n**┣** `{p}camel` **─︎** Картинка верблюда\n**┣** `{p}elephant` **─︎** Картинка слона\n**┣** `{p}zebra` **─︎** Картинка зебры\n**┣** `{p}crocodile` **─︎** Картинка крокодила\n**┣** `{p}whale` **─︎** Картинка кита\n**┣** `{p}dolphin` **─︎** Картинка дельфина\n**┣** `{p}crab` **─︎** Картинка краба\n**┣** `{p}horse` **─︎** Картинка лошади\n**┣** `{p}wolf` **─︎** Картинка волка\n**┣** `{p}owl` **─︎** Картинка совы\n**┣** `{p}duck` **─︎** Картинка утки\n**┣** `{p}penguin` **─︎** Картинка пингвина\n**┣** `{p}chicken` **─︎** Картинка курицы\n**┣** `{p}monkey` **─︎** Картинка обезьяны\n**┣** `{p}frog` **─︎** Картинка лягушки\n**┣** `{p}pig` **─︎** Картинка свиньи\n**┣** `{p}cow` **─︎** Картинка коровы\n**┣** `{p}lion` **─︎** Картинка льва\n**┣** `{p}tiger` **─︎** Картинка тигра\n**┗** `{p}rabbit` **─︎** Картинка зайца", color=discord.Color.blue())
		elif screen == 7:
			embed=discord.Embed(title=f"{emoji6} Фан", description=f"{test_msg}**┏** `{p}gay` **─︎** Узнать насколько юзер ГеЙ\n**┣** `{p}holy` **─︎** Узнать насколько юзер святой\n**┣** `{p}IQ` **─︎** Узнать айкью юзера\n**┣** `{p}moder` **─︎** Шанс юзера быть модер-ом\n**┣** `{p}say` **─︎** Написать текст\n**┣** `{p}spoiler` **─︎** Написать текст с спойлером\n**┣** `{p}question` **─︎** Рандомный ответ на вопрос\n**┗** `{p}embed` **─︎** Эмбед-конструктор", color=discord.Color.blue())
		elif screen == 8:
			embed=discord.Embed(title=f"{emoji7} Битвы", description=f"{test_msg}**┏** `{p}fight` **─︎** Начать битву с юзером\n**┣** `{p}shop` **─︎** Магазин\n**┣** `{p}buy-item` **─︎** Купить предмет\n**┣** `{p}wear-item` **─︎** Надеть предмет\n**┣** `{p}sell-item` **─︎** Продать предмет\n**┣** `{p}work` **─︎** Работа\n**┣** `{p}daily` **─︎** Дневная награда\n**┣** `{p}profile` **─︎** Ваш профиль\n**┗** `{p}imposter` **─︎** Мини-игра", color=discord.Color.blue())
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))