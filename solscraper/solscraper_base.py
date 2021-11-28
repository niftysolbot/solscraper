"""Main module."""
from scrapy.selector import Selector
from solscraper.proxy.proxies import getProxies

import requests


def entrypoint(args):
    # proxy = 'magiceden'
    # url = 'https://magiceden.io/marketplace/mutable_self_by_labyrinth'
    # url = 'https://solsea.io/collection/619e8819cca4b8caa13d3115'
    url = 'https://opensea.io/collection/3dpunks'
    # url = 'http://httpbin.org/'
    print("Solscraper started with args: " + str((args)))
    proxy_list = getProxies()
    print("Proxy URL list size: " + str(len(proxy_list)))
    for prox in ['proxx']:
        try:
            # r = requests.get('http://localhost:8050/render.html', params={'url': url, 'wait': 3, 'proxy': 'http://' + prox}, timeout=3)
            r = requests.get('http://localhost:8050/render.html',
                             params={'url': url, 'wait': 3, 'images': 0, 'engine': 'chromium', 'timeout': 15}, timeout=10)
            #print(r.text)
            if 'You need to enable JavaScript to run this app' not in r.text:
                print("Success!")
                print(r.text)
            else:
                print("Fail")

        except:
            pass
