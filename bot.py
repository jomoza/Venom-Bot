from discord import Game, Intents, File
from discord.ext.commands import Bot
from modules import msfcraft
from modules import logger
from modules import menu

import os

BOT_PREFIX = ('!')
TOKEN = ''  # ENTER YOUR TOKEN

intents = Intents.default().all()
client = Bot(command_prefix=BOT_PREFIX, intents=intents)

@client.command(name='create',
                description='msfvenom discord bot.',
                brief='[] Create a metasploit payload.',
                aliases=['createpayload', 'msfvenom', 'createmsf'],
                pass_context=True)
async def create(context, plat, ip, port):
    try:
        response = f"{context.message.author.mention} wants to create a {plat} payload for {ip}"
        msfC = msfcraft.msfCrafting(plat, ip, port)
        wlog = logger.logInfo()
        await context.send(response)
        wlog.writeLog(response)
        msfC.run()
        os.system(msfC.getPayloadCmd())
        await context.send(response)
        await context.send(file=File(msfC.getPayloadFile()))
    except Exception as e:
        print(e)

@client.command(name='helpme',
                description='a better help message than this.',
                brief='[] Shows detailed help.',
                aliases=['hh', 'helpmeplease', 'wtfisthisshit'],
                pass_context=True)
async def helpme(context):
    try:
        advHelp = menu.botMenus()
        await context.send(advHelp.getMenu())
    except Exception as e:
        print(e)

@client.event
async def on_ready():
    await client.change_presence(activity=Game(name='malware crafting'))
    print(client.user.name)

client.run(TOKEN)