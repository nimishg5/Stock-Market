import appConstants
from yahooApiForFinance import analyze_chart_for_multi_frames
from emailSender import *
from emailMessageResultModel import *


# This below map will help us to calculate 200MA and 50MA
timeFrameDaysMap = {appConstants.FIFTEEN_MINS: 20,
                    appConstants.THIRTY_MINS: 40,
                    appConstants.ONE_HOUR: 100,
                    appConstants.ONE_DAY: 400}

for i in range(len(appConstants.TICKER_LIST)):
    setEmailMessage(appConstants.LINE_BREAK + appConstants.MESSAGE_PATTERN)
    analyze_chart_for_multi_frames(appConstants.TICKER_LIST[i], timeFrameDaysMap)
    setEmailMessage(appConstants.MESSAGE_PATTERN + appConstants.LINE_BREAK)


trigger_mail(getEmailMessage())