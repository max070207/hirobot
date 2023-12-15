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

	@commands.command(aliases=["rank", "ранг"])
	@commands.guild_only()
	async def __rank(self, ctx, member: discord.Member=None):
		if member == None:
			member = ctx.author
		with open('/root/bot/databases/lvl.json', 'r') as f:
			users = json.load(f)
		try:
			exp = users[str(member.id)]["exp"]
			lvl = users[str(member.id)]["lvl"]
			img = Image.open("/root/bot/supports/rank_card.png")
			draw = ImageDraw.Draw(img)
			av = member.avatar_url_as(size=1024)
			data = BytesIO(await av.read())
			pfp = Image.open(data)
			pfp = pfp.resize((100,100))
			font = ImageFont.truetype("/root/Fonts/courbd.ttf", 20)
			draw.text((120, 35),f"{member.name}",(0,0,0),font=font)
			draw.text((190, 70),f"{lvl}",(0,0,0),font=font)
			draw.text((310, 70),f"{exp}/{lvl ** 3 * 6 + 100}",(0,0,0),font=font)
			img.paste(pfp, (0,0))
			img.save('/root/bot/supports/rank_card_edit.png')
			await ctx.send(file=discord.File("/root/bot/supports/rank_card_edit.png"))
		except KeyError:
			emoji_no = self.bot.get_emoji(744165695662850170)
			embed=discord.Embed(colour=discord.Color.red())
			embed.add_field(name=f"{emoji_no} Ошибка!", value=f"**{member.name}** ещё не получал опыт!", inline=False)
			await ctx.send(embed=embed)

	@__rank.error
	async def rank_error(self, ctx, error):
		with open('/root/bot/databases/prefixes.json', 'r') as f:
			data = json.load(f)
			p = data[str(ctx.guild.id)]
		if isinstance(error, commands.MissingRequiredArgument) or isinstance(error, commands.TooManyArguments) or isinstance(error, commands.BadArgument) or isinstance(error, commands.MemberNotFound) or isinstance(error, commands.UserNotFound) or isinstance(error, commands.MessageNotFound) or isinstance(error, commands.ChannelNotReadable) or isinstance(error, commands.ChannelNotFound)  or isinstance(error, commands.EmojiNotFound) or isinstance(error, commands.PartialEmojiConversionFailure) or isinstance(error, commands.MissingPermissions) or isinstance(error, commands.BotMissingPermissions) or isinstance(error, commands.BadUnionArgument) or isinstance(error, commands.ArgumentParsingError):
			embed=discord.Embed(title=f'Команда **"{p}rank" `||` "{p}ранг"**', description="**Увидеть ранг выбранного юзера**\n\n\n", color=discord.Color.blue(), timestamp=datetime.datetime.utcnow())
			embed.add_field(name="**Использование:**", value=f"`{p}rank [@Юзер]`", inline=False)
			embed.add_field(name="**Примеры:**\n`{p}rank`", value=":white_small_square: Увидеть Ваш ранг", inline=False)
			embed.add_field(name=f"`{p}rank @{ctx.author}`", value=":white_small_square: Увидеть ранг выбранного юзера", inline=False)
			embed.add_field(name=f"`{p}rank {ctx.author.id}`", value=":white_small_square: Увидеть ранг выбранного юзера по его id", inline=False)
			embed.set_footer(text=f'{self.bot.user.name}', icon_url=self.bot.user.avatar_url)
			await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))