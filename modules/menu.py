class botMenus(object):
    """docstring for botMenus."""
    def __init__(self):
        self.hlpmenu = "\nThis is advanced MSFVenom DISCORD BOT Help:\nAll commands can start wiz $ or #\n[*] $create <platform> <ip_server_addres> <remote_port>\nPlatform options: windows, sh, linux, macox, web"
    def getMenu(self):
        return self.hlpmenu
