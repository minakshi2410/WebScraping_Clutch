from os import read
import csv
from newproxy import PROXY_POOL_ENABLED
import requests
import requests


url = 'https://clutch.co/developers/artificial-intelligence'

headers = {
    'authority': 'clutch.co',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    'sec-ch-ua-mobile': '?0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://clutch.co/developers/artificial-intelligence',
    'accept-language': 'en-JP,en;q=0.9,ja-JP;q=0.8,ja;q=0.7,hi-IN;q=0.6,hi;q=0.5,en-US;q=0.4',
}


proxy = {'91.121.93.172:80'}
print(len(proxy))

response = requests.get(url, headers=headers)
print(response.status_code)


