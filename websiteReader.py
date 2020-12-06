import requests 
from bs4 import BeautifulSoup
from datetime import datetime

def moneyControl(url):   
    response = requests.get(url) 
    if response.status_code==200:
        soup=BeautifulSoup(response.text,'html.parser')
        scripts=soup.find("table",{"class":"b_12 dvdtbl"}) 

        scriptBonusAnnounceMentDateDict = {}
        format = '%d-%m-%Y' # The format 
        today = datetime.today()
        for script in scripts.findAll("tr")[2:]: # for skipping 1st 2 enteries we have added the last condition
            key = script.findChildren()[1].text
            value = script.findChildren()[5].text

            announcementDate = datetime.strptime(value,format)
            delta = today - announcementDate
            if (delta.days < 30):
                scriptBonusAnnounceMentDateDict[key] = value
        
        print('Scripts for which Bonus is announced within 30 days are : ' + str(scriptBonusAnnounceMentDateDict))
    else: 
        print("Error") 
          
moneyControl('https://www.moneycontrol.com/stocks/marketinfo/bonus/index.php')