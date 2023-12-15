import discord
from discord.ext import commands
import json
import datetime

class Event(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_guild_join(self, guild):
		with open('/root/bot/databases/prefixes.json', 'r') as f:
				data = json.load(f)

		if str(guild.id) in data:
			prefix = data[str(guild.id)]
		else:
			async def update_data(data,guild,prefix):
				data[guild] = prefix

			await update_data(data,str(guild.id),str("h!"))

			with open('/root/prefixes.json', 'w') as f:
				json.dump(data,f,indent=4)
		channel = self.bot.get_channel(787215186288312330)
		embed=discord.Embed(title="Бот присоединился к серверу", colour=0x00ff00, timestamp=datetime.datetime.utcnow())
		embed.add_field(name="Имя:", value=f"`{guild.name}`", inline=True)
		embed.add_field(name="ID:", value=f"`{guild.id}`", inline=True)
		embed.add_field(name="Создатель:", value=f"`{guild.owner}`", inline=True)
		embed.add_field(name="Участников:", value=f"`{len(guild.members)}`", inline=True)
		embed.add_field(name="Пользователей:", value=f"`{len(list(filter(lambda m: not m.bot, guild.members)))}`", inline=True)
		embed.set_footer(text=f'{len(self.bot.guilds)} серверов')
		await channel.send(embed=embed)

def setup(bot):
	bot.add_cog(Event(bot))