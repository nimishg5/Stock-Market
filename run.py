import datetime as dt
import pandas as pd
import pandas_datareader.data as web

start = dt.datetime(2020,1,1)
end = dt.datetime(2020,7,19)

df = web.DataReader('RELIANCE.NS', 'yahoo', start, end)
df['200dma'] = df['Close'].rolling(window=200).mean()
df['50dma']  = df['Close'].rolling(window=50).mean()
# df.dropna(inplace=True)

# df1 = df['200dma']
# df2 = df['50dma']

# df2.index = df1.index

# total_df = pd.concat([df1, df2], axis = 1)

print(df.tail())