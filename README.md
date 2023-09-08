# MSFVenom-Discord-Bot
Simple Discord bot to craft metasploit payloads.

![alt text](https://i.ibb.co/NxD7mDs/we.gif "Venom Discord Bot")

The Bot works by executing msfvenom with the parameters that you give the bot. Then he will send you the payload file.

## Requirements

[+] msfvenom https://www.metasploit.com/get-started

[+] discord.py https://discordpy.readthedocs.io/en/latest/api.html

[+] Python requirements: `pip3 install -r requirements.txt`

## How to use

1.- Put your Discord Bot Token in TOKEN variable on **bot.py**

https://github.com/reactiflux/discord-irc/wiki/Creating-a-discord-bot-&-getting-a-token

2.- Run **bot.py** with `python3 bot.py`

3.- Make "!help" or "!helpme" in Discord chat to know how to use the bot

```
!create <platform> <LHOST> <LPORT>
Platform options: windows, sh, linux, macox, web
```
