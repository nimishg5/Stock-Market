from yahooApiForFinance import analyze_chart_for_multi_frames
from emailSender import *
from resultModel import getEmailMessage

tickers = [
    "ADANIPORTS.NS",
    "AMBUJACEM.NS",
    "ASIANPAINT.NS",
    "AUROPHARMA.NS",
    "AXISBANK.NS",
    "BAJAJ-AUTO.NS",
    "BAJFINANCE.NS",
    "BPCL.NS",
    "BHARTIARTL.NS",
    "INFRATEL.NS",
    "BOSCHLTD.NS",
    "CIPLA.NS",
    "COALINDIA.NS",
    "DRREDDY.NS",
    "EICHERMOT.NS",
    "GAIL.NS",
    "HCLTECH.NS",
    "HDFCBANK.NS",
    "HEROMOTOCO.NS",
    "HINDALCO.NS",
    "HINDPETRO.NS",
    "HINDUNILVR.NS",
    "HDFC.NS",
    "ITC.NS",
    "ICICIBANK.NS",
    "IBULHSGFIN.NS",
    "IOC.NS",
    "INDUSINDBK.NS",
    "INFY.NS",
    "KOTAKBANK.NS",
    "LT.NS",
    "LUPIN.NS",
    "M&M.NS",
    "MARUTI.NS",
    "NTPC.NS",
    "ONGC.NS",
    "POWERGRID.NS",
    "RELIANCE.NS",
    "SBIN.NS",
    "SUNPHARMA.NS",
    "TCS.NS",
    "TATAMOTORS.NS",
    "TATASTEEL.NS",
    "TECHM.NS",
    "UPL.NS",
    "ULTRACEMCO.NS",
    "VEDL.NS",
    "WIPRO.NS",
    "YESBANK.NS",
    "ZEEL.NS"]

for i in range(len(tickers)):
    analyze_chart_for_multi_frames(tickers[i], '15m')

# print('final analysis : \n' + getEmailMessage())
trigger_mail(getEmailMessage())