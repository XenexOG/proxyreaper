from colorama import init, Fore
import sys
import os
import requests
from bs4 import BeautifulSoup
import check
import scrape

os.system('cls')

test_url = 'google.com'

init()

class proxyreaper():
    def __init__(self):
        self.main()

    def main(self):
        print(Fore.RED + """
    dBBBBBb dBBBBBb    dBBBBP`Bb  .BP dBP dBP dBBBBBb    dBBBP dBBBBBb   dBBBBBb  dBBBP dBBBBBb
       dB'     dBP   dBP.BP     .BP     dBP      dBP               BB       dB'            dBP
  dBBBP'  dBBBBK   dBP.BP    dBBK     dBP   dBBBBK'  dBBP     dBP BB   dBBBP' dBBP    dBBBBK
 dBP     dBP  BB  dBP.BP    dB'      dBP   dBP  BB  dBP      dBP  BB  dBP    dBP     dBP  BB
dBP     dBP  dB' dBBBBP    dB' dBP  dBP   dBP  dB' dBBBBP   dBBBBBBB dBP    dBBBBP  dBP  dB'""")
        print(Fore.BLUE + 'by Xenex\n\n\n')
        print(Fore.RED + '[1] ' + Fore.WHITE + 'Scrape')
        print(Fore.RED + '[2] ' + Fore.WHITE + 'Check')
        print(Fore.RED + '[e] ' + Fore.WHITE + 'Exit')

        m = input('>')
        if m == '1':
            os.system('cls')
            scrape.scrape()
        elif m == '2':
            os.system('cls')
            check.check()
        elif m == 'e':
            os.system('cls')
            sys.exit(1)
        else:
            os.system('cls')
            print(Fore.RED + 'ERROR: Input not recognised. Please retype and try again.')
            self.main()

if __name__ == '__main__':
    proxyreaper()
