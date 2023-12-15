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

	@commands.command(aliases=["server", "сервер"])
	@commands.guild_only()
	async def __server(self, ctx):
		status = check_category(str(ctx.guild.id), "Utilities")
		if status == 0:
			return
		emoji_bot = self.bot.get_emoji(828277310368645130)
		emoji_users = self.bot.get_emoji(828277466203553793)
		emoji_user = self.bot.get_emoji(828277492019757066)
		emoji_online = self.bot.get_emoji(746038919249920020)
		emoji_idle = self.bot.get_emoji(746038147573481512)
		emoji_dnd = self.bot.get_emoji(746038248446492782)
		emoji_offline = self.bot.get_emoji(746038507595628625)
		emoji_textchannel = self.bot.get_emoji(828277386516627457)
		emoji_voicechannel = self.bot.get_emoji(828277416031289364)
		emoji_channels = self.bot.get_emoji(828277544720531488)
		if ctx.guild.region == discord.VoiceRegion.amsterdam:
			region = ":flag_nl: Нидерланды"
		elif ctx.guild.region == discord.VoiceRegion.brazil:
			region = ":flag_br: Бразилия"
		elif ctx.guild.region == discord.VoiceRegion.dubai:
			region = ":flag_ae: ОАЭ"
		elif ctx.guild.region == discord.VoiceRegion.eu_central:
			region = ":flag_eu: Центральная Европа"
		elif ctx.guild.region == discord.VoiceRegion.eu_west:
			region = ":flag_eu: Западная Европа"
		elif ctx.guild.region == discord.VoiceRegion.europe:
			region = ":flag_eu: Европа"
		elif ctx.guild.region == discord.VoiceRegion.frankfurt:
			region = ":flag_de: Германия"
		elif ctx.guild.region == discord.VoiceRegion.hongkong:
			region = ":flag_hk: Гонконг"
		elif ctx.guild.region == discord.VoiceRegion.india:
			region = ":flag_in: Индия"
		elif ctx.guild.region == discord.VoiceRegion.japan:
			region = ":flag_jp: Япония"
		elif ctx.guild.region == discord.VoiceRegion.london:
			region = ":flag_gb: Великобритания"
		elif ctx.guild.region == discord.VoiceRegion.russia:
			region = ":flag_ru: Россия"
		elif ctx.guild.region == discord.VoiceRegion.singapore:
			region = ":flag_sg: Сингапур"
		elif ctx.guild.region == discord.VoiceRegion.southafrica:
			region = ":united_nations: Северная Африка"
		elif ctx.guild.region == discord.VoiceRegion.sydney:
			region = ":flag_au: Австралия"
		elif ctx.guild.region == discord.VoiceRegion.us_central:
			region = ":flag_us: Центральный США"
		elif ctx.guild.region == discord.VoiceRegion.us_east:
			region = ":flag_us: Востоный США"
		elif ctx.guild.region == discord.VoiceRegion.us_south:
			region = ":flag_us: Южный США"
		elif ctx.guild.region == discord.VoiceRegion.us_west:
			region = ":flag_us: Западный США"
		elif ctx.guild.region == discord.VoiceRegion.vip_amsterdam:
			region = ":high_brightness: :flag_nl: ВИП Амстердам"
		elif ctx.guild.region == discord.VoiceRegion.vip_us_east:
			region = ":high_brightness: :flag_us: ВИП восточный США"
		else:
			region = ":high_brightness: :flag_us: ВИП западный США"
		embed = discord.Embed(title=f"Информация о сервере {ctx.guild.name}:", colour=discord.Color.blue(), timestamp=datetime.datetime.utcnow())

		statuses = [len(list(filter(lambda m: str(m.status) == "online", ctx.guild.members))),
					len(list(filter(lambda m: str(m.status) == "idle", ctx.guild.members))),
					len(list(filter(lambda m: str(m.status) == "dnd", ctx.guild.members))),
					len(list(filter(lambda m: str(m.status) == "offline", ctx.guild.members)))]

		text_channels = len(ctx.guild.text_channels)
		voice_channels = len(ctx.guild.voice_channels)
		all_channels = text_channels + voice_channels
		embed.add_field(name="Участники:", value=f"{emoji_users} Всего: **{len(ctx.guild.members)}**\n{emoji_user} Людей: **{len(list(filter(lambda m: not m.bot, ctx.guild.members)))}**\n{emoji_bot} Ботов: **{len(list(filter(lambda m: m.bot, ctx.guild.members)))}**\n{emoji_online} Онлайн: **{statuses[0]}**\n{emoji_idle} Не активен: **{statuses[1]}**\n{emoji_dnd} Не беспокоить: **{statuses[2]}**\n{emoji_offline} Оффлайн: **{statuses[3]}**", inline = True)
		embed.add_field(name="Каналы:", value=f"{emoji_channels} Всего: **{all_channels}**\n{emoji_textchannel} Текстовых: **{text_channels}**\n{emoji_voicechannel} Голосовых: **{voice_channels}**", inline = True)
		embed.add_field(name="Сервер создан:", value=f'**{ctx.guild.created_at.strftime("%d/%m/%Y %H:%M:%S")} UTC**', inline = False)
		embed.add_field(name="Владелец:", value=f'**{ctx.guild.owner}**', inline = True)
		embed.add_field(name="Регион:", value=f'**{region}**', inline = True)
		embed.add_field(name="Ролей:", value=f"**{len(ctx.guild.roles)}**", inline = False)
		embed.add_field(name="ID:", value=f'**{ctx.guild.id}**', inline = True)
		embed.add_field(name="\u200b", value="\u200b", inline = True)
		embed.set_thumbnail(url=ctx.guild.icon_url)
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))