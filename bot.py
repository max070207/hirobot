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

def get_prefix(bot, message):
	with open('/root/bot/databases/prefixes.json', 'r') as f:
		data = json.load(f)
	if str(message.guild.id) in data:
		prefix = data[str(message.guild.id)]
		return commands.when_mentioned_or(str(prefix))(bot, message)
	else:
		prefix = "h!"
		return commands.when_mentioned_or(str(prefix))(bot, message)

intents = discord.Intents(guilds=True, members=True, bans=False, emojis=True, integrations=True, webhooks=True, invites=False, voice_states=False, presences=False, messages=True, guild_messages=True, dm_messages=True, reactions=True, guild_reactions=True, dm_reactions=False, typing=False, guild_typing=False, dm_typing=False)
TOKEN = 'оп а токена то и нет :/'
bot = commands.Bot(command_prefix=get_prefix, intents=intents)
commands_cogs = ["apologize", "audit", "authors", "avatar", "ban", "bear", "bird", "bite", "bug", "buy-item", "bye", "camel", "cat", "categories", "channelinfo", "chicken", "clear", "compliment", "congratulate", "cow", "crab", "crocodile", "cry", "daily", "dog", "dolphin", "duck", "elephant", "embed", "eval", "feed", "fight", "fox", "frog", "gay", "giraffe", "help", "high_five", "holy", "horse", "hug", "imposter", "info", "invite", "inviteinfo", "IQ", "kangaroo", "kick", "kiss", "lick", "lion", "lol", "look", "moder", "monkey", "nuke", "owl", "panda", "panic", "parrot", "pat", "penguin", "pig", "pinch", "poke", "profile", "punch", "question", "rabbit", "rand", "reload", "roleinfo", "say", "scare", "sell-item", "server", "set-prefix", "shake_hand", "sheep", "shop", "sleep", "slowmode", "smell", "smoke", "spoiler", "star", "stat", "status", "support", "tea", "tickle", "tiger", "unban", "user", "vote", "wear-item", "weather", "welcome", "whale", "wolf", "work", "zebra"]
events_cogs = ["on_ready", "on_command_error", "on_message", "on_member_join", "on_member_remove", "on_message_delete", "on_guild_channel_create", "on_guild_channel_delete", "on_guild_role_create", "on_guild_role_delete", "on_guild_join", "on_guild_remove"]
commands_count = 0
events_count = 0
bot.remove_command("help")
bot.load_extension("jishaku")
for cog in commands_cogs:
	commands_count += 1
	bot.load_extension(f"commands.{cog}")
	print(f"```{cog}``` cog loaded [{commands_count}]/[102]")

for cog in events_cogs:
	events_count += 1
	bot.load_extension(f"events.{cog}")
	print(f"```{cog}``` cog loaded [{events_count}]/[12]")

bot.run(TOKEN)
