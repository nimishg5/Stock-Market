import datetime as dt
import pandas as pd
import time as _time
import requests
import smtplib
from datetime import datetime
from datetime import date
from datetime import timedelta

def modify_timestamp(filtered_json):    
    for i, timestamp in enumerate(filtered_json['timestamp']):
        filtered_json['timestamp'][i] = datetime.fromtimestamp(timestamp)

def trigger_mail(message):
    s = smtplib.SMTP('smtp.gmail.com', 587) 
    s.ehlo()
    s.starttls() 
    s.login("bestscripttracker@gmail.com", "007nimish") 
    s.sendmail("bestscripttracker@gmail.com", "131nimish@gmail.com", message) 
    s.quit()
    print('Email sent successfully')

def check_for_crossovers(df, key1, key2):
    print('*******************************************')
    print('start of check_for_crossovers for ' + key1 + ' and '+key2)
    crossover = 0
    closedPriceLowerThanDma = False
    counter = 0

    for index in df.index:
        if counter == 0:
            closedPriceLowerThanDma = df[key1][index] < df[key2][index]

        if df[key1][index] > df[key2][index] and closedPriceLowerThanDma:
            closedPriceLowerThanDma = not closedPriceLowerThanDma
            crossover = crossover + 1
            print('Cross Over occoured on ' + str(df['timestamp'][index]))
        elif df[key1][index] < df[key2][index] and (not closedPriceLowerThanDma):
            closedPriceLowerThanDma = not closedPriceLowerThanDma
            crossover = crossover + 1
            print('Cross Over occoured on ' + str(df['timestamp'][index]))
        # else:
            # print('going smooth')
        counter = counter + 1
 
    if bool(crossover):
        # trigger a mail once crossover happens
        #trigger_mail('Golden Cross Occoured')
        print('Cross Over Occoured for ' + key1 + '  &  ' + key2 + '  : '+ str(crossover))
    else:
        print('Nothing Happened for ' + key1 + '  &  ' + key2)
    
    print('*******************************************')
    print('end of check_for_crossovers for ' + key1 + ' and '+key2)

def analyze_chart_for_multi_frames(ticker):
    today = date.today()
    olddate = today - timedelta(days = 400)

    today = today.strftime('%d-%m-%Y')
    olddate = olddate.strftime('%d-%m-%Y')
    start = int(_time.mktime(_time.strptime(olddate, '%d-%m-%Y')))
    end = int(_time.mktime(_time.strptime(today, '%d-%m-%Y')))
    interval = '1d'

    print('Fetching Share Prices for Dates ', olddate , " till ", today, " for Script : ", ticker)

    # defining a params dict for the parameters to be sent to the API
    params = {'period1': start, 'period2': end, 'interval': interval}
    url = "https://query1.finance.yahoo.com/v8/finance/chart/{}".format(ticker)
    r = requests.get(url=url, params=params)
    data = r.json()
    print(url)

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

    check_for_crossovers(df, 'close', '200dma')
    check_for_crossovers(df, '50dma', '200dma')
    check_for_crossovers(df, 'close', '50dma')