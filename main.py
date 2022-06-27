'''

~ Powerful Vanity Stealer In Python
~ By Aryan.#1337

'''


import os
import asyncio
import random
import aiohttp
import json
import sys
import time
from colorama import Fore

def clear():
  os.system("cls")

clear()

os.system("title Vanity Sniper - Aryan.#1337")

token = input(f"{Fore.CYAN}[>]{Fore.RESET} Token: ")
clear()
vanity = input(f"{Fore.CYAN}[>]{Fore.RESET} Vanity Code: ")
clear()
guild = int(input(f"{Fore.CYAN}[>]{Fore.RESET} Where Vanity Should Be Added: "))
clear()
user_type = input(f"{Fore.CYAN}[>]{Fore.RESET} Bot True/False: ")
api = random.choice([6, 8, 9])
snipeno = random.randint(1, 30)

clear()

time.sleep(1)

if user_type in ["True", "true", True]:
  headers = {"Authorization": "Bot {}".format(token)}

elif user_type in ["False", "false", False]:
  headers = {"Authorization": token}



async def vanity_sniper():
  json = {
                'code': f"aryan-sniper-{snipeno}",
                'reason': "Aryan.#1337 | Vanity Sniper"
  }
  async with aiohttp.ClientSession(headers=headers) as session:
    async with session.patch(f"https://discord.com/api/v{api}/guilds/{guild}/vanity-url", json=json, headers=headers) as sniped:
      if sniped.status in (200, 201, 204):
        print(f"{Fore.GREEN}[+]{Fore.RESET} Aryan.#1337 | Vanity Sniped")
        sys.exit()



async def vanity_checker():
  async with aiohttp.ClientSession(headers=headers) as session:
    while True:
      async with session.get(f"https://discord.com/api/v{api}/invites/{vanity}", headers=headers) as checker:
        if checker.status == 404:
          await vanity_sniper()
        else:
          print(f"{Fore.RED}[>]{Fore.RESET} Aryan.#1337 | Vanity Not Available")



loop = asyncio.get_event_loop()
loop.run_until_complete(vanity_checker())
loop.close()