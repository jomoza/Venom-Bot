import discord

class BotMenu(object):
    """Class for generating a help menu for the Discord bot."""
    def __init__(self):
        """
        Initialize a BotMenu object with a predefined help menu.

        The help menu provides information about bot usage and commands.
        """
        self.helpmenu: discord.Embed = discord.Embed(
            title='Help menu',
            url='https://github.com/Bigyls/MSFVenomBOT',
            description='This is an advanced Discord MSFVenomBOT Help.\n',
            color=0x19bdda,
        )
        self.helpmenu.add_field(name='Usage:', value="All commands can start with '!'\n", inline=False)
        self.helpmenu.add_field(name='Create payload:', value="!create <platform> <LHOST> <LPORT>\n", inline=False)
        self.helpmenu.add_field(name='Platform options:', value="windows, sh, linux, macos, web\n", inline=False)
        self.helpmenu.set_thumbnail(url="https://imgur.com/RTBEU0L.png")

    def getMenu(self) -> discord.Embed:
        """
        Get the help menu as a Discord embed.

        :return: The help menu as a Discord embed.
        """
        return self.helpmenu
