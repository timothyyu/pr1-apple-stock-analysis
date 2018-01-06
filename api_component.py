#Imports

import pandas as pd
from pandas.io.json import json_normalize
import numpy as np
from matplotlib import pyplot as plt
import json
import requests 
import csv

#API request

#Text document that is untracked (not pushed to git) with API key
#Create a file called untracked_api_key.txt with your key and DO NOT add to git when commiting or pushing changes

with open('untracked_api_key.txt', 'r') as file_object:
		api_key = file_object.readline()

stock_ticker = "AAPL"
target_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="+stock_ticker+"&outputsize=full&apikey="+api_key
print("API request: " + target_url)

apple_raw = requests.get(target_url).json()

with open('apple_raw','w+') as outfile:
	json.dump(apple_raw, outfile)

df = pd.DataFrame.from_dict(apple_raw["Time Series (Daily)"], orient='index')
df.reset_index(inplace=True)
df = df.rename(columns={"index":"timestamp","1. open":"open","2. high":"high","3. low":"low","4. close":"close","5. volume":"volume"})
df.to_csv("apple_raw.csv",index = False)

#Parse data

#Check data for errors/missing datapoints

#Visualize data

#Data analysis

