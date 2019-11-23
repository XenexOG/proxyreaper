import sys
import os
import requests
import time
import configparser
import threading

import proxyreaper
from utils import *

class check():
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.cfg')

        self.proxies_type = ''
        self.proxies_file = ''
        self.test_url = config.get('checker', 'test_url')
        self.file_dir = config.get('checker', 'file_dir')
        self.threads = int(config.get('checker', 'threads'))
        self.timeout = int(config.get('checker', 'timeout'))

        self.dead = 0
        self.alive = 0
        self.to_check = []

        self.proxy_file()

    def proxy_file(self):
        os.system('cls')
        print(self.proxies_file)
        self.proxies_file = get('Enter the name of the file with the proxies: ')
        if not self.proxies_file:
            os.system('cls')
            error('Specified file does not exist. Please try again.')
            self.proxy_file()
        else:
            self.proxy_type()

    def proxy_type(self):
        os.system('cls')
        m = get('Please specify the type of the proxies\n' +\
                red + '[' + blue + '1' + red + '] - ' + white + 'HTTP/S\n' +\
                red + '[' + blue + '2' + red + '] - ' + white + 'SOCKS4\n' +\
                red + '[' + blue + '3' + red + '] - ' + white + 'SOCKS5\n')

        if m == '1':
            self.proxies_type = 'http'
            self.proxy_check()
        elif m == '2':
            self.proxies_type = 'socks4'
            self.proxy_check()
        elif m == '3':
            self.proxies_type = 'socks5'
            self.proxy_check()
        else:
            os.system('cls')
            error('ERROR: Input not recognised. Please retype and try again.')
            self.proxy_type()

    def proxy_check(self):
        os.system('cls')

        checking = True

        with open(self.proxies_file, 'r') as f:
            self.proxy_count = sum(1 for proxy in open(self.proxies_file))
            action('Loaded {} proxies.'.format(self.proxy_count))
            
            for proxy in f:
                self.to_check.append(proxy.strip())

        action('Starting threads.')

        threads = []
        for i in range(self.threads):
            threads.append(threading.Thread(target=self.check_proxies))
            action('Starting thread {}'.format(i + 1))
            threads[i].start()
            time.sleep(0.25)

        action('{} threads started.'.format(self.threads))

        while checking:
            if len(threading.enumerate()) - 1 == 0:
                checking = False
            else:
                os.system('cls')

                action('{} proxies '.format(self.alive) + red + 'dead.')
                action('{} proxies '.format(self.dead) + blue + 'alive.')

                proxyreaper.proxyreaper()
    
    def check_proxies(self):
        while len(self.to_check) > 0:
            proxy = self.to_check[0]
            self.to_check.pop(0)

            alert('Checking {} | {} left | {} alive | {} dead'.format(proxy, len(self.to_check), self.alive, self.dead))
            try:
                requests.get(self.test_url, proxies={'http': self.proxies_type + '://' + proxy + '/'}, timeout=int(self.timeout))
            except:
                error('{} not working.'.format(proxy))
                self.dead = self.dead + 1
            else:
                action('Found working proxy ({})'.format(proxy))
                save_to_file(self.file_dir, proxy)
                self.alive = self.alive + 1