import discord
from discord.ext import commands
from discord import User
import random

client = discord.Client()

description = '''An example bot to showcase the discord.ext.commands extension
module.

There are a number of utility commands being showcased here.'''
bot = commands.Bot(command_prefix='c!', description=description)

bot.remove_command('help')

creator = "vCrexmyNutJuice#1234"
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command(pass_context=True)
async def help2(ctx):
    help = discord.Embed(title="", description="Help:", colour=discord.Colour.green())
    help.set_author(name="Bot Creator - " + (creator), url="https://discord.gg/fuCsACq")
    help.add_field(name="Command .", value="Describtion here", inline=False)
    await bot.whisper(embed=help)
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def info(ctx):
    info = discord.Embed(title="Bot Creator - " + (creator), description="Bot in development ideas welcome list of bots info:", color=0xeee657)
    
    # give info about you here
    info.add_field(name="Author", value="Bot Creator - " + (creator))

    # give users a link to invite thsi bot to their server
    info.add_field(name="Invite", value="https://discordapp.com/oauth2/authorize?client_id=483411855818227723&permissions=8&redirect_uri=https%3A%2F%2Fdiscordapp.com%2Foauth2%2Fauthorize%3Fresponse_type%3Dcode%26client_id%3D483411855818227723&scope=bot", inline=False)
    await bot.say(embed=info)
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def owner(ctx):
    if ctx.message.author.id == "385005936525443072":
        await bot.say("Love You Daddy")
    else:
        await bot.say("Your Not My Daddy")

@bot.command(pass_context=True)
async def say(ctx, *, something):
    await bot.say("**{} said:** {}".format(str(ctx.message.author), something))
    await bot.delete_message(ctx.message)
	
@bot.command(pass_context=True)
async def points(ctx):
    points = discord.Embed(title="Points", description="Bot in development ideas welcome list of bots current point data:", colour=discord.Colour.green())

    points.add_field(name="Display Name", value="""vCrexmyNutJuice
Preast James
Elfprincess93
OliverOzpin(Rwby)
ApeNormal
Yeah sure Whatever
DEATHPOUL!!!!!!
EvilHeelGlorious
BamaShockz
Deltadeer
DHARRIS
icecold
MacGunne
Night Cat
OLL13 DA T1T4N
RebelWithoutAPause
sb CaTus
shizzy01
Snoopdizzle33
Sweetgurl384
Uralom
VocaloidIsntAnime
𝓓𝓪𝓼 𝓜𝓸𝓻𝓫𝓪𝓬𝓱-𝓜𝓸𝓷𝓼𝓽𝓮𝓻
	""")

    # give users a link to invite thsi bot to their server
    points.add_field(name="Points", value="""1000000pts
0pts
0pts
0pts
0pts
0pts
0pts
0pts
0pts
0pts
0pts
0pts
0pts
0pts
0pts
0pts
0pts
0pts
0pts
0pts
0pts
0pts
0pts""", inline=True)


    await bot.say(embed=points)
    await bot.delete_message(ctx.message)
	
@bot.command(pass_context=True)
async def names(ctx):
    names = discord.Embed(title="Names", description="Bot in development ideas welcome list of bots current point data:", colour=discord.Colour.red())

    names.add_field(name="Display Name", value="""vCrexmyNutJuice
Preast James
Elfprincess93
OliverOzpin(Rwby)
ApeNormal
Yeah sure Whatever
DEATHPOUL!!!!!!
EvilHeelGlorious
BamaShockz
Deltadeer
DHARRIS
icecold
MacGunne
Night Cat
OLL13 DA T1T4N
RebelWithoutAPause
sb CaTus
shizzy01
Snoopdizzle33
Sweetgurl384
Uralom
VocaloidIsntAnime
𝓓𝓪𝓼 𝓜𝓸𝓻𝓫𝓪𝓬𝓱-𝓜𝓸𝓷𝓼𝓽𝓮𝓻
	""")

    # give users a link to invite thsi bot to their server
    names.add_field(name="Actual Name", value="""WIP
""", inline=True)


    await bot.say(embed=names)
    await bot.delete_message(ctx.message)


bot.run('NDgzNDExODU1ODE4MjI3NzIz.DmTHFg.56xSDsZvUGgcELOscffpLuc7CUs')
