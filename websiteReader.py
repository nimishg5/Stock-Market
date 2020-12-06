import requests 
from bs4 import BeautifulSoup
from datetime import datetime
import schedule
import time

def moneyControl(url, dateIndex):
    response = requests.get(url)
    bonusOrDividend = ''
    if response.status_code==200:
        soup=BeautifulSoup(response.text,'html.parser')
        scripts=soup.find("table",{"class":"b_12 dvdtbl"})
        
        if "bonus" in url: 
            bonusOrDividend = 'bonus'
        else:
            bonusOrDividend = 'dividend'

        scriptBonusAnnounceMentDateDict = {}
        format = '%d-%m-%Y' # The format 
        today = datetime.today()
        for script in scripts.findAll("tr")[2:]: # for skipping 1st 2 enteries we have added the last condition
            key = script.findChildren()[1].text
            value = script.findChildren()[dateIndex].text

            announcementDate = datetime.strptime(value,format)
            delta = today - announcementDate
            if (delta.days < 7):
                scriptBonusAnnounceMentDateDict[key] = value
        
        print('Scripts for which '+ bonusOrDividend + ' is announced within 7 days are : ' + str(scriptBonusAnnounceMentDateDict) + '\n\n')
    else: 
        print("Error")

def job():
    moneyControl('https://www.moneycontrol.com/stocks/marketinfo/dividends_declared/index.php?sel_year=2020', 6)
    moneyControl('https://www.moneycontrol.com/stocks/marketinfo/bonus/index.php', 5)

# After every hour moneyControl() is called. 
schedule.every().hour.do(job)

while True:   
    schedule.run_pending() 
    time.sleep(1) 
