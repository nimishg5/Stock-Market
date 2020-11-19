import datetime as dt
import pandas as pd
import time as _time
import requests
import smtplib
from datetime import datetime
from datetime import date
from datetime import timedelta
from stockAnalyzers import crossovers_analyzer

def modify_timestamp(filtered_json):    
    for i, timestamp in enumerate(filtered_json['timestamp']):
        filtered_json['timestamp'][i] = datetime.fromtimestamp(timestamp)

def analyze_chart_for_multi_frames(ticker, timeframe):
    today = date.today()
    olddate = today - timedelta(days = 40)

    today = today.strftime('%d-%m-%Y')
    olddate = olddate.strftime('%d-%m-%Y')
    start = int(_time.mktime(_time.strptime(olddate, '%d-%m-%Y')))
    end = int(_time.mktime(_time.strptime(today, '%d-%m-%Y')))
    interval = timeframe

    print('Fetching Share Prices for Dates ', olddate , " till ", today, " for Script : ", ticker)

    # defining a params dict for the parameters to be sent to the API
    params = {'period1': start, 'period2': end, 'interval': interval}
    url = "https://query1.finance.yahoo.com/v8/finance/chart/{}".format(ticker)
    r = requests.get(url=url, params=params)
    data = r.json()
    # print(data)

    filtered_json = {}
    filtered_json['timestamp'] = data['chart']['result'][0]['timestamp']
    filtered_json['close']     = data['chart']['result'][0]['indicators']['quote'][0]['close']
    filtered_json['volume']    = data['chart']['result'][0]['indicators']['quote'][0]['volume']

    modify_timestamp(filtered_json)

    # Create DataFrame
    df = pd.DataFrame(filtered_json)
    df['200dma'] =  df['close'].rolling(window=200).mean()
    df['50dma']  =  df['close'].rolling(window=50).mean()
    df.dropna(inplace=True)
    # print(df)

    # crossovers_analyzer(df, 'close', '200dma')
    # crossovers_analyzer(df, '50dma', '200dma')
    crossovers_analyzer(df, 'close', '50dma', ticker)