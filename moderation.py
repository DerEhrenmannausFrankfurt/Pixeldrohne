import discord
from discord.ext import commands


class Mods:
    def __init__(self, bot):
        self.bot = bot
        self.color = 0xf0aade

    @commands.command(name="kick", no_pm=True)
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member, *arg):
        if arg == ():
            reason = "Der Nutzer wurde vom Server geworfen."
        else:
            reason = " ".join(arg)
        embed = discord.Embed(
            title="Kick",
            description=f"Der Nutzer {user.name} wurde mit dem Grund `{reason}` gekicked.",
            color=self.color
        )
        await discord.Guild.kick(ctx.guild, user=user, reason=reason)
        await ctx.channel.send(embed=embed)

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('Es schaut fast so aus als sei der Nutzer nicht mehr auf dem Server.')
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send('Nutzer konnte nicht gekicked werden.')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('Sorry, du kannst diesen Befehl leider nicht nutzen.')

    @commands.command(name="ban", no_pm=True)
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member, *arg):
        if arg == ():
            reason = "Der Nutzer wurde vom Server geworfen."
        else:
            reason = " ".join(arg)
        embed = discord.Embed(
            title="Kick",
            description=f"Der Nutzer {user.name} wurde mit dem Grund `{reason}` gebannt.",
            color=self.color
        )
        await discord.Guild.kick(ctx.guild, user=user, reason=reason)
        await ctx.channel.send(embed=embed)

    @ban.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('Es schaut fast so aus als sei der Nutzer nicht mehr auf dem Server.')
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send('Nutzer konnte nicht gebannt werden.')
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('Sorry, du kannst diesen Befehl leider nicht nutzen.')

    @commands.command(name="purge", no_pm=True)
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, messages):
        messages = int(messages) + 1
        deleted = await ctx.channel.purge(limit=messages, bulk=True)
        await ctx.channel.send(f"Es wurden erfolgreich {len(deleted)-1} Nachrichten gelöscht.", delete_after=5)
