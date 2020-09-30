from discord.ext import commands

from dotenv import load_dotenv
import os


class AmongUs(commands.Cog):
    def __init__(self, bot):
        load_dotenv()

        self.bot = bot
        self.deads = []
        self.TOKEN = os.getenv('IM_TOKEN')
        self.VOICE_CHANNEL_ID = int(os.getenv('IM_VC'))
        self.ADMIN_CHANNEL_ID = int(os.getenv('IM_ADMIN'))
        self.BOT_ID = 760578307195535381
    
    # mute all undead members
    @commands.command()
    @commands.has_role('Game Manager')
    async def play(self, ctx):
        await self.handle_voice(ctx, True)
        await ctx.send('Muted everyone.')

    # unmute all undead members
    @commands.command()
    @commands.has_role('Game Manager')
    async def meet(self, ctx):
        await self.handle_voice(ctx, False)
        await ctx.send('Unmuted undeads.')

    # unmute all and clear self.deads list
    @commands.command()
    @commands.has_role('Game Manager')
    async def clear(self, ctx):
        self.deads.clear()
        await self.handle_voice(ctx, False)
        await ctx.send('Game restarted.')

    # print self.deads list
    @commands.command()
    @commands.has_role('Game Manager')
    async def dead(self, ctx):
        await ctx.send('Currently dead: ' + ', '.join([m.display_name for m in self.deads]))

    # add player to self.deads list
    @commands.command()
    @commands.has_role('Game Manager')
    async def kill(self, ctx, player):
        try:
            member = await ctx.guild.fetch_member(int(player[3:-1]))
        except:
            await ctx.send(f'Invalid user')
        else:
            if member.id == self.BOT_ID:
                await ctx.send("You can't kill me ;)")
            elif member not in self.get_voice_members():
                await ctx.send("Member is not playing.")
            elif member in self.deads:
                await ctx.send(f'{member.mention} is already dead.')
            else:
                self.deads.append(member)
                print([m.nick for m in self.deads])
                await member.edit(mute=True, reason='Muted in Among Us game.')
                await ctx.send(f'{member.mention} has been killed.')
                    

    def get_voice_members(self):
        return self.bot.get_channel(self.VOICE_CHANNEL_ID).members
        

    async def handle_voice(self, ctx, to_mute: bool):
        members = self.get_voice_members()
        if to_mute:
            for m in members:
                await m.edit(mute=True, reason='Muted in Among Us game.')
        else:
            for m in members:
                if m not in self.deads:
                    await m.edit(mute=False, reason='Unmuted in Among Us game.')