import requests
import csv
from requests.models import Response
import concurrent.futures



proxy = '211.187.102.102'

url = 'https://clutch.co/developers/artificial-intelligence'

headers = {
'authority': 'clutch.co',
'cache-control': 'max-age=0',
'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
'sec-ch-ua-mobile': '?0',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'navigate',
'sec-fetch-user': '?1',
'sec-fetch-dest': 'document',
'referer': 'https://clutch.co/developers/artificial-intelligence',
'accept-language': 'en-JP,en;q=0.9,ja-JP;q=0.8,ja;q=0.7,hi-IN;q=0.6,hi;q=0.5,en-US;q=0.4',
}

r = requests.get(url, headers=headers, proxies={'http' : proxy,'https': proxy})
print(r.status_code)
print(r)


exit()


 
''' 
def extract(proxy):
    #this was for when we took a list into the function, without conc futures.
    #proxy = random.choice(proxylist)
    headers = {
    'authority': 'clutch.co',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    'sec-ch-ua-mobile': '?0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'referer': 'https://clutch.co/developers/artificial-intelligence',
    'accept-language': 'en-JP,en;q=0.9,ja-JP;q=0.8,ja;q=0.7,hi-IN;q=0.6,hi;q=0.5,en-US;q=0.4',
    }
 '''
''' 
    r = requests.get(url, headers=headers, proxies={'http' : proxy,'https': proxy}, timeout=2)
    print(r.status_code)
    print(r)

 '''

'''     try:
        #change the url to https://httpbin.org/ip that doesnt block anything
        r = requests.get(url, headers=headers, proxies={'http' : proxy,'https': proxy}, timeout=2)

        print(r.json(), ' | Works')
    except:
        pass
    return proxy '''
''' 

with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(extract, proxy)

 '''


