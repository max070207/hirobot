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

api_key = "6c6c8c79b3fefde7b6e4f4ad9dd42621"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

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

	@commands.command(aliases=["weather", "погода"])
	@commands.guild_only()
	async def __weather(self, ctx, *, city):
		status = check_category(str(ctx.guild.id), "Utilities")
		if status == 0:
			return
		city_name = city
		complete_url = base_url + "appid=" + api_key + "&q=" + city_name
		response = requests.get(complete_url)
		x = response.json()
		channel = ctx.message.channel
		if x["cod"] != "404":
			y = x["main"]
			current_temp = y["temp"]
			current_temp_feels_like = y["feels_like"]
			current_temp_max = y["temp_max"]
			current_temp_min = y["temp_min"]
			current_temp_c = current_temp - 273.15
			current_temp_feels_like_c = current_temp_feels_like - 273.15
			current_temp_min_c = current_temp_min - 273.15
			current_temp_max_c = current_temp_max - 273.15
			current_temp_c1 = round(current_temp_c, 12)
			current_temp_feels_like_c1 = round(current_temp_feels_like_c, 12)
			current_temp_min_c1 = round(current_temp_min_c, 12)
			current_temp_max_c1 = round(current_temp_max_c, 12)
			current_pressure = y["pressure"]
			current_humidity = y["humidity"]
			current_name = x["name"]
			w = x["weather"]
			v = x["wind"]
			current_wind_speed = v["speed"]
			u = x["clouds"]
			current_clouds = u["all"]
			embed = discord.Embed(title=f"Погода в городе {city}", color=discord.Color.blue(), timestamp=ctx.message.created_at,)
			embed.add_field(name="Температура:", value=f"Температура: `{current_temp_c1}°C`\nОщущается как: `{current_temp_feels_like_c1}°C`\nМакс. температура: `{current_temp_max_c1}°C`\nМин. температура: `{current_temp_min_c1}°C`", inline=False)
			embed.add_field(name="Влажность:", value=f"**{current_humidity}%**", inline=False)
			embed.add_field(name="Атмосферное давление:", value=f"**{current_pressure}hPa**", inline=False)
			embed.add_field(name="Облачность:", value=f"**{current_clouds}%**", inline=False)
			embed.add_field(name="Скорость ветра:", value=f"**{current_wind_speed}м/с**", inline=False)
			embed.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
			await channel.send(embed=embed)
		else:
			emoji_no = self.bot.get_emoji(744165695662850170)
			embed=discord.Embed(colour=discord.Color.red())
			embed.add_field(name=f"{emoji_no} Ошибка!", value=f"Город не обнаружен!", inline=False)
			embed.add_field(name=f"Пример использования команды:", value=f"```/weather Moscow```")
			await ctx.send(embed=embed)

	@__weather.error
	async def weather_error(self, ctx, error):
		with open('/root/bot/databases/prefixes.json', 'r') as f:
			data = json.load(f)
			p = data[str(ctx.guild.id)]
		if isinstance(error, commands.MissingRequiredArgument) or isinstance(error, commands.TooManyArguments) or isinstance(error, commands.BadArgument) or isinstance(error, commands.MemberNotFound) or isinstance(error, commands.UserNotFound) or isinstance(error, commands.MessageNotFound) or isinstance(error, commands.ChannelNotReadable) or isinstance(error, commands.ChannelNotFound)  or isinstance(error, commands.EmojiNotFound) or isinstance(error, commands.PartialEmojiConversionFailure) or isinstance(error, commands.MissingPermissions) or isinstance(error, commands.BotMissingPermissions) or isinstance(error, commands.BadUnionArgument) or isinstance(error, commands.ArgumentParsingError):
			embed=discord.Embed(title=f'Команда **"{p}weather" `||` "{p}погода"**', description="**Увидеть погоду в выбранном городе**\n\n\n", color=discord.Color.blue(), timestamp=datetime.datetime.utcnow())
			embed.add_field(name="**Использование:**", value=f"`{p}weather <Город>`", inline=False)
			embed.add_field(name=f"**Примеры:**\n`{p}weather Москва`", value=":white_small_square: Увидеть погоду в Москве", inline=False)
			embed.set_footer(text=f'{self.bot.user.name}', icon_url=self.bot.user.avatar_url)
			await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))