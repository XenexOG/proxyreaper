from colorama import init
import sys
import os

import check
import scrape
from utils import *

os.system('cls')

init()

class proxyreaper():
    def __init__(self):
        self.main()

    def main(self):
        print(red + """
    dBBBBBb dBBBBBb    dBBBBP`Bb  .BP dBP dBP dBBBBBb    dBBBP dBBBBBb   dBBBBBb  dBBBP dBBBBBb
       dB'     dBP   dBP.BP     .BP     dBP      dBP               BB       dB'            dBP
  dBBBP'  dBBBBK   dBP.BP    dBBK     dBP   dBBBBK'  dBBP     dBP BB   dBBBP' dBBP    dBBBBK
 dBP     dBP  BB  dBP.BP    dB'      dBP   dBP  BB  dBP      dBP  BB  dBP    dBP     dBP  BB
dBP     dBP  dB' dBBBBP    dB' dBP  dBP   dBP  dB' dBBBBP   dBBBBBBB dBP    dBBBBP  dBP  dB' v1.1""")
        print(blue + 'by Xenex\n')
        m = get('Main Menu\n' +\
                red + '[' + blue + '1' + red + '] - ' + white + 'Scrape\n' +\
                red + '[' + blue + '2' + red + '] - ' + white + 'Check\n' +\
                red + '[' + blue + '3' + red + '] - ' + white + 'Exit\n')

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
            error('Input not recognised. Please retype and try again.')
            self.main()

if __name__ == '__main__':
    proxyreaper()
