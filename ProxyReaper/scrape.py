import sys
import os
import requests
from bs4 import BeautifulSoup
import configparser

import proxyreaper
from utils import *

class scrape:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.cfg')

        self.proxies_type = ''
        self.file_dir = config.get('scraper', 'file_dir')
        self.threads = int(config.get('scraper', 'threads'))

        self.proxies_type = ''

        self.proxy_type()

    def proxy_type(self):
        m = get('Please specify the type of the proxies\n' +\
                red + '[' + blue + '1' + red + '] - ' + white + 'HTTP/S\n' +\
                red + '[' + blue + '2' + red + '] - ' + white + 'SOCKS4\n' +\
                red + '[' + blue + '3' + red + '] - ' + white + 'SOCKS5\n')
        
        if m == '1':
            self.proxies_type = 'http'
            self.scrape_proxies()
        elif m == '2':
            self.proxies_type = 'socks4'
            self.scrape_proxies()
        elif m == '3':
            self.proxies_type = 'socks5'
            self.scrape_proxies()
        else:
            os.system('cls')
            error('Input not recognised. Please retype and try again.')
            self.proxy_type()

    def scrape_proxies(self):
        os.system('cls')

        action('Started scraping.')

        # proxy-list.download
        try:
            action('Scraping proxy-list.downlod')
            r = requests.get('https://www.proxy-list.download/api/v1/get?type=' + self.proxies_type)
            proxies = r.text
            if self.proxies_type == 'http':
                r2 = requests.get('https://www.proxy-list.download/api/v1/get?type=https')
                proxies = proxies + r2.text
            action('Done.')
        except Exception as e:
            error('{}'.format(e))
            get('Press any key to continue...')

        # proxyscrape.com
        try:
            action('Scraping proxyscrape.com')
            r = requests.get('https://api.proxyscrape.com?request=displayproxies&proxytype=' + self.proxies_type)
            proxies = proxies + r.text
            action('Done.')
        except Exception as e:
            error('{}'.format(e))
            get('Press any key to continue...')

        # proxy.rudnkh.me
        if type == 'http':
            try:
                action('Scraping proxy.rudnkh.me')
                r = requests.get('https://proxy.rudnkh.me/txt')
                proxies = proxies + r.text
                action('Done.')
            except Exception as e:
                error('{}'.format(e))
                get('Press any key to continue...')

        # free-proxy-list.net
        if type == 'http':
            try:
                action('Scraping free-proxy-list.net')
                r = requests.get('https://www.free-proxy-list.net/')
                soup = BeautifulSoup(r.text, 'html.parser')
                proxy_table_fpl = soup.select('table#proxylisttable tr')
                for p in proxy_table_fpl:
                    info = p.find_all('td')
                    if len(info):
                        proxy_fpl = ':'.join([info[0].text, info[1].text])
                proxies = proxies + proxy_fpl
                action('Done.')
            except Exception as e:
                error('{}'.format(e))
                get('Press any key to continue...')

        # TODO: Add more proxy providers

        action('Removing duplicates.')

        final_proxies = '\n'.join(set(proxies.split()))
        lines = 0

        with open('results_{}.txt'.format(self.proxies_type), 'w') as f:
            f.write(final_proxies)
            f.close()

        with open('results_{}.txt'.format(self.proxies_type), 'r') as f:
            for line in f:
                lines = lines + 1
            f.close()

        os.system('cls')
        action('Scraped ' + blue + '{} '.format(lines) + white + 'proxies.')
        proxyreaper.proxyreaper()
