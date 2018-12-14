# MSFVenom-Discord-Bot
Simple Discord bot to craft metasploit payloads.


The Bot works by executing msfvenom with the parameters that you give the bot. Then he will send you the payload file and leave a record in the log file

## Requeriments
[+] Metasploit https://www.metasploit.com/get-started

[+] Python3.6 https://www.python.org/downloads/release/python-367/

[+] discord.py https://discordpy.readthedocs.io/en/latest/api.html

## How to use
0.- if you are in linux and you do not have pytho3.6 nor the dependencies you can execute the file **setup.sh** to install automatically all the dependencies


1.- Put your Discord Bot Token in TOKEN variable on **bot.py**

https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token

2.- Run it

3.- Make "#help" or "#helpme" in Discord chat to know how to use the bot


```
[*] $create <platform> <ip_server_addres> <remote_port>
Platform options: windows, sh, linux, macox, web
```
