import json
import requests


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
    'Accept' : '*/*',
    'Accept-Encoding': 'gzip, deflate, br'
    }
resp = requests.get('https://query1.finance.yahoo.com/v8/finance/chart/ADANIPORTS.NS?period1=1706639400&period2=1708367400&interval=15m', headers=headers)
resp_dict = resp.json()
pretty = json.dumps(resp_dict, indent=10)
print(pretty)