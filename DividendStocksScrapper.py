# # Import required modules
import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv
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
def getFields(record):
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
        records.append(getFields(record))

    df = pd.concat([df, pd.DataFrame(records, columns=columns)], ignore_index=True)
    return df
def driver_func():
    # Driver Code
    url = "https://www.moneycontrol.com/stocks/marketinfo/dividends_declared/homebody.php"
    table = generate_raw(url)
    df = get_df_from_table(table)
    df = df.drop(df.index[:4])
    df = df.reset_index(drop=True)
    stocks = df['Company'].tolist()
    pattern = r'<b>(.*?)</b>'
    matches = []
    for stock in stocks:
        match = re.search(pattern, stock)
        if match:
            matches.append(match.group(1))

    df1 = pd.DataFrame()
    df1['Company'] = matches
    df1['Type'] = df['Type'].copy()
    df1['Percentage'] = df['Percentage'].copy()
    df1['Announcement'] = df['Announcement'].copy()
    df1['Record'] = df['Record'].copy()
    df1['Ex-Dividend'] = df['Ex-Dividend'].copy()

    # Convert 'Announcement' column to datetime type
    df1['Announcement'] = pd.to_datetime(df1['Announcement'], format='%d-%m-%Y')
    # Convert 'Percentage' column to numeric type
    df1['Percentage'] = pd.to_numeric(df1['Percentage'])
    # Calculate the date before 4 days
    four_days_ago = datetime.now() - timedelta(days=15)
    # Filter the DataFrame
    filtered_df = df1[(df1['Announcement'] > four_days_ago) & (df1['Percentage'] > 100)]

    filtered_df.to_excel('DividendStocksFiltered2.xlsx')
