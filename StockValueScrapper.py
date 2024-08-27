import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from datetime import datetime, timedelta

# Headers
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

# Columns
columns = ['Company', 'Type', 'Percentage', 'Announcement', 'Record', 'Ex-Dividend']

# Generate raw data
def generate_raw(url):
    response = requests.get(url, headers=headers, timeout=10)
    soup = BeautifulSoup(response.content, 'html5lib')
    table = soup.findAll('tr')
    return table

# Get the relevant fields
def get_fields(record):
    data = record.findAll('td')
    processed_record = []
    for item in data:
        processed_record.append(item.decode_contents())
    return processed_record

# Build a dataframe from table
def get_df_from_table(table):
    df = pd.DataFrame(columns=columns)
    records = []
    for record in table:
        records.append(get_fields(record))

    df = pd.concat([df, pd.DataFrame(records, columns=columns)], ignore_index=True)
    return df

def driver_func(stock_name , symbol):
     # Driver Code
    url = "https://www.moneycontrol.com/company-facts/"+stock_name+"/dividends"+symbol
    table = generate_raw(url)
    df = get_df_from_table(table)
    df = df.drop(df.index[:4])
    df = df.reset_index(drop=True)
    return df
