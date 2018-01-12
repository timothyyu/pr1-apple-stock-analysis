#Imports
import pandas as pd
import matplotlib.pyplot as pp
import seaborn
import numpy as np
import matplotlib.dates as mdate

import datetime as dt

from matplotlib.ticker import ScalarFormatter, FormatStrFormatter

#Parse data
stock_pd = pd.read_csv("apple_raw.csv")
rsi_pd = pd.read_csv("apple_raw_rsi.csv")
#stock_pd = pd.read_csv("daily_MSFT.csv")
stock_pd.head()

stock_pd1 = stock_pd.sort_values(by='timestamp')
stock_pd1.set_index('timestamp', inplace=True)
stock_pd2 = stock_pd.sort_values(by='timestamp')
stock_pd2.set_index('timestamp', inplace=True)
stock_pd3 = stock_pd.sort_values(by='timestamp')
stock_pd3.set_index('timestamp', inplace=True)

rsi_pd1 = rsi_pd.sort_values(by='timestamp')
rsi_pd1.set_index('timestamp', inplace=True)
rsi_pd2 = rsi_pd.sort_values(by='timestamp')
rsi_pd2.set_index('timestamp', inplace=True)
rsi_pd3 = rsi_pd.sort_values(by='timestamp')
rsi_pd3.set_index('timestamp', inplace=True)

#print(stock_pd)

month_ticks = ("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec")
#x_pos = [i for i, _ in enumerate(month_ticks)]
#x_pos=[0,25,50,75,100,250,150,175,200,250,200,220]
x_pos = np.arange(0,300,22,dtype=None)

#try:

##  STOCK Closing Price Chart
max_closing = stock_pd1.truncate(before=str('2017-01-01'), after=str('2017-12-31'))["close"].max() + 20

pp.subplot(3,1,1)
pp.ylim(50,max_closing)
pp.ylabel("Stock Price ($) - " + "AAPL")

pp.xticks(x_pos, month_ticks)

stock_pd1.truncate(before=str('2017-01-01'), after=str('2017-12-31'))['close'].plot(figsize=(12,12), color="red")

pp.subplot(3,1,2)
pp.ylim(50,max_closing)
pp.ylabel("Stock Price ($) - " + "AAPL")
pp.xticks(x_pos, month_ticks)
stock_pd2.truncate(before=str('2016-01-01'), after=str('2016-12-31'))['close'].plot(figsize=(12,12), color="purple")

pp.subplot(3,1,3)
pp.ylim(50,max_closing)
pp.ylabel("Stock Price ($) - " + "AAPL")
pp.xticks(x_pos, month_ticks)
stock_pd3.truncate(before=str('2015-01-01'), after=str('2015-12-31'))['close'].plot(figsize=(12,12), color="orange")

pp.subplots_adjust(hspace=0.5)

ax = pp.subplot(3,1,1)
ax.set_xlabel('Year 2017')
labels = [item.get_text() for item in ax.get_xticklabels()]

labels[0] = 'Jan'
labels[1] = 'Feb'
labels[2] = 'May'
labels[3] = 'Apr'
labels[4] = 'May'
labels[5] = 'Jun'
labels[6] = 'Jul'
labels[7] = 'Aug'
labels[8] = 'Sep'
labels[9] = 'Oct'
labels[10] = 'Nov'
labels[11] = 'Dec'

ax.set_xticklabels(labels)


ax = pp.subplot(3,1,2)
ax.set_xlabel('Year 2016')
labels = [item.get_text() for item in ax.get_xticklabels()]

labels[0] = 'Jan'
labels[1] = 'Feb'
labels[2] = 'May'
labels[3] = 'Apr'
labels[4] = 'May'
labels[5] = 'Jun'
labels[6] = 'Jul'
labels[7] = 'Aug'
labels[8] = 'Sep'
labels[9] = 'Oct'
labels[10] = 'Nov'
labels[11] = 'Dec'

ax.set_xticklabels(labels)

ax = pp.subplot(3,1,3)
ax.set_xlabel('Year 2015')
labels = [item.get_text() for item in ax.get_xticklabels()]

labels[0] = 'Jan'
labels[1] = 'Feb'
labels[2] = 'May'
labels[3] = 'Apr'
labels[4] = 'May'
labels[5] = 'Jun'
labels[6] = 'Jul'
labels[7] = 'Aug'
labels[8] = 'Sep'
labels[9] = 'Oct'
labels[10] = 'Nov'
labels[11] = 'Dec'

ax.set_xticklabels(labels)
pp.show()

###############
## RSI Chart
###############

pp.subplot(3,1,1)
pp.ylim(20,100)
pp.axhline(y=30)
pp.axhline(y=70)
pp.ylabel("RSI Index - " + "AAPL")
pp.xticks(x_pos, month_ticks)
rsi_pd1.truncate(before=str('2017-01-01'), after=str('2017-12-31'))['RSI'].plot(figsize=(12,12), color="red")

pp.subplot(3,1,2)
pp.ylim(20,100)
pp.axhline(y=30)
pp.axhline(y=70)
pp.ylabel("RSI Index - " + "AAPL")
pp.xticks(x_pos, month_ticks)
#pp.axhline(y=30, color='r', linestyle='-')

rsi_pd2.truncate(before=str('2016-01-01'), after=str('2016-12-31'))['RSI'].plot(figsize=(12,12), color="purple")

pp.subplot(3,1,3)
pp.ylim(20,100)
pp.axhline(y=30)
pp.axhline(y=70)
pp.ylabel("RSI Index - " + "AAPL")
pp.xticks(x_pos, month_ticks)


rsi_pd3.truncate(before=str('2015-01-01'), after=str('2015-12-31'))['RSI'].plot(figsize=(12,12), color="orange")

pp.subplots_adjust(hspace=0.5)

ax = pp.subplot(3,1,1)

ax.set_xlabel('Year 2017')

labels = [item.get_text() for item in ax.get_xticklabels()]

labels[0] = 'Jan'
labels[1] = 'Feb'
labels[2] = 'May'
labels[3] = 'Apr'
labels[4] = 'May'
labels[5] = 'Jun'
labels[6] = 'Jul'
labels[7] = 'Aug'
labels[8] = 'Sep'
labels[9] = 'Oct'
labels[10] = 'Nov'
labels[11] = 'Dec'

ax.set_xticklabels(labels)

ax = pp.subplot(3,1,2)
ax.set_xlabel('Year 2016')

labels = [item.get_text() for item in ax.get_xticklabels()]

labels[0] = 'Jan'
labels[1] = 'Feb'
labels[2] = 'May'
labels[3] = 'Apr'
labels[4] = 'May'
labels[5] = 'Jun'
labels[6] = 'Jul'
labels[7] = 'Aug'
labels[8] = 'Sep'
labels[9] = 'Oct'
labels[10] = 'Nov'
labels[11] = 'Dec'

ax.set_xticklabels(labels)

ax = pp.subplot(3,1,3)
ax.set_xlabel('Year 2015')
labels = [item.get_text() for item in ax.get_xticklabels()]

labels[0] = 'Jan'
labels[1] = 'Feb'
labels[2] = 'May'
labels[3] = 'Apr'
labels[4] = 'May'
labels[5] = 'Jun'
labels[6] = 'Jul'
labels[7] = 'Aug'
labels[8] = 'Sep'
labels[9] = 'Oct'
labels[10] = 'Nov'
labels[11] = 'Dec'

ax.set_xticklabels(labels)

pp.show()

#################
##
## Volume Chart
##
#################



max_vol = stock_pd1.truncate(before=str('2015-01-01'), after=str('2017-12-31'))["volume"].max() + 1000000



pp.subplot(3,1,1)
pp.ylim(50,max_vol)
pp.ylabel("Volume (in 100 Million) - " + "AAPL")
pp.xticks(x_pos, month_ticks)
stock_pd1.truncate(before=str('2017-01-01'), after=str('2017-12-31'))['volume'].plot(figsize=(12,12), color="red")

pp.subplot(3,1,2)
pp.ylim(50,max_vol)
pp.ylabel("Volume (in 100 Million) - " + "AAPL")
pp.xticks(x_pos, month_ticks)
stock_pd2.truncate(before=str('2016-01-01'), after=str('2016-12-31'))['volume'].plot(figsize=(12,12), color="purple")

pp.subplot(3,1,3)
pp.ylim(50,max_vol)
pp.ylabel("Volume (in 100 Million) - " + "AAPL")
pp.xticks(x_pos, month_ticks)
stock_pd3.truncate(before=str('2015-01-01'), after=str('2015-12-31'))['volume'].plot(figsize=(12,12), color="orange")

pp.subplots_adjust(hspace=0.5)

ax = pp.subplot(3,1,1)
ax.set_xlabel('Year 2017')
labels = [item.get_text() for item in ax.get_xticklabels()]

labels[0] = 'Jan'
labels[1] = 'Feb'
labels[2] = 'May'
labels[3] = 'Apr'
labels[4] = 'May'
labels[5] = 'Jun'
labels[6] = 'Jul'
labels[7] = 'Aug'
labels[8] = 'Sep'
labels[9] = 'Oct'
labels[10] = 'Nov'
labels[11] = 'Dec'

ax.set_xticklabels(labels)


ax = pp.subplot(3,1,2)
ax.set_xlabel('Year 2016')
labels = [item.get_text() for item in ax.get_xticklabels()]

labels[0] = 'Jan'
labels[1] = 'Feb'
labels[2] = 'May'
labels[3] = 'Apr'
labels[4] = 'May'
labels[5] = 'Jun'
labels[6] = 'Jul'
labels[7] = 'Aug'
labels[8] = 'Sep'
labels[9] = 'Oct'
labels[10] = 'Nov'
labels[11] = 'Dec'

ax.set_xticklabels(labels)

ax = pp.subplot(3,1,3)
ax.set_xlabel('Year 2015')

labels = [item.get_text() for item in ax.get_xticklabels()]
labels[0] = 'Jan'
labels[1] = 'Feb'
labels[2] = 'May'
labels[3] = 'Apr'
labels[4] = 'May'
labels[5] = 'Jun'
labels[6] = 'Jul'
labels[7] = 'Aug'
labels[8] = 'Sep'
labels[9] = 'Oct'
labels[10] = 'Nov'
labels[11] = 'Dec'

ax.set_xticklabels(labels)


pp.show()



