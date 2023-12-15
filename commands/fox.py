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

	@commands.command(aliases=["fox", "лис"])
	@commands.guild_only()
	async def __fox(self, ctx):
		status = check_category(str(ctx.guild.id), "Images")
		if status == 0:
			return
		pictures = ['https://img4.goodfon.ru/original/4500x3000/4/a1/lis-lisa-ryzhaia-solntse-trava-boke.jpg',
					'https://web-zoopark.ru/wp-content/uploads/2018/07/2-143.jpg',
					'https://masyamba.ru/%D1%84%D0%BE%D1%82%D0%BE-%D0%BB%D0%B8%D1%81/68-%D0%BB%D0%B8%D1%81%D0%B0-%D1%84%D0%BE%D1%82%D0%BE.jpg',
					'https://bigpicture.ru/wp-content/uploads/2011/12/1022.jpg',
					'https://tverigrad.ru/wp-content/uploads/2017/06/%D0%BB%D0%B8%D1%81%D0%B0-16-%D0%BC%D0%B0%D1%8F.jpg',
					'https://avatars.mds.yandex.net/get-pdb/963318/ce3f5f4e-85e1-43da-88f7-90b9bde070b5/s1200?webp=false',
					'https://fotovmire.ru/wp-content/uploads/2019/03/10287/vnimatelnyj-vzgljad-ryzhej-plutovki.jpg',
					'https://avatars.mds.yandex.net/get-pdb/69339/9ce7a520-06d1-433d-a9b0-5b6e7829fc97/s1200?webp=false',
					'https://avatars.mds.yandex.net/get-pdb/777813/38632f3b-fcc7-4a48-818b-ba90b075a7d7/s1200?webp=false',
					'https://imya-sonnik.ru/wp-content/uploads/2019/10/s1200-2020-06-03t100102.252.jpg',
					'https://img1.goodfon.ru/wallpaper/nbig/0/6c/lisa-zver-vzglyad-lis.jpg']
		embed=discord.Embed(title="Лис! 🦊")
		embed.set_image(url=f"{random.choice(pictures)}")
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))