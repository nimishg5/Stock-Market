import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2000,1,1)
end = dt.datetime(2020,12,31)

df = web.DataReader('RELIANCE.NS', 'yahoo', start, end)
df['200dma'] = df['Adj Close'].rolling(window=200).mean()
df['50dma']  = df['Adj Close'].rolling(window=50).mean()
df.dropna(inplace=True)
#print(df)

df_ohlc = df['Adj Close'].resample('15D').ohlc()
df_volume = df['Volume'].resample('15D').sum()

df_ohlc.reset_index(inplace=True)

df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

ax1 = plt.subplot2grid((6,1), (0,0), rowspan = 5, colspan = 1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan = 1, colspan = 1, sharex = ax1)

ax1.xaxis_date()
ax1.plot(df.index, df['Adj Close'])
ax1.plot(df.index, df['200dma'])
ax1.plot(df.index, df['50dma'])

candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g', colordown='r')
ax2.fill_between(df_volume.index.map(mdates.date2num), df_volume.values, 0)

#df['Adj Close'].plot()
plt.show()