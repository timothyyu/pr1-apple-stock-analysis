###Imports

import pandas as pd
from pandas.io.json import json_normalize
import numpy as np
from matplotlib import pyplot as plt
import json
import requests 
import csv
import os.path

###API request (price data and RSI)

#Load API key:
if os.path.isfile("untracked_api_key.txt") == True:
	with open('untracked_api_key.txt', 'r') as file_object:
		#Text document that is untracked in project-one directory (NOT pushed to git) with API key
		#Create a file called untracked_api_key.txt with your key and DO NOT add to git when commiting or pushing changes
		api_key = file_object.readline()
elif os.path.isfile("untracked_api_key.txt") == False:
	print("untracked_api_key.txt not in directory; please provide API key in a file named untracked_api_key.txt in the same directory.")

stock_ticker = "AAPL"

#Check if apple_raw and apple_raw.csv exists (i.e. do not run API request if request already completed/files are present)
if os.path.isfile("apple_raw") == False or os.path.isfile("apple_raw.csv") == False:
	
	#API request (price data)
	target_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="+stock_ticker+"&outputsize=full&apikey="+api_key
	
	print("API request: " + target_url)
	apple_raw = requests.get(target_url).json()

	#Save JSON response to file
	with open('apple_raw','w+') as outfile:
		json.dump(apple_raw, outfile,indent=4, sort_keys=True)

	#Save JSON response to CSV
	df = pd.DataFrame.from_dict(apple_raw["Time Series (Daily)"], orient='index')
	df.reset_index(inplace=True)
	df = df.rename(columns={"index":"timestamp","1. open":"open","2. high":"high","3. low":"low","4. close":"close","5. volume":"volume"})
	df['timestamp'] = df['timestamp'].astype('datetime64[ns]')
	df.to_csv("apple_raw.csv",date_format="%Y-%m-%d",index = False)

#Check if apple_raw_rsi and apple_raw_rsi.csv exists
if os.path.isfile("apple_raw_rsi") == False or os.path.isfile("apple_raw_rsi.csv") == False:

	#API request (RSI data for close price)
	target_url_rsi = "https://www.alphavantage.co/query?function=RSI&symbol="+stock_ticker+"&interval=daily&time_period=60&series_type=close&apikey="+api_key
	print("API request: " + target_url_rsi)

	apple_raw_rsi = requests.get(target_url_rsi).json()

	#Save JSON response to file
	with open('apple_raw_rsi','w+') as outfile:
		json.dump(apple_raw_rsi, outfile,indent=4, sort_keys=True)

	#Save JSON response to CSV
	df_rsi = pd.DataFrame.from_dict(apple_raw_rsi["Technical Analysis: RSI"], orient='index')
	df_rsi.reset_index(inplace=True)
	df_rsi = df_rsi.rename(columns={"index":"timestamp"})
	df_rsi['timestamp'] = df_rsi['timestamp'].astype('datetime64[ns]')
	df_rsi.to_csv("apple_raw_rsi.csv",date_format="%Y-%m-%d",index = False)

###Parse data

###Check data for errors/missing datapoints

###Visualize data

###Data analysis

