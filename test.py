from proxy_request import ProxyRequest


requests = ProxyRequest()
result = requests.get('https://www.clutch.co/')
print(result.status_code)