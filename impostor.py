from discord.ext import commands
import discord
from cogs import among_us

from dotenv import load_dotenv
import os


load_dotenv()
TOKEN = os.getenv('IM_TOKEN')
VOICE_CHANNEL_ID = int(os.getenv('IM_VC'))
ADMIN_CHANNEL_ID = int(os.getenv('IM_ADMIN'))
BOT_ID = 760578307195535381

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix='!', intents=intents)


@bot.listen()
async def on_ready():
    bot.add_cog(among_us.AmongUs(bot))
    admin_channel = bot.get_channel(ADMIN_CHANNEL_ID)
    print('Connected to discord.')
    await admin_channel.send('Connected :)')


bot.run(TOKEN)
