#Imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn
import numpy as np
import matplotlib.dates as mdate
import datetime as dt

#Parse data
stock_pd = pd.read_csv("apple_raw.csv")
rsi_pd = pd.read_csv("apple_raw_rsi.csv")

#verify column datatypes
#print(stock_pd.dtypes)

stock_pd = pd.read_csv('apple_raw.csv',parse_dates=['timestamp'])
stock_pd = stock_pd.sort_values(by='timestamp')
stock_pd.drop(['open','high','low'],axis = 1, inplace = True)
stock_pd.set_index('timestamp',inplace=True)

#Multi-year color chart closing price (all three years)
stock_pd.truncate(before=str('2017-01-01'), after=str('2017-12-31'))['close'].plot(figsize=(16, 12), color="red")
stock_pd.truncate(before=str('2016-01-01'), after=str('2016-12-31'))['close'].plot(figsize=(16, 12), color="purple")
stock_pd.truncate(before=str('2015-01-01'), after=str('2015-12-31'))['close'].plot(figsize=(16, 12), color="orange")
plt.title("Apple Stock Closing Price between Year 2015 - 2017")
plt.xlabel("Year 2015 - 2017")
plt.ylabel("Stock Closing Price ($)")
plt.savefig('2015-2017 Apple close single chart.png')
plt.show()




'''
#Individual year and closing price
#'timestamp' column set as index ---> able to to use dataframe to filter for plot
stock_pd['2015']['close'].plot(figsize=(16, 12))
plt.show()
plt.savefig('2015 close')

stock_pd['2016']['close'].plot(figsize=(16, 12))
plt.show()
plt.savefig('2016 close')

stock_pd['2017']['close'].plot(figsize=(16, 12))
plt.show()
plt.savefig('2017 close')
'''


#stock_pd_2015 = stock_pd['2015']
#stock_pd_2016 = stock_pd['2016']
#stock_pd_2017 = stock_pd['2017']


#Debugging

#print(stock_pd.head())

#truncate function does not modify dataframe
#stock_pd =stock_pd.truncate(before=str('2015-01-01'), after=str('2017-12-31'))['close'].plot(figsize=(16, 12))
