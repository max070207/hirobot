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

events_list = ["member_join", "member_remove", "channel_create", "channel_delete", "role_create", "role_delete", "message_delete"]

class Command(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command(aliases=["audit", "аудит"])
	@commands.guild_only()
	@commands.has_permissions(administrator=True)
	async def __audit(self, ctx, status:str=None, event:str=None, channel_id:int=None):
		emoji_note = self.bot.get_emoji(785095507122978836)
		emoji_yes = self.bot.get_emoji(785095546146652180)
		emoji_no = self.bot.get_emoji(785095586671230986)
		with open('/root/bot/databases/audit_servers.json', 'r') as f:
			data = json.load(f)
		if status == None:
			if not str(ctx.guild.id) in data:
				data[str(ctx.guild.id)] = {}
			embed=discord.Embed(color=0x00FFFF, description=f"{emoji_yes} - Включено\n{emoji_no} - Выключено\n")
			for event in events_list:
				if not event in data[str(ctx.guild.id)]:
					embed.description += f"\n**{event} ─︎** {emoji_no}"
				elif data[str(ctx.guild.id)][event]["status"] == "on":
					embed.description += f"\n**{event} ─︎** {emoji_yes}"
				elif data[str(ctx.guild.id)][event]["status"] == "off":
					embed.description += f"\n**{event} ─︎** {emoji_no}"
			await ctx.send(embed=embed)
			return
		if status != "on":
			if status != "off":
				await ctx.send(f"Статус может быть только `on` или `off`!")
				return
		if not event in events_list:
			await ctx.send(f"Ивент `{event}` не обнаружен!")
			return
		if status == "on":
			if channel_id == None:
				await ctx.send(f"Вы забыли указать id канала для отправки сообщений!")
				return
			if not self.bot.get_channel(channel_id) in ctx.guild.text_channels:
				await ctx.send(f"Такого канала не существует!")
				return
		async def update_data(data, guild):
			if not guild in data:
				data[guild] = {}
		async def change_status(ctx, data, guild, event, status, channel_id):
			if not event in data[guild]:
				data[guild][event] = {}
				data[guild][event]["status"] = status
				data[guild][event]["channel_id"] = channel_id
				embed=discord.Embed(title=f"{emoji_yes} Успешно!", color=0x00FFFF, description=f"Ивенту **`{event}`** присвоен статус **`{status}`**")
				await ctx.send(embed=embed)
			else:
				if status == "off":
					if data[guild][event]["status"] == "off":
						embed=discord.Embed(title=f"{emoji_note} Примечание", color=0x00FFFF, description=f"Ивент **`{event}`** уже отключён")
						await ctx.send(embed=embed)
					elif data[guild][event]["status"] == "on":
						embed=discord.Embed(title=f"{emoji_yes} Успешно!", color=0x00FFFF, description=f"Ивенту **`{event}`** присвоен статус **`{status}`**")
						await ctx.send(embed=embed)
				elif status == "on":
					if data[guild][event]["status"] == "on":
						embed=discord.Embed(title=f"{emoji_note} Примечание", color=0x00FFFF, description=f"Ивент **`{event}`** уже включён")
						await ctx.send(embed=embed)
					elif data[guild][event]["status"] == "off":
						embed=discord.Embed(title=f"{emoji_yes} Успешно!", color=0x00FFFF, description=f"Ивенту **`{event}`** присвоен статус **`{status}`**")
						await ctx.send(embed=embed)
				data[guild][event]["status"] = status
				if status == "on":
					data[guild][event]["channel_id"] = channel_id
		await update_data(data, str(ctx.guild.id))
		await change_status(ctx, data, str(ctx.guild.id), event, status, channel_id)
		with open('/root/bot/databases/audit_servers.json', 'w') as f:
				json.dump(data,f,indent=4)

	@__audit.error
	async def audit_error(self, ctx, error):
		with open('/root/bot/databases/prefixes.json', 'r') as f:
			data = json.load(f)
			p = data[str(ctx.guild.id)]
		if isinstance(error, commands.MissingRequiredArgument) or isinstance(error, commands.TooManyArguments) or isinstance(error, commands.BadArgument) or isinstance(error, commands.MemberNotFound) or isinstance(error, commands.UserNotFound) or isinstance(error, commands.MessageNotFound) or isinstance(error, commands.ChannelNotReadable) or isinstance(error, commands.ChannelNotFound)  or isinstance(error, commands.EmojiNotFound) or isinstance(error, commands.PartialEmojiConversionFailure) or isinstance(error, commands.MissingPermissions) or isinstance(error, commands.BotMissingPermissions) or isinstance(error, commands.BadUnionArgument) or isinstance(error, commands.ArgumentParsingError):
			embed=discord.Embed(title=f'Команда **"{p}audit" `||` "{p}аудит"**', description="**Включить аудит для вашего сервера**\n\n\n", color=discord.Color.blue(), timestamp=datetime.datetime.utcnow())
			embed.add_field(name="**Необходимые права:**", value="```ADMINISTRATOR```", inline=False)
			embed.add_field(name="**Использование:**", value=f"`{p}audit [on | off] [Имя ивента] [Канал айди]`", inline=False)
			embed.add_field(name="**Доступные имена ивентов:**", value=f"`member_join`\n`member_remove`\n`channel_create`\n`channel_delete`\n`role_create`\n`role_delete`\n`message_delete`", inline=False)
			embed.add_field(name=f"**Примеры:**\n`{p}audit`", value=":white_small_square: Увидеть список включённых и отключённых ивентов", inline=False)
			embed.add_field(name=f"`{p}audit on message_delete 742412216309121077`", value=":white_small_square: Включить ивент удаление сообщения", inline=False)
			embed.set_footer(text=self.bot.user.name, icon_url=self.bot.user.avatar_url)
			await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))