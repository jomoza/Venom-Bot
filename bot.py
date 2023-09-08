#!/usr/bin/python3
from discord import Game, Intents, File
from discord.ext.commands import Bot
from modules import msfcraft
from modules import menu

import logging
import os
import re

# Constants
BOT_PREFIX = ('!')
TOKEN = ''  # ENTER YOUR TOKEN
DEBUG_LOG = 'logs/MSFVenomBOT_DEBUG.log'
ERROR_LOG = 'logs/MSFVenomBOT_ERROR.log'

intents = Intents.default().all()
client = Bot(command_prefix=BOT_PREFIX, intents=intents)

logging.basicConfig(filemode='a',
                    format='%(asctime)s:%(levelname)s:%(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S%p',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)

@client.command(name='create',
                description='msfvenom discord bot.',
                brief='[] Create a metasploit payload.',
                aliases=['createpayload', 'msfvenom', 'createmsf'],
                pass_context=True)
async def create(context, plat, ip, port):
    try:
        if re.match(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', ip) == None:
            logger.error(f"User: {context.message.author.mention} enter invalid IP.")
            await context.send("Invalid IP")
        if re.match(r'(windows|sh|linux|macos|web)', plat) == None:
            logger.error(f"User: {context.message.author.mention} enter invalid plateform.")
            await context.send("Invalid plateform")
        logger.info(f"{context.message.author.mention} wants to create a {plat} payload for {ip}.", DEBUG_LOG)
        msfC = msfcraft.msfCrafting(plat, ip, port)
        logger.debug(f"Payload crafting for user {context.message.author.mention}.", DEBUG_LOG)
        msfC.run()
        os.system(msfC.getPayloadCmd())
        logger.debug(f"Payload for {context.message.author.mention} with {plat} and {ip} was created.", DEBUG_LOG)
        await context.send(file=File(msfC.getPayloadFile()))
        logger.debug(f"{msfC.getPayloadFile()} was send to {context.message.author.mention}.", DEBUG_LOG)
    except Exception as e:
        logger.error(f" Error: {e} for user: {context.message.author.mention}.", ERROR_LOG)

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
        logger.error(f" Error: {e} for user: {context.message.author.mention}.", ERROR_LOG)

@client.event
async def on_ready():
    await client.change_presence(activity=Game(name='malware crafting'))
    logger.debug(f"Server {client.user.name} is running.", DEBUG_LOG)

try:
    client.run(TOKEN)
except Exception as e:
    logger.error(f"{e}.", ERROR_LOG)
