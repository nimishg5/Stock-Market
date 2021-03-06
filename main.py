from yahooApiForFinance import analyze_chart_for_multi_frames
from emailSender import *
from emailMessageResultModel import *

tickerList = [
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

# This below map will help us to calculate 200MA and 50MA
timeFrameDaysMap = {"15m": 20,
                    "30m": 40,
                    "1h": 100,
                    "1d": 400}

patterMessage = '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
lineBreak = '\n'
for i in range(len(tickerList)):
    setEmailMessage(lineBreak + patterMessage)
    analyze_chart_for_multi_frames(tickerList[i], timeFrameDaysMap)
    setEmailMessage(patterMessage + lineBreak)

# print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
# print(getEmailMessage())
trigger_mail(getEmailMessage())