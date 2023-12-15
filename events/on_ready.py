import discord
from discord.ext import commands
from discord.ext import tasks
import asyncio
import json
import datetime

class Event(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		print('Logged successfully!')
		@tasks.loop(seconds=1800)
		async def change_status():
			servs = len(self.bot.guilds)
			channelCount = len(set(self.bot.get_all_channels()))
			memberCount = 0
			for guild in self.bot.guilds:
				memberCount += len(guild.members)
			await self.bot.change_presence(status = discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=f'h!help || {servs} SERVERS'))
			await asyncio.sleep(600)
			await self.bot.change_presence(status = discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=f'h!help || {memberCount} MEMBERS'))
			await asyncio.sleep(600)
			await self.bot.change_presence(status = discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=f'h!help || {channelCount} CHANNELS'))
			await asyncio.sleep(600)
		change_status.start()
		@tasks.loop(seconds=86400)
		async def take_salary():
			with open('/root/bot/databases/fight.json', 'r') as f:
				data = json.load(f)
			channel = self.bot.get_channel(870742823203373086)
			embed=discord.Embed(title=":mag: Идёт проверка раздачи зарплат")
			await channel.send(embed=embed)
			for member in data:
				if "work" in data[member]:
					if data[member]["work"]["type"] == "work":
						if data[member]["work"]["time_to_next_salary"] == str(datetime.date.today()):
							money = data[member]["work"]["salary"]
							data[member]["money"] += money
							date = str(datetime.date.today() + datetime.timedelta(days=7))
							data[member]["work"]["time_to_next_salary"] = date
							embed=discord.Embed(title=f":mag_right: Выдал зарплату пользователю {member}")
							await channel.send(embed=embed)
			with open('/root/bot/databases/fight.json', 'w') as f:
				json.dump(data,f,indent=4)
		take_salary.start()

def setup(bot):
	bot.add_cog(Event(bot))