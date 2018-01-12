# 

#Summary of major findings (project-one, "Analyzing for “Hidden Patterns” in Apple’s Stock Market Data")

## Sum

1. Are there certain months that are better for buying or selling Apple Stock? 
2. Does the RSI give more accurate signals on a larger timeframe than on a smaller timeframe in identifying overbought and oversold conditions for Apple stock?
3. Is it possible to do any predictive analysis based on these patterns? (linear regression/line fit?)
4. Is Apple currently overvalued or oversold based selected historical data (i.e. 2015-2017)?

## Project Components

### api_component.py

Component to pull specified data from the Alphavantage API, and store in both raw JSON and in a formatted CSV.

### main.py

Component to parse data from CSV and visualize closing price, volume, and RSI for a stock using matplotlib subplots.

### multi_year.py

Component to parse data from CSV and visualize closing price for a stock over three years using matplotlib.

### data_clean_up_analysis.ipynb

Juptyer Notebook summarizing the data exploration, data cleanup, and final analysis of this project. 



## 