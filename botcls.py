import requests
from bs4 import BeautifulSoup
from time import sleep
from colorama import Fore
from datetime import datetime
from streamlit import caching
from os import system
import logging
from ctypes import windll


logging.getLogger("requests").setLevel(logging.WARNING)
clear = lambda : system('cls')

class main(object):

    def start(self):
        system('cls')
        print(Fore.RED+"""
    ██╗███╗   ██╗██╗   ██╗██╗████████╗███████╗    ███████╗ ██████╗██████╗  █████╗ ██████╗ ███████╗██████╗ 
    ██║████╗  ██║██║   ██║██║╚══██╔══╝██╔════╝    ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
    ██║██╔██╗ ██║██║   ██║██║   ██║   █████╗      ███████╗██║     ██████╔╝███████║██████╔╝█████╗  ██████╔╝
    ██║██║╚██╗██║╚██╗ ██╔╝██║   ██║   ██╔══╝      ╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗
    ██║██║ ╚████║ ╚████╔╝ ██║   ██║   ███████╗    ███████║╚██████╗██║  ██║██║  ██║██║     ███████╗██║  ██║ v1.2
    ╚═╝╚═╝  ╚═══╝  ╚═══╝  ╚═╝   ╚═╝   ╚══════╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝
                                                  By: Abo3abd#9966                                             
    """+Fore.RESET)

    def choosing(self):
        typee = 1
        Page_num = 1
        total = 1
        print(Fore.YELLOW+'[1]'+Fore.RED+' - '+Fore.LIGHTMAGENTA_EX+'Scrape The Main Page\n'+Fore.YELLOW+'[2]'+Fore.RED+' - '+Fore.LIGHTMAGENTA_EX+'Scrape Pages With Keywords\n'+Fore.RESET)
        ch1 = str(input(Fore.LIGHTCYAN_EX+'Choose What Scrape Way You Want : '+Fore.RESET))
        self.ch1 = ch1
        if ch1 < '1' or ch1 > '2' or len(ch1) > 1:
            print(Fore.LIGHTRED_EX+'Wrong !, Try Again')
            sleep(1)
            main().start()
            main().choosing()
        elif ch1 == '2':
            keyword = input(Fore.LIGHTCYAN_EX+'Type Keyword : '+Fore.YELLOW)
            keyword = keyword.replace(" ", "")
            print(keyword)
        main().start()
        print(Fore.YELLOW+'[1]'+Fore.RED+' - '+Fore.LIGHTMAGENTA_EX+'Bumped Recently\n'+Fore.YELLOW+'[2]'+Fore.RED+' - '+Fore.LIGHTMAGENTA_EX+'Member Count\n'+Fore.RESET)
        ch1_2 = input(Fore.LIGHTCYAN_EX+'Choose Scraping With Bumped Recently/Member Count : '+Fore.RESET)
        if ch1_2 < '1' or ch1_2 > '2' or len(ch1_2) > 1:
            print(Fore.LIGHTRED_EX+'Wrong !, Try Again')
            sleep(1)
            main().start()
            main().choosing()
            pass
            
        if ch1_2 == '1':
            typee = 'bumped_at'
        elif ch1_2 == '2':
            typee = 'member_count'
        
        if ch1 == '1':
            furl = f'https://disboard.org/servers/{Page_num}?sort={typee}'
            self.furl = furl
        elif ch1 == '2':
            furl = f'https://disboard.org/servers/tag/{keyword}/{Page_num}?sort={typee}'
            self.furl = furl
        
        input(Fore.GREEN+'\nPress Any Key To Start Scraping...'+Fore.RESET)
        main().start()
        main().scraper(furl, Page_num, total)

    
    def scraper(self, furl, Page_num, total):
        stotal = 1
        while True:
            if Page_num == stotal:
                r = requests.get(furl).text
                stotal += 1
            else:
                pass
            sleep(5)
            servers = BeautifulSoup(r, 'html.parser').findAll('div', class_="column is-one-third-desktop is-half-tablet")
            for server in servers:
                windll.kernel32.SetConsoleTitleW('invite Scraper v1.2 - Total Scraped : '+ str(total) + ' - ' +'You Are in Page Number : '+ str(Page_num) + ' - ' +'Add me On Discord : Abo3abd#9966')
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
                    caching.clear_memo_cache()
                sleep(0.1)
            Page_num += 1


main().start()
main().choosing()