import discord
import logging
import re

class EntryCheck(object):
    def __init__(self, context, plat: str, ip: str, port: str):
        """
        Initialize an EntryCheck object with context, platform (plat), IP address (ip), and port.

        :param context: Discord context for the user's interaction.
        :param plat: The platform provided by the user.
        :param ip: The IP address provided by the user.
        :param port: The port number provided by the user.
        """
        self.context = context
        self.plat = plat
        self.ip = ip
        self.port = port

    async def checkAll(self) -> int:
        """
        Check all the user-provided parameters (platform, IP, and port).

        :return: 0 if any of the checks fail, 1 if all checks pass.
        """
        plat_check = await self.checkPlateform()
        ip_check = await self.checkIP()
        port_check = await self.checkport()

        if plat_check == 0 or ip_check == 0 or port_check == 0:
            return 0
        else:
            return 1

    async def checkPlateform(self) -> int:
        """
        Check if the provided platform is valid.

        :return: 0 if the check fails, 1 if the check passes.
        """
        if re.match(r'(windows|sh|linux|macos|web)', self.plat) == None:
            logging.error(f"User: {self.context.message.author.name} entered an invalid platform.")
            embed = discord.Embed(
                title='Error',
                url='https://github.com/Bigyls/MSFVenomBOT',
                description='Invalid platform name\n',
                color=0xFF5733
            )
            embed.add_field(name='Chosen among them:', value='- windows\n- sh\n- linux\n- macos\n- web')
            embed.set_thumbnail(url="https://imgur.com/RTBEU0L.png")
            await self.context.send(embed=embed)
            return 0
        else:
            return 1

    async def checkIP(self) -> int:
        """
        Check if the provided IP address is valid.

        :return: 0 if the check fails, 1 if the check passes.
        """
        if re.match(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', self.ip) == None:
            logging.error(f"User: {self.context.message.author.name} entered an invalid IP.")
            embed = discord.Embed(
                title='Error',
                url='https://github.com/Bigyls/MSFVenomBOT',
                description='Invalid IP\n',
                color=0xFF5733
            )
            embed.set_thumbnail(url="https://imgur.com/RTBEU0L.png")
            await self.context.send(embed=embed)
            return 0
        else:
            return 1

    async def checkport(self) -> int:
        """
        Check if the provided port number is valid.

        :return: 0 if the check fails, 1 if the check passes.
        """
        if re.match(r'^(?!0)([1-9]\d{0,4}|[1-5]\d{4}|6[0-4]\d{3}|65[0-4]\d{2}|655[0-2]\d|6553[0-5])$', self.port) == None:
            logging.error(f"User: {self.context.message.author.name} entered an invalid port.")
            embed = discord.Embed(
                title='Error',
                url='https://github.com/Bigyls/MSFVenomBOT',
                description='Invalid port\n',
                color=0xFF5733
            )
            embed.set_thumbnail(url="https://imgur.com/RTBEU0L.png")
            await self.context.send(embed=embed)
            return 0
        else:
            return 1
