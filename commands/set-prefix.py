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

	@commands.command(aliases=["set-prefix", "новый-префикс"])
	@commands.guild_only()
	@commands.has_permissions(administrator=True)
	@commands.cooldown(3, 86400, commands.BucketType.guild)
	async def __set_prefix(self, ctx, *, prefix=None):
		if prefix == None:
			prefix = "h!"
		if len(str(prefix)) > 3:
			emoji_no = self.bot.get_emoji(785095586671230986)
			embed=discord.Embed(title=f"{emoji_no} Ошибка!", description="Префикс не может быть больше 3-х символов!", color=discord.Color.red())
			await ctx.send(embed=embed)
			return
		with open('/root/bot/databases/prefixes.json', 'r') as f:
			data = json.load(f)
		async def update_data(data,guild,prefix):
			data[guild] = prefix
		await update_data(data,str(ctx.guild.id),str(prefix))
		with open('/root/bot/databases/prefixes.json', 'w') as f:
			json.dump(data,f,indent=4)
		await ctx.send(f"Префикс бота изменён на `{prefix}`. Используйте `{prefix}set-prefix <prefix>` чтобы снова изменить его!")

	@__set_prefix.error
	async def set_prefix_error(self, ctx, error):
		with open('/root/bot/databases/prefixes.json', 'r') as f:
			data = json.load(f)
			p = data[str(ctx.guild.id)]
		if isinstance(error, commands.MissingRequiredArgument) or isinstance(error, commands.TooManyArguments) or isinstance(error, commands.BadArgument) or isinstance(error, commands.MemberNotFound) or isinstance(error, commands.UserNotFound) or isinstance(error, commands.MessageNotFound) or isinstance(error, commands.ChannelNotReadable) or isinstance(error, commands.ChannelNotFound)  or isinstance(error, commands.EmojiNotFound) or isinstance(error, commands.PartialEmojiConversionFailure) or isinstance(error, commands.MissingPermissions) or isinstance(error, commands.BotMissingPermissions) or isinstance(error, commands.BadUnionArgument) or isinstance(error, commands.ArgumentParsingError):
			embed=discord.Embed(title=f'Команда **"{p}set-prefix" `||` "{p}новый-префикс"**', description="**Бот повторит написанный вами текст с вашей конфигурацией**\n\n\n", color=discord.Color.blue(), timestamp=datetime.datetime.utcnow())
			embed.add_field(name="**Необходимые права:**", value="```ADMINISTRATOR```", inline=False)
			embed.add_field(name="**Использование:**", value=f"`{p}set-prefix <Префикс>`", inline=False)
			embed.add_field(name=f"**Примеры:**\n`{p}set-prefix /`", value=":white_small_square: Изменить префикс на /", inline=False)
			embed.set_footer(text=f'{self.bot.user.name}', icon_url=self.bot.user.avatar_url)
			await ctx.send(embed=embed)
		if isinstance(error, commands.CommandOnCooldown):
			emoji_no = self.bot.get_emoji(785095586671230986)
			time_to_retry = round(error.retry_after)
			embed=discord.Embed(title=f"{emoji_no} Ошибка!", description=f"Действует задержка!\nПопробуйте позже через `{time_to_retry}` секунд", color=discord.Color.red())
			await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))