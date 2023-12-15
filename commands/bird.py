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

	@commands.command(aliases=["bird", "птица"])
	@commands.guild_only()
	async def __bird(self, ctx):
		status = check_category(str(ctx.guild.id), "Images")
		if status == 0:
			return
		pictures = ["https://avatars.mds.yandex.net/get-pdb/2700313/8eb75c51-4f63-4b73-bcbd-0ea8fdda6117/s1200?webp=false",
					"https://cdn1.ozone.ru/multimedia/1037553914.jpg",
					"https://www.ejin.ru/wp-content/uploads/2017/09/5-1258.jpg",
					"https://get.wallhere.com/photo/bird-branch-blue-1035981.jpg",
					"https://million-wallpapers.ru/wallpapers/0/46/486572919469631/popugai.jpg",
					"https://avatars.mds.yandex.net/get-pdb/2397645/f37cab2f-2d40-40f5-afcf-465eafffbf31/s1200?webp=false",
					"https://img3.goodfon.ru/original/7000x4667/b/8d/vetki-pticy-popugai-zelen.jpg",
					"https://img3.goodfon.ru/original/2048x1437/a/61/ptica-perya-hvost-cvet-vetka.jpg",
					"https://million-wallpapers.ru/wallpapers/4/25/16471136626097254428/ptica-s-xoxolkom.jpg",
					"https://wallbox.ru/wallpapers/main2/201712/149024686158d35ccd275445.04722140.jpg",
					"https://i.pinimg.com/originals/7e/eb/89/7eeb89646ab525a916285c5222ae5dac.jpg",
					"https://naked-science.ru/wp-content/uploads/2018/01/field_image_paradi0.jpg",
					"https://funik.ru/wp-content/uploads/2019/03/de1ea1d2a463912fe27c.jpg",
					"https://kto-chto-gde.ru/wp-content/uploads/2017/09/mandarinka-2-copy.jpg",
					"https://www.1zoom.ru/big2/266/289703-alexfas01.jpg",
					"https://i.pinimg.com/736x/db/2e/91/db2e911f97fd993343ce768dc057375d.jpg",
					"https://www.tokkoro.com/picsup/3025926-bird_close-up_colorful_exotic_golden-pheasant_pheasant_wildlife.jpg",
					"https://avatars.mds.yandex.net/get-pdb/2821305/c9c27976-bb03-4fa9-8937-b6686834d96b/s1200?webp=false",
					"https://avatars.mds.yandex.net/get-pdb/931389/9171f9e2-453e-479a-87be-e9be01a9f1d1/s1200?webp=false",
					"https://kuda-spb.ru/uploads/d942726257ab199deb561cb8452ef883.jpg",
					"https://funik.ru/wp-content/uploads/2019/03/3091e94fa5373bade99b-768x799.jpg",
					"https://wallpaperscave.ru/images/original/18/01-11/animals-birds-8450.jpg",
					"https://wallbox.ru/wallpapers/main/201251/02ca9289bb38dd2.jpg",
					"https://avatars.mds.yandex.net/get-pdb/2338686/0a0674c2-f1df-44b2-89d3-2f473a8b9e6d/s1200?webp=false"]
		embed=discord.Embed(title="Птица! 🐦")
		embed.set_image(url=f"{random.choice(pictures)}")
		await ctx.send(embed=embed)

def setup(bot):
	bot.add_cog(Command(bot))