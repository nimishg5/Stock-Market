import stockAnalyzerForNiftyFifty
import DividendStocksScrapper
import ExcelWriter
from emailSender import trigger_mail_2
from emailMessageResultModel import *
from datetime import date

print("Starting our Python Code")
file_name = "DividendStocksFiltered_"+ str(date.today()) +".xlsx"
df = DividendStocksScrapper.driver_func(10, 250)
ExcelWriter.write_into_excel(df, file_name)
stockAnalyzerForNiftyFifty.triggerFirstCalculation()

trigger_mail_2(getEmailMessage(), file_name)

print("---------- Python Code Successfully Ran ---------")