from yahooApiForFinance import analyze_chart_for_multi_frames
from emailSender import *
from emailMessageResultModel import *
from mongoMethods import *

# This below map will help us to calculate 200MA and 50MA
timeFrameDaysMap = {"15m": 20,
                    "30m": 40,
                    "1h": 100,
                    "1d": 400}

patterMessage = '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'
lineBreak = '\n'

collection = createConnectionWithDB('stock-analyzer', 'Nifty50')
tickerList = fetchNifty50AllStocks(collection)
closeConnection()

for i in range(len(tickerList)):
    setEmailMessage(lineBreak + patterMessage)
    analyze_chart_for_multi_frames(tickerList[i], timeFrameDaysMap)
    setEmailMessage(patterMessage + lineBreak)

# print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
# print(getEmailMessage())
trigger_mail(getEmailMessage())