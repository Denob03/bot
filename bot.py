import discord
from discord.ext import commands
TOKEN = 'MiPBQWwYYkNRGhpZtOwTJRC_uvt4C9AM'
client = commands.Bot(command_prefix = '.')
@client_event
async def on_ready():
    print ('Bot is ready. ')
client.run('MiPBQWwYYkNRGhpZtOwTJRC_uvt4C9AM')
