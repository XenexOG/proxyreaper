from colorama import init, Fore
import sys
import os
import requests
from bs4 import BeautifulSoup
import proxyreaper

class check():
    def __init__(self):
        self.checked = ''
        self.proxies_file = ''
        self._type = ''
        self.timeout = 0
        self.proxy_file()

    def proxy_file(self):
        os.system('cls')
        self.proxies_file = input(Fore.BLUE + 'Enter the name of the file with the proxies: ' + Fore.WHITE)
        if not self.proxies_file:
            os.system('cls')
            print(Fore.RED + 'Error: ' + Fore.WHITE + 'File specified does not exist. Please try again.')
            self.proxy_file()
        else:
            self.proxy_type()

    def proxy_type(self):
        os.system('cls')
        print(Fore.BLUE + 'Please specify the type of the proxies')
        print(Fore.RED + '[1] ' + Fore.WHITE + 'HTTP/S')
        print(Fore.RED + '[2] ' + Fore.WHITE + 'SOCKS4')
        print(Fore.RED + '[3] ' + Fore.WHITE + 'SOCKS5')

        m = input(Fore.WHITE + '>')
        if m == '1':
            self._type = 'http'
            self.proxy_timeout()
        elif m == '2':
            self._type = 'socks4'
            self.proxy_timeout()
        elif m == '3':
            self._type = 'socks5'
            self.proxy_timeout()
        else:
            os.system('cls')
            print(Fore.RED + 'ERROR: Input not recognised. Please retype and try again.')
            self.proxy_type()

    def proxy_timeout(self):
        os.system('cls')
        self.timeout = input(Fore.BLUE + 'Enter the timeout (default 5): ' + Fore.WHITE)
        if not self.timeout:
            self.timeout = 5
        
        self.proxy_check()

    def proxy_check(self):
        os.system('cls')
        print(Fore.BLUE + 'Started checking...')

        dead = 0
        with open(self.proxies_file, 'r') as f:
            for proxy in f:
                try:
                    r = requests.get('https://google.com/', proxies={type}, timeout=self.timeout)
                    r.raise_for_status()
                except Exception as e:
                    dead = dead + 1
                    pass
                else:
                    self.checked = self.checked + proxy + '\n'
            print(Fore.BLUE + 'Done.')

        alive = 0
        with open('checked-' + self.proxies_file, 'w') as f:
            for proxy in self.checked:
                f.write(proxy)
                alive = alive + 1
            print(Fore.BLUE + 'Done.')

        os.system('cls')

        print(Fore.WHITE + '{} proxies '.format(alive) + Fore.RED + 'dead.')
        print(Fore.WHITE + '{} proxies '.format(dead) + Fore.BLUE + 'alive.')

        proxyreaper.proxyreaper()
