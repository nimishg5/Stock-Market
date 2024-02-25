import stockAnalyzerForNiftyFifty
import DividendStocksScrapper
import ExcelWriter
from emailSender import *
from emailMessageResultModel import *

print("Starting our Python Code")
df = DividendStocksScrapper.driver_func(10, 250)
ExcelWriter.write_into_excel(df, "DividendStocksFiltered_nimish.xlsx")
stockAnalyzerForNiftyFifty.triggerFirstCalculation()

trigger_mail_2(getEmailMessage(), "DividendStocksFiltered_nimish.xlsx")

print("---------- Python Code Successfully Ran ---------")