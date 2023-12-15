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

def recieve_work_from_id(work_id:int):
    if work_id == 1:
        work_name = "Дворник"
        work_need_lvl = 5
        work_salary = 150
    elif work_id == 2:
        work_name = "Сторож"
        work_need_lvl = 7
        work_salary = 200
    elif work_id == 3:
        work_name = "Уборщик"
        work_need_lvl = 9
        work_salary = 250
    elif work_id == 4:
        work_name = "Врач"
        work_need_lvl = 11
        work_salary = 300
    elif work_id == 5:
        work_name = "Учитель"
        work_need_lvl = 13
        work_salary = 350
    elif work_id == 6:
        work_name = "Кассир"
        work_need_lvl = 15
        work_salary = 400
    elif work_id == 7:
        work_name = "Водитель"
        work_need_lvl = 17
        work_salary = 450
    elif work_id == 8:
        work_name = "Грузчик"
        work_need_lvl = 19
        work_salary = 500
    elif work_id == 9:
        work_name = "Повар"
        work_need_lvl = 21
        work_salary = 600
    elif work_id == 10:
        work_name = "Менеджер по продажам"
        work_need_lvl = 23
        work_salary = 700
    elif work_id == 11:
        work_name = "Оператор колл-центра"
        work_need_lvl = 25
        work_salary = 750
    elif work_id == 12:
        work_name = "Курьер"
        work_need_lvl = 27
        work_salary = 800
    elif work_id == 13:
        work_name = "Репетитор"
        work_need_lvl = 29
        work_salary = 850
    elif work_id == 14:
        work_name = "Программист"
        work_need_lvl = 31
        work_salary = 900
    elif work_id == 15:
        work_name = "Администратор"
        work_need_lvl = 33
        work_salary = 1000
    return work_name, work_need_lvl, work_salary

class Command(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=["work", "работать"])
    @commands.guild_only()
    async def __work(self, ctx, work_id: int=None, to_do=None):
        try:
            status = check_category(str(ctx.guild.id), "Mini-games")
            if status == 0:
                return
            emoji_coin = self.bot.get_emoji(828277358690959380)
            if work_id == None:
                if to_do == None:
                    description = f"""**Доступные вакансии**

                    ***Дворник***
                    • Доступ: от `5` уровня
                    • Оплата: 150 {emoji_coin} / 7 д.
                    • ID: 1

                    ***Сторож***
                    • Доступ: от `7` уровня
                    • Оплата: 200 {emoji_coin} / 7 д.
                    • ID: 2

                    ***Уборщик***
                    • Доступ: от `9` уровня
                    • Оплата: 250 {emoji_coin} / 7 д.
                    • ID: 3

                    ***Врач***
                    • Доступ: от `11` уровня
                    • Оплата: 300 {emoji_coin} / 7 д.
                    • ID: 4

                    ***Учитель***
                    • Доступ: от `13` уровня
                    • Оплата: 350 {emoji_coin} / 7 д.
                    • ID: 5

                    ***Кассир***
                    • Доступ: от `15` уровня
                    • Оплата: 400 {emoji_coin} / 7 д.
                    • ID: 6

                    ***Водитель***
                    • Доступ: от `17` уровня
                    • Оплата: 450 {emoji_coin} / 7 д.
                    • ID: 7

                    ***Грузчик***
                    • Доступ: от `19` уровня
                    • Оплата: 500 {emoji_coin} / 7 д.
                    • ID: 8

                    ***Повар***
                    • Доступ: от `21` уровня
                    • Оплата: 600 {emoji_coin} / 7 д.
                    • ID: 9

                    ***Менеджер по продажам***
                    • Доступ: от `23` уровня
                    • Оплата: 700 {emoji_coin} / 7 д.
                    • ID: 10

                    ***Оператор колл-центра***
                    • Доступ: от `25` уровня
                    • Оплата: 750 {emoji_coin} / 7 д.
                    • ID: 11

                    ***Курьер***
                    • Доступ: от `27` уровня
                    • Оплата: 800 {emoji_coin} / 7 д.
                    • ID: 12

                    ***Репетитор***
                    • Доступ: от `29` уровня
                    • Оплата: 850 {emoji_coin} / 7 д.
                    • ID: 13

                    ***Программист***
                    • Доступ: от `31` уровня
                    • Оплата: 900 {emoji_coin} / 7 д.
                    • ID: 14

                    ***Администратор***
                    • Доступ: от `33` уровня
                    • Оплата: 1000 {emoji_coin} / 7 д.
                    • ID: 15"""
                    embed=discord.Embed(title="Работа", description=description, color=discord.Color.blue())
                    await ctx.send(embed=embed)
                    return
            if not work_id in range(1, 16):
                emoji = self.bot.get_emoji(744165695662850170)
                embed=discord.Embed(title=f"{emoji} Ошибка!", description="Неверный ID работы!", color=discord.Color.red())
                await ctx.send(embed=embed)
                return
            with open('/root/bot/databases/fight.json', 'r') as f:
                data = json.load(f)
            if not str(ctx.author.id) in data:
                data[str(ctx.author.id)] = {}
                data[str(ctx.author.id)]["exp"] = 0
                data[str(ctx.author.id)]["lvl"] = 1
                data[str(ctx.author.id)]["money"] = 0
                data[str(ctx.author.id)]["items"] = {}
            if to_do == "get":
                work = recieve_work_from_id(work_id)
                if data[str(ctx.author.id)]['lvl'] < work[1]:
                    emoji = self.bot.get_emoji(744165695662850170)
                    embed=discord.Embed(title=f"{emoji} Ошибка!", description=f"Нехватает уровня для устройства на работу!\nНеобходимый уровень: `{work[1]}`", color=discord.Color.red())
                    await ctx.send(embed=embed)
                    return
                if data[str(ctx.author.id)]["work"]["type"] == "work":
                    emoji = self.bot.get_emoji(744165695662850170)
                    w1 = recieve_work_from_id(data[str(ctx.author.id)]["work"]["name"])
                    embed=discord.Embed(title=f"{emoji} Ошибка!", description=f"Сначала увольтесь с работы `{w1[0]}`!", color=discord.Color.red())
                    await ctx.send(embed=embed)
                    return
                if not "work" in data[str(ctx.author.id)]:
                    data[str(ctx.author.id)]["work"] = {}
                date = str(datetime.date.today() + datetime.timedelta(days=7))
                data[str(ctx.author.id)]["work"]["name"] = work_id
                data[str(ctx.author.id)]["work"]["type"] = "work"
                data[str(ctx.author.id)]["work"]["salary"] = work[2]
                data[str(ctx.author.id)]["work"]["time_to_next_salary"] = date
                emoji_yes = self.bot.get_emoji(785095546146652180)
                embed=discord.Embed(title=f"{emoji_yes} Успешно!", color=discord.Color.green(), description=f"Вы устроились на работу `{work[0]}`")
                await ctx.send(embed=embed)
            elif to_do == "работать":
                work = recieve_work_from_id(work_id)
                if data[str(ctx.author.id)]['lvl'] < work[1]:
                    emoji = self.bot.get_emoji(744165695662850170)
                    embed=discord.Embed(title=f"{emoji} Ошибка!", description=f"Нехватает уровня для устройства на работу!\nНеобходимый уровень: `{work[1]}`", color=discord.Color.red())
                    await ctx.send(embed=embed)
                    return
                if data[str(ctx.author.id)]["work"]["type"] == "work":
                    emoji = self.bot.get_emoji(744165695662850170)
                    w1 = recieve_work_from_id(data[str(ctx.author.id)]["work"]["name"])
                    embed=discord.Embed(title=f"{emoji} Ошибка!", description=f"Сначала увольтесь с работы {w1[0]}!", color=discord.Color.red())
                    await ctx.send(embed=embed)
                    return
                if not "work" in data[str(ctx.author.id)]:
                    data[str(ctx.author.id)]["work"] = {}
                date = str(datetime.date.today() + datetime.timedelta(days=7))
                data[str(ctx.author.id)]["work"]["name"] = work_id
                data[str(ctx.author.id)]["work"]["type"] = "work"
                data[str(ctx.author.id)]["work"]["salary"] = work[2]
                data[str(ctx.author.id)]["work"]["time_to_next_salary"] = date
                emoji_yes = self.bot.get_emoji(785095546146652180)
                embed=discord.Embed(title=f"{emoji_yes} Успешно!", color=discord.Color.green(), description=f"Вы устроились на работу `{work[0]}`")
                await ctx.send(embed=embed)
            elif to_do == "quit":
                work = recieve_work_from_id(work_id)
                if not "work" in data[str(ctx.author.id)]:
                    emoji = self.bot.get_emoji(744165695662850170)
                    embed=discord.Embed(title=f"{emoji} Ошибка!", description=f"Вы ещё не устроены ни на какую работу!", color=discord.Color.red())
                    await ctx.send(embed=embed)
                    return
                if data[str(ctx.author.id)]["work"]["name"] != work_id:
                    emoji = self.bot.get_emoji(744165695662850170)
                    embed=discord.Embed(title=f"{emoji} Ошибка!", description=f"Вы не работаете на этой работе!", color=discord.Color.red())
                    await ctx.send(embed=embed)
                    return
                if data[str(ctx.author.id)]["work"]["type"] == "fired":
                    emoji = self.bot.get_emoji(744165695662850170)
                    embed=discord.Embed(title=f"{emoji} Ошибка!", description=f"Вы ещё не устроены ни на какую работу!", color=discord.Color.red())
                    await ctx.send(embed=embed)
                    return
                data[str(ctx.author.id)]["work"]["type"] = "fired"
                data[str(ctx.author.id)]["work"]["salary"] = 0
                data[str(ctx.author.id)]["work"]["time_to_next_salary"] = "0"
                emoji_yes = self.bot.get_emoji(785095546146652180)
                embed=discord.Embed(title=f"{emoji_yes} Успешно!", color=discord.Color.green(), description=f"Вы покинули работу `{work[0]}`")
                await ctx.send(embed=embed)
            elif to_do == "уволиться":
                work = recieve_work_from_id(work_id)
                if not "work" in data[str(ctx.author.id)]:
                    emoji = self.bot.get_emoji(744165695662850170)
                    embed=discord.Embed(title=f"{emoji} Ошибка!", description=f"Вы ещё не устроены ни на какую работу!", color=discord.Color.red())
                    await ctx.send(embed=embed)
                    return
                if data[str(ctx.author.id)]["work"]["name"] != work_id:
                    emoji = self.bot.get_emoji(744165695662850170)
                    embed=discord.Embed(title=f"{emoji} Ошибка!", description=f"Вы не работаете на этой работе!", color=discord.Color.red())
                    await ctx.send(embed=embed)
                    return
                if data[str(ctx.author.id)]["work"]["type"] == "fired":
                    emoji = self.bot.get_emoji(744165695662850170)
                    embed=discord.Embed(title=f"{emoji} Ошибка!", description=f"Вы ещё не устроены ни на какую работу!", color=discord.Color.red())
                    await ctx.send(embed=embed)
                    return
                data[str(ctx.author.id)]["work"]["type"] = "fired"
                data[str(ctx.author.id)]["work"]["salary"] = 0
                data[str(ctx.author.id)]["work"]["time_to_next_salary"] = "0"
                emoji_yes = self.bot.get_emoji(785095546146652180)
                embed=discord.Embed(title=f"{emoji_yes} Успешно!", color=discord.Color.green(), description=f"Вы покинули работу `{work[0]}`")
                await ctx.send(embed=embed)
            else:
                emoji = self.bot.get_emoji(744165695662850170)
                embed=discord.Embed(title=f"{emoji} Ошибка!", description="Неверный аргумент действия!\nДоступные аргументы:\n\t`get`, `работать` - устроиться на работу\n\t`quit`, `уволиться` - уволиться с работы", color=discord.Color.red())
                await ctx.send(embed=embed)
                return
            with open('/root/bot/databases/fight.json', 'w') as f:
                json.dump(data,f,indent=4)
        except Exception as e:
            await ctx.send(e)

    @__work.error
    async def work_error(self, ctx, error):
        with open('/root/bot/databases/prefixes.json', 'r') as f:
            data = json.load(f)
            p = data[str(ctx.guild.id)]
        if isinstance(error, commands.MissingRequiredArgument) or isinstance(error, commands.TooManyArguments) or isinstance(error, commands.BadArgument) or isinstance(error, commands.MemberNotFound) or isinstance(error, commands.UserNotFound) or isinstance(error, commands.MessageNotFound) or isinstance(error, commands.ChannelNotReadable) or isinstance(error, commands.ChannelNotFound)  or isinstance(error, commands.EmojiNotFound) or isinstance(error, commands.PartialEmojiConversionFailure) or isinstance(error, commands.MissingPermissions) or isinstance(error, commands.BotMissingPermissions) or isinstance(error, commands.BadUnionArgument) or isinstance(error, commands.ArgumentParsingError):
            embed=discord.Embed(title=f'Команда **"{p}work" `||` "{p}работать"**', description="**Устроиться/уволиться с работы**\n\n\n", color=discord.Color.blue(), timestamp=datetime.datetime.utcnow())
            embed.add_field(name="**Использование:**", value=f"`{p}work <work_id> <get | quit | работать | уволиться>`", inline=False)
            embed.add_field(name=f"**Примеры:**\n`{p}work 1 get`", value=":white_small_square: Устроиться на работу дворником (ID: 1)", inline=False)
            embed.set_footer(text=f'{self.bot.user.name}', icon_url=self.bot.user.avatar_url)
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Command(bot))