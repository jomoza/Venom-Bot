#!/usr/bin/python3

from discord.ext.commands import Bot
from modules import msfcraft
from modules import menu
from modules import check

import discord
import logging
import os

BOT_PREFIX = ('!')
TOKEN: str = ''  # ENTER YOUR TOKEN

intents = discord.Intents.default()
client: Bot = Bot(command_prefix=BOT_PREFIX, intents=intents)

logging.basicConfig(filename='logs/MSFVenomBOT.log',
                    filemode='a',
                    format='%(asctime)s:%(levelname)s:%(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S%p',
                    level=logging.DEBUG)

@client.command(name='create',
                description='msfvenom discord bot.',
                brief='[] Create a metasploit payload.',
                aliases=['createpayload', 'msfvenom', 'createmsf'],
                pass_context=True)
async def create(context, plat: str, ip: str, port: str) -> None:
    """
    Create a Metasploit payload based on user input.

    :param context: The context of the command invocation.
    :param plat: The target platform for the payload.
    :param ip: The IP address to be used in the payload.
    :param port: The port number to be used in the payload.
    """
    try:
        entry = check.EntryCheck(context, plat, ip, port)
        if await entry.checkAll():
            logging.info(f"{context.message.author.name} wants to create a {plat} payload for {ip}.")
            msfC = msfcraft.msfCrafting(plat, ip, port)
            logging.debug(f"Payload crafting for user {context.message.author.name}.")
            msfC.run()
            os.system(msfC.getPayloadCmd())
            logging.info(f"Payload for {context.message.author.name} with {plat} and {ip} was created.")
            await context.send(file=discord.File(msfC.getPayloadFile()))
            logging.info(f"{msfC.getPayloadFile()} was sent to {context.message.author.name}.")

    except Exception as e:
        logging.error(f" Error: {e} for user: {context.message.author.name}.")

@client.command(name='helpme',
                description='a better help message than this.',
                brief='[] Shows detailed help.',
                aliases=['hh', 'helpmeplease', 'wtfisthisshit'],
                pass_context=True)
async def helpme(context) -> None:
    """
    Display a detailed help menu.

    :param context: The context of the command invocation.
    """
    try:
        advHelp = menu.BotMenu()
        await context.send(embed=advHelp.getMenu())

    except Exception as e:
        logging.error(f" Error: {e} for user: {context.message.author.name}.")

@client.event
async def on_ready() -> None:
    """
    Event handler when the bot is ready.
    """
    await client.change_presence(activity=discord.Game(name='malware crafting'))
    logging.debug(f"Server {client.user.name} is running.")

try:
    client.run(TOKEN)

except Exception as e:
    logging.error(f"{e}.")
