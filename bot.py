# bot.py
import os
import random
import json
import urllib
import requests
from discord.ext import commands
import discord
from dotenv import load_dotenv


load_dotenv()
TOKEN = "T0KEN"

bot = commands.Bot(command_prefix='!!')

ip = "mc.Backrooms.me"

url = 'https://api.mcsrvstat.us/2/' + ip

AllowedRoles = ('bot dev','Moderator')

bot.remove_command('help')


@bot.event
async def on_ready():
    print("Bot started")
    activity = discord.Game(name=" on mc.Backrooms.me")
    await bot.change_presence(status=discord.Status.online, activity=activity)


@bot.event
async def on_member_join(member):
    ment = member.mention
    channel = bot.get_channel(738869896338997338)
    await channel.send("Welcome to The Backrooms investagation server "+ ment +" Please don't leave or we will steal your room,\n use !!info to get info about the discord server and !!help to get more bot commands")


@bot.command(help='Admin only Help command')
@commands.has_any_role(*AllowedRoles)
async def ahelp(ctx):
    await ctx.send("""```

  e          sends args back to you                    (Admin only)
  ahelp      Shows this message                        (Admin only)
  setstatus  Set bot playing message                   (Admin only)
  setip      Change the ip used by the bot             (Admin only)
  resetip    Reset the ip used by the bot              (Admin only)
  listadmin  Lists roles allowed to use admin commands (Admin only)
  help       Help manu with admin only commands hidden
  info       Shows bot info
  online     Shows who is on the server
  plug       Get info about The Plug
  serverinfo Get online players from another server

```""")


@bot.command(help='Help command')
async def help(ctx):
    await ctx.send("""```

  ahelp         Help for admins (shows admin only commands)
  help          Shows this message
  info          Shows bot info
  online        Shows who is on the server
  plug          Get info about The Plug
  serverinfo    Get online players from another server

```""")


@bot.command(help='Shows bot info')
async def info(ctx):
    await ctx.send("This is The Backrooms Investigation server where we try to solve the mystery of the location of the mysterious backrooms photo. While many of these liminal space photos like the backrooms could be real, there is some questioning of weather these photos are actually real. Some of them  turn out to be 3D renders. Could the backrooms be a 3D render? We do not know. If not, then there is still something to find out; where the location actually is. use !!info to get info about the discord server and !!help to get more bot commands")

@bot.command(help='Get info about The Plug')
async def plug(ctx):
    await ctx.send("the plug from the backrooms image is a type C US plug")

@bot.command(help='Lists roles allowed to use admin commands (Admin only)')
@commands.has_any_role(*AllowedRoles)
async def listadmin(ctx):
    await ctx.send(AllowedRoles)

@bot.command(help='Set bot playing message (Admin only)')
@commands.has_any_role(*AllowedRoles)
async def setstatus(ctx, *, status:str):
    activity = discord.Game(name=status)
    await bot.change_presence(status=discord.Status.online, activity=activity)


@bot.command(help='Get online players from another server')
async def serverinfo(ctx, ServerIP):
    url = 'https://api.mcsrvstat.us/2/' + ServerIP
    resp = requests.get(url=url)
    data = resp.json()
    if str(data['online']) == "True":
        if 'list' in data['players']:
            response = "Online Players for " + ServerIP + " : " + str(data['players']['list'])
        else:
            response = "Nobody is online on " + ServerIP
    else:
        response = ServerIP + " Is offline"

    await ctx.send(response)


@bot.command(help='Change the ip used by the bot (Admin only)')
@commands.has_any_role(*AllowedRoles)
async def setip(ctx, NewIP):
    global url
    global ip
    ip = NewIP
    url = 'https://api.mcsrvstat.us/2/' + ip
    response = "set ip to " + ip
    await ctx.send(response)


@bot.command(help='Reset the ip used by the bot (Admin only)')
@commands.has_any_role(*AllowedRoles)
async def resetip(ctx):
    global url
    global ip
    ip = "mc.Backrooms.me"
    url = 'https://api.mcsrvstat.us/2/mc.Backrooms.me'
    response = "reset ip to mc.Backrooms.me"
    await ctx.send(response)



@bot.command(help='Shows who is on the server')
async def online(ctx):
    resp = requests.get(url=url)
    data = resp.json()
    if str(data['online']) == "True":
        if 'list' in data['players']:
            response = "Online Players for " + ip + " : " + str(data['players']['list'])
        else:
            response = "Nobody is online on " + ip
    else:
        response = ip + " Is offline"

    await ctx.send(response)


@bot.command(help='sends args back to you (Admin only)')
@commands.has_any_role(*AllowedRoles)
async def e(ctx, *, content:str):
    await ctx.send(content)
    await ctx.message.delete()


@bot.command()
async def debug(ctx, debug_mode):
    resp = requests.get(url=url)
    data = resp.json()

    if debug_mode == "1":
        response = data['players']

    elif debug_mode == "2":
        response = data

    await ctx.send(response)



bot.run(TOKEN)
