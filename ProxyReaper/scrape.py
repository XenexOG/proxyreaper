from colorama import init, Fore
import sys
import os
import requests
from bs4 import BeautifulSoup
import proxyreaper

def scrape():
    type = ''

    print(Fore.RED + 'Select what type of proxy do you want to scrape\n\n\n')
    print(Fore.RED + '[1] ' + Fore.WHITE + 'HTTP/S')
    print(Fore.RED + '[2] ' + Fore.WHITE + 'SOCKS4')
    print(Fore.RED + '[3] ' + Fore.WHITE + 'SOCKS5')
    print(Fore.RED + '[b] ' + Fore.WHITE + 'Back')

    m = input('>')
    if m == '1':
        type = 'http'
    elif m == '2':
        type = 'socks4'
    elif m == '3':
        type = 'socks5'
    elif m == 'b':
        os.system('cls')
        proxyreaper.proxyreaper()
    else:
        os.system('cls')
        print(Fore.RED + 'ERROR: Input not recognised. Please retype and try again.')
        scrape()

    os.system('cls')
    print(Fore.RED + 'Started Scraping...')

    # proxy-list.download
    try:
        print(Fore.BLUE + '\nScraping: ' + Fore.WHITE + 'proxy-list.downlod...')
        r = requests.get('https://www.proxy-list.download/api/v1/get?type=' + type)
        proxies = r.text
        if type == 'http':
            r2 = requests.get('https://www.proxy-list.download/api/v1/get?type=https')
            proxies = proxies + r2.text
        print(Fore.BLUE + 'Done.')
    except Exception as e:
        print(Fore.RED + 'ERROR: ' + Fore.WHITE + '{}'.format(e))
        input(Fore.BLUE + 'Press any key to continue...')

    # proxyscrape.com
    try:
        print(Fore.BLUE + '\nScraping: ' + Fore.WHITE + 'proxyscrape.com...')
        r = requests.get('https://api.proxyscrape.com?request=displayproxies&proxytype=' + type)
        proxies = proxies + r.text
        print(Fore.BLUE + 'Done.')
    except Exception as e:
        print(Fore.RED + 'ERROR: ' + Fore.WHITE + '{}'.format(e))
        input(Fore.BLUE + 'Press any key to continue...')

    # proxy.rudnkh.me
    if type == 'http':
        try:
            print(Fore.BLUE + '\nScraping: ' + Fore.WHITE + 'proxy.rudnkh.me...')
            r = requests.get('https://proxy.rudnkh.me/txt')
            proxies = proxies + r.text
            print(Fore.BLUE + 'Done.')
        except Exception as e:
            print(Fore.RED + 'ERROR: ' + Fore.WHITE + '{}'.format(e))
            input(Fore.BLUE + 'Press any key to continue...')

    # free-proxy-list.net
    if type == 'http':
        try:
            print(Fore.BLUE + '\nScraping: ' + Fore.WHITE + 'free-proxy-list.net...')
            r = requests.get('https://www.free-proxy-list.net/')
            soup = BeautifulSoup(r.text, 'html.parser')
            proxy_table_fpl = soup.select('table#proxylisttable tr')
            for p in proxy_table_fpl:
                info = p.find_all('td')
                if len(info):
                    proxy_fpl = ':'.join([info[0].text, info[1].text])
            proxies = proxies + proxy_fpl
        except Exception as e:
            print(Fore.RED + 'ERROR: ' + Fore.WHITE + '{}'.format(e))
            input(Fore.BLUE + 'Press any key to continue...')

    # TODO: Add more proxy providers

    print(Fore.RED + '\nRemoving duplicates...')

    final_proxies = '\n'.join(set(proxies.split()))
    lines = 0

    with open('results_{}.txt'.format(type), 'w') as f:
        f.write(final_proxies)
        f.close()

    with open('results_{}.txt'.format(type), 'r') as f:
        for line in f:
            lines = lines + 1
        f.close()

    # TODO: Do some tidying

    os.system('cls')
    print(Fore.WHITE + 'Scraped ' + Fore.RED + '{} '.format(lines) + Fore.WHITE + 'proxies')
    proxyreaper.proxyreaper()
