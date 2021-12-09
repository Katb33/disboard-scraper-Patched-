# i dont care if u skid this tool, BUT DONT PUT TOKEN GRABBER IN IT MF!!!
import requests
from bs4 import BeautifulSoup
from time import sleep
from colorama import Fore, Back
from datetime import datetime
import sys
import os




os.system('cls')
print(Fore.RED+"""
██╗███╗   ██╗██╗   ██╗██╗████████╗███████╗    ███████╗ ██████╗██████╗  █████╗ ██████╗ ███████╗██████╗ 
██║████╗  ██║██║   ██║██║╚══██╔══╝██╔════╝    ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
██║██╔██╗ ██║██║   ██║██║   ██║   █████╗      ███████╗██║     ██████╔╝███████║██████╔╝█████╗  ██████╔╝
██║██║╚██╗██║╚██╗ ██╔╝██║   ██║   ██╔══╝      ╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗
██║██║ ╚████║ ╚████╔╝ ██║   ██║   ███████╗    ███████║╚██████╗██║  ██║██║  ██║██║     ███████╗██║  ██║
╚═╝╚═╝  ╚═══╝  ╚═══╝  ╚═╝   ╚═╝   ╚══════╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝
                                              By: Abo3abd#9966                                             
"""+Fore.RESET)

def delay_print(s):
    for Sexycat in s:
        sys.stdout.write(Sexycat)
        sys.stdout.flush()
        sleep(0.05)

delay_print("If u want to add keywords open the file and edit the link, i can add this feature but im lazy, Have Fun :)\n")
print(Back.WHITE+Fore.BLACK+"------------------------------------------ Scraping Now ! ------------------------------------------\n"+Back.RESET+Fore.RESET)

Page_num = 1
total = 1
def scraper():
    global Page_num
    global total
    r = requests.get(f'https://disboard.org/servers/tag/gaming/{Page_num}?sort=-member_count').text
    sleep(5)
    servers = BeautifulSoup(r, 'html.parser').findAll('div', class_="column is-one-third-desktop is-half-tablet")
    for server in servers:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        eyedee = server.find('a', class_="button button-join is-discord").get('data-id')
        url = f"https://disboard.org/site/get-invite/{eyedee}"
        x = requests.get(url)
        tempinvite = x.text
        invite = tempinvite.replace('"', '')
        print(Fore.YELLOW+current_time+Fore.RED+' | '+Fore.GREEN+'New Invite Scraped : '+Fore.WHITE+invite+Fore.RED+' | '+Fore.LIGHTCYAN_EX+'Page Number : '+str(Page_num)+Fore.RED+' | '+Fore.LIGHTBLUE_EX+'Total Scraped : '+str(total)+Fore.RESET)
        total += 1
        with open('invites.txt', 'a') as f:
            f.write(invite+'\n')
            f.close()
        sleep(0.1)
    Page_num += 1

while True:
    scraper()
