from yahooApiForFinance import *

with open("nifty50-scripts.txt") as file_input:
    tickers = []
    for ticker in file_input:
        tickers.append(ticker)
    
    print(tickers[28])
    analyze_chart_for_multi_frames(tickers[28])