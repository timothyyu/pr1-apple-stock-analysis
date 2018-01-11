#Imports
import pandas as pd
import matplotlib.pyplot as pp
import seaborn
import numpy as np
import matplotlib.dates as mdate

import datetime as dt

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
pp.subplot(3,1,1)
pp.ylim(50,220)
pp.ylabel("Stock Price ($) - " + "AAPL")

pp.xticks(x_pos, month_ticks)

stock_pd1.truncate(before=str('2017-01-01'), after=str('2017-12-31'))['close'].plot(figsize=(12,12), color="red")

pp.subplot(3,1,2)
pp.ylim(50,220)
pp.ylabel("Stock Price ($) - " + "AAPL")
pp.xticks(x_pos, month_ticks)
stock_pd2.truncate(before=str('2016-01-01'), after=str('2016-12-31'))['close'].plot(figsize=(12,12), color="purple")

pp.subplot(3,1,3)
pp.ylim(50,220)
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
pp.axhline(y=70,linestyle =':')
pp.axhline(y=30,linestyle =':')
pp.ylabel("RSI Index - " + "AAPL")
pp.xticks(x_pos, month_ticks)
rsi_pd1.truncate(before=str('2017-01-01'), after=str('2017-12-31'))['RSI'].plot(figsize=(12,12), color="red")

pp.subplot(3,1,2)
pp.ylim(20,100)
pp.axhline(y=70,linestyle =':')
pp.axhline(y=30,linestyle =':')
pp.ylabel("RSI Index - " + "AAPL")
pp.xticks(x_pos, month_ticks)
rsi_pd2.truncate(before=str('2016-01-01'), after=str('2016-12-31'))['RSI'].plot(figsize=(12,12), color="purple")

pp.subplot(3,1,3,)
pp.ylim(20,100)
pp.axhline(y=70,linestyle =':')
pp.axhline(y=30,linestyle =':')
pp.ylabel("RSI Index - " + "AAPL")
pp.xticks(x_pos, month_ticks)
rsi_pd3.truncate(before=str('2015-01-01'), after=str('2015-12-31'))['RSI'].plot(figsize=(12,12), color="orange")

pp.subplots_adjust(hspace=0.5)

ax = pp.subplot(3,1,1,)
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

for label in ax.get_xticklabels():
     label.set_horizontalalignment('right')

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

'''
pp.subplot(3,2,1)
pp.ylim(20,100)
pp.ylabel("RSI Index - " + "AAPL")
rsi_pd1.truncate(before=str('2017-01-01'), after=str('2017-12-31'))['RSI'].plot(figsize=(12,12), color="red")

pp.subplot(3,2,2)
pp.ylim(20,100)
pp.ylabel("RSI Index - " + "AAPL")
rsi_pd2.truncate(before=str('2016-01-01'), after=str('2016-12-31'))['RSI'].plot(figsize=(12,12), color="purple")

pp.subplot(3,2,3)
pp.ylim(20,100)
pp.ylabel("RSI Index - " + "AAPL")
rsi_pd3.truncate(before=str('2015-01-01'), after=str('2015-12-31'))['RSI'].plot(figsize=(12,12), color="orange")

pp.subplots_adjust(hspace=0.5)

ax = pp.subplot(3,2,1)
ax.set_xlabel('Year 2017')
labels = [item.get_text() for item in ax.get_xticklabels()]

labels[0] = 'Jan-2017'
labels[1] = 'Mar-2017'
labels[2] = 'May-2017'
labels[3] = 'Aug-2017'
labels[4] = 'Oct-2017'
labels[5] = 'Dec-2017'
ax.set_xticklabels(labels)

ax = pp.subplot(3,2,2)
ax.set_xlabel('Year 2016')
labels = [item.get_text() for item in ax.get_xticklabels()]

labels[0] = 'Jan-2016'
labels[1] = 'Mar-2016'
labels[2] = 'May-2016'
labels[3] = 'Aug-2016'
labels[4] = 'Oct-2016'
labels[5] = 'Dec-2016'
ax.set_xticklabels(labels)

ax = pp.subplot(3,2,3)
ax.set_xlabel('Year 2015')
labels = [item.get_text() for item in ax.get_xticklabels()]

labels[0] = 'Jan-2015'
labels[1] = 'Mar-2015'
labels[2] = 'May-2015'
labels[3] = 'Aug-2015'
labels[4] = 'Oct-2015'
labels[5] = 'Dec-2015'
ax.set_xticklabels(labels)

pp.show()

'''
print("here")

month_ticks = ("Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec")
x_pos = [i for i, _ in enumerate(month_ticks)]

pp.xticks(x_pos, month_ticks)

vol_list=stock_pd1.truncate(before=str('2017-01-01'), after=str('2017-12-31'))['volume']
print(vol_list)
#pp.subplot(3,1,1)
#pp.ylim(20,10000000000)
pp.ylabel("Trading Volume (in Million) - " + "AAPL")
#stock_pd1.truncate(before=str('2017-01-01'), after=str('2017-12-31'))['volume'].plot(kind="bar",figsize=(250,250), color="red")
pp.bar( x_pos, vol_list , color='red')
pp.show()


'''
pp.subplot(3,1,2)
pp.ylim(20,1000000)
pp.ylabel("Trading Volume (in Million) - " + "AAPL")
#stock_pd2.truncate(before=str('2016-01-01'), after=str('2016-12-31'))['volume'].plot(kind='bar',figsize=(12,12), color="purple")


pp.subplot(3,1,3)
pp.ylim(20,10000000000)
pp.ylabel("Trading Volume (in Million) - " + "AAPL")
#stock_pd3.truncate(before=str('2015-01-01'), after=str('2015-12-31'))['volume'].plot(figsize=(12,12), color="orange")
x=len(stock_pd3.truncate(before=str('2015-01-01'), after=str('2015-12-31'))['volume'])
#pp.bar(x,stock_pd3.truncate(before=str('2015-01-01'), after=str('2015-12-31'))['volume'], width=0.8)
pp.subplots_adjust(hspace=0.5)

ax = pp.subplot(3,2,1)
ax.set_xlabel('Year 2017')
labels = [item.get_text() for item in ax.get_xticklabels()]

labels[0] = 'Jan-2017'
labels[1] = 'Mar-2017'
labels[2] = 'May-2017'
labels[3] = 'Aug-2017'
labels[4] = 'Oct-2017'
labels[5] = 'Dec-2017'
ax.set_xticklabels(labels)

ax = pp.subplot(3,2,2)
ax.set_xlabel('Year 2016')
labels = [item.get_text() for item in ax.get_xticklabels()]

labels[0] = 'Jan-2016'
labels[1] = 'Mar-2016'
labels[2] = 'May-2016'
labels[3] = 'Aug-2016'
labels[4] = 'Oct-2016'
labels[5] = 'Dec-2016'
ax.set_xticklabels(labels)

ax = pp.subplot(3,2,3)
ax.set_xlabel('Year 2015')
labels = [item.get_text() for item in ax.get_xticklabels()]

labels[0] = 'Jan-2015'
labels[1] = 'Mar-2015'
labels[2] = 'May-2015'
labels[3] = 'Aug-2015'
labels[4] = 'Oct-2015'
labels[5] = 'Dec-2015'
ax.set_xticklabels(labels)

#pp.show()


#except:
#	print("error")
'''
