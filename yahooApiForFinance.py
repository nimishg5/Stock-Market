import datetime as dt
import pandas as pd
import time as _time
import requests
import appConstants
from datetime import datetime
from datetime import date
from datetime import timedelta
from stockAnalyzers import crossovers_analyzer

def modify_timestamp(filtered_json):    
    for i, timestamp in enumerate(filtered_json[appConstants.TIMESTAMP]):
        filtered_json[appConstants.TIMESTAMP][i] = datetime.fromtimestamp(timestamp)

def analyze_chart_for_multi_frames(ticker, timeFrameDaysMap):

    for timeframe, backdays in timeFrameDaysMap.items():
        today = date.today()
        olddate = today - timedelta(days = backdays)

        today = today.strftime(appConstants.DATE_FORMAT)
        olddate = olddate.strftime(appConstants.DATE_FORMAT)
        start = int(_time.mktime(_time.strptime(olddate, appConstants.DATE_FORMAT)))
        end = int(_time.mktime(_time.strptime(today, appConstants.DATE_FORMAT)))
        interval = timeframe

        print('Fetching Share Prices for Dates ', olddate , " till ", today, " for Script : ", ticker)

        # defining a params dict for the parameters to be sent to the API
        params = {appConstants.PERIOD1_KEY: start, appConstants.PERIOD2_KEY: end, appConstants.INTERVAL_KEY: interval}
        url = appConstants.YAHOO_FINANCE_API.format(ticker)
        # print('url is ' + url + '\n with params as ' + str(params))
        response = requests.get(url=url, params=params, headers=appConstants.YAHOO_FINANCE_HEADERS)
        data = response.json()
        

        filtered_json = {}
        filtered_json[appConstants.TIMESTAMP] = data[appConstants.CHART][appConstants.RESULT][0][appConstants.TIMESTAMP]
        filtered_json[appConstants.CLOSE_KEY]     = data[appConstants.CHART][appConstants.RESULT][0][appConstants.INDICATORS][appConstants.QUOTE][0][appConstants.CLOSE_KEY]
        filtered_json[appConstants.VOLUME]    = data[appConstants.CHART][appConstants.RESULT][0][appConstants.INDICATORS][appConstants.QUOTE][0][appConstants.VOLUME]

        modify_timestamp(filtered_json)

        # Create DataFrame
        df = pd.DataFrame(filtered_json)
        df[appConstants.MA_200_KEY] =  df[appConstants.CLOSE_KEY].rolling(window=200).mean()
        df[appConstants.MA_50_KEY]  =  df[appConstants.CLOSE_KEY].rolling(window=50).mean()
        df.dropna(inplace=True)

        crossovers_analyzer(df, appConstants.CLOSE_KEY, appConstants.MA_200_KEY, interval, ticker)
        crossovers_analyzer(df, appConstants.MA_50_KEY, appConstants.MA_200_KEY, interval, ticker)