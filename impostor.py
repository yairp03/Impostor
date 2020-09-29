from discord.ext import commands
import discord
import os
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('IMPOSTOR_TOKEN')
intents = discord.Intents.default()
intents.members = True
VOICE_CHANNEL_ID = 757998039985291268
ADMIN_CHANNEL_ID = 760582768324509708
BOT_ID = 760578307195535381

bot = commands.Bot(command_prefix='!', intents=intents)

deads = []
@bot.listen()
async def on_ready():
    admin_channel = bot.get_channel(ADMIN_CHANNEL_ID)
    print('Connected to discord.')
    await admin_channel.send('Connected :)')

# mute all undead members
@bot.command()
@commands.has_role('Game Manager')
async def play(ctx):
    await handle_voice(ctx, True)
    await ctx.send('Muted everyone.')

# unmute all undead members
@bot.command()
@commands.has_role('Game Manager')
async def meet(ctx):
    await handle_voice(ctx, False)
    await ctx.send('Unmuted undeads.')

# unmute all and clear deads list
@bot.command()
@commands.has_role('Game Manager')
async def clear(ctx):
    deads.clear()
    await handle_voice(ctx, False)
    await ctx.send('Game restarted.')

# print deads list
@bot.command()
@commands.has_role('Game Manager')
async def dead(ctx):
    await ctx.send('Currently dead: ' + ', '.join([m.display_name for m in deads]))

# add player to deads list
@bot.command()
@commands.has_role('Game Manager')
async def kill(ctx, player):
    try:
        member = await ctx.guild.fetch_member(int(player[3:-1]))
    except:
        await ctx.send(f'Invalid user')
    else:
        if member.id == BOT_ID:
            await ctx.send("You can't kill me ;)")
        elif member not in get_voice_members():
            await ctx.send("Member is not playing.")
        elif member in deads:
            await ctx.send(f'{member.mention} is already dead.')
        else:
            deads.append(member)
            print(deads)
            await ctx.send(f'{member.mention} has been killed.')
                

def get_voice_members():
    return bot.get_channel(VOICE_CHANNEL_ID).members
    

async def handle_voice(ctx, to_mute: bool):
    members = get_voice_members()
    if to_mute:
        for m in members:
            await m.edit(mute=True, reason='Muted in Among Us game.')
    else:
        for m in members:
            if m not in deads:
                await m.edit(mute=False, reason='Unmuted in Among Us game.')


bot.run(TOKEN)
