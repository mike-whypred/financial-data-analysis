# Time Series

Time series data plays an important role in financial markets as it exists in various forms, such as historical share price and trading volume data, or economic indicators. Python offers various functions that make it quick and easy to analyse time series data.


## Getting Started

In your Python IDE (whether it is Collab, Jupyter Notebook or Spyder), first let's import the required libraries for this module.

```
### import libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime, timedelta
```


## Import Data

For this module, we will be using the historical share price for Nvidia. We will be using the **yfinance** library to obtain our data.

```
### import data

ticker = 'NVDA'
nvda = yf.Ticker(ticker)


# define start and end dates
start = datetime(2020,1,1)
end = datetime.now()

# get historical share prices
nvda_prices = nvda.history(start = start, end = end, interval = "1d")

# reset index so date index is a regular column
nvda_prices = nvda_prices.reset_index()
```

Here we have imported the historical daily share price data for Nvidia from 01/01/2020 till the present day. By default, yfinance sets the date column as the index for the dataframe - we would like the date column to be a regular column so we use **reset_index()** to reset the dataframe index.

## Extract Strings for Various Periods

When working with time series data, there may be instances where we wish to analyse patterns based on specific days, weeks, months or years. We can use **dt** to extract day, week, month, quarter and year values from time series data. 

```
# get day
nvda_prices['day'] = nvda_prices['Date'].dt.day

# get week
nvda_prices['week'] = nvda_prices['Date'].dt.isocalendar().week

# get month
nvda_prices['month'] = nvda_prices['Date'].dt.month

# get quarter
nvda_prices['quarter'] = nvda_prices['Date'].dt.quarter

# get year
nvda_prices['year'] = nvda_prices['Date'].dt.year

# get stock prices for Q2 of 2023
nvda_prices_q2_2023 = nvda_prices[(nvda_prices['quarter'] == 2) & (nvda_prices['year'] == 2023)]
```

We can use these values to also filter down our time series data, e.g. filtering down to stock prices in Q2 of 2023 in the above example.


## Date Based Arithmetic Operations

Python has functions that allow us to manipulate dates. We can use functions such as **timedelta** or **DateOffset** to add or subtract from our date series.

```
# add 1 day to date index
# multiple approaches

nvda_prices['New_Date'] = nvda_prices['Date'] + timedelta(days = 1)
nvda_prices['New_Date'] = nvda_prices['Date'] + pd.DateOffset(days = 1)

# subtract 5 months from date index

nvda_prices['New_Month'] = nvda_prices['Date'] - pd.DateOffset(months = 5)
```

**timedelta** only allows us to manipulate dates by days, whereas **DateOffset** is able to manipulate dates with many more time units, from seconds, hours, days, through to weeks, months and years.

## Leading/Lagging Time Series using Shift

When working with multiple time series datasets, we may wish to determine if one time series is a leading or lagging indicator of another. We can use **shift** to move a time series upwards or downwards in our dataframe by a specified number of periods.

```
## Example 1

nvda_prices_shift = nvda_prices.copy()

nvda_prices_shift = nvda_prices_shift.drop(['New_Date', 'New_Month'], axis = "columns")

# shift close prices forward by 30 days
nvda_prices_shift['Close'] = nvda_prices_shift['Close'].shift(30)
nvda_prices_shift.head()

# shift open prices back by 15 days
nvda_prices_shift['Open'] = nvda_prices_shift['Open'].shift(-15)
nvda_prices_shift.tail()
```
In this next example, we want to compare Nvidia's recent share price rally to Cisco's (back in the Dotcom bubble period). 

```
## Example 2 - compare Cisco to Nvidia

# get cisco prices

ticker = 'CSCO'
csco = yf.Ticker(ticker)


# define start and end dates
start = datetime(1998,1,1)
end = datetime.now()

# get historical share prices
csco_prices = csco.history(start = start, end = end, interval = "1d")

# reset index so date index is a regular column
csco_prices = csco_prices.reset_index()

# rename close price column
csco_prices = csco_prices.rename(columns = {'Close': 'CSCO_Close'})
 

# get Nvidia prices

ticker = 'NVDA'
nvda = yf.Ticker(ticker)

# define start and end dates
start = datetime(1998,1,1) # note NVDA IPO'd in 1999
end = datetime.now()

# get historical share prices
nvda_prices = nvda.history(start = start, end = end, interval = "1d")

# reset index so date index is a regular column
nvda_prices = nvda_prices.reset_index()
 
# rename close price column
nvda_prices = nvda_prices.rename(columns = {'Close': 'NVDA_Close'})
 

# combine Cisco and Nvida close price

df = pd.concat([csco_prices[['Date', 'CSCO_Close']]], axis = 1)
                
df = csco_prices[['Date', 'CSCO_Close']]            

# map NVDA price to CSCO price using date index                
df['NVDA_Close'] = df['Date'].map(nvda_prices.set_index('Date')['NVDA_Close'])


# calculate daily returns
df[['CSCO_Daily_Rtn', 'NVDA_Daily_Rtn']] = df[['CSCO_Close', 'NVDA_Close']].pct_change()


# shift CSCO close price and daily return by 26 years
df['CSCO_Close_Shift'] = df['CSCO_Close'].shift(252 * 25)
df['CSCO_Daily_Rtn_Shift'] = df['CSCO_Daily_Rtn'].shift(252 * 25)

```
So far we have obtained the historical share prices for both Nvidia and Cisco, and combined the close prices into a single dataframe. We then calculated the daily returns, and then shifted Cisco's daily returns forward by 25 years (to align its Dotcom rally with the start of Nvidia's recent rally).


```
# drop empty rows
df = df.dropna()


# calculate cumulative returns
df[['NVDA_Cum_Rtn', 'CSCO_Shift_Cum_Rtn']] = (1 + df[['NVDA_Daily_Rtn', 'CSCO_Daily_Rtn_Shift']]).cumprod() - 1


# plot cumulative returns for NVDA vs shifted CSCO
plt.figure(figsize = (10, 6))
plt.plot(df['NVDA_Cum_Rtn'].values, label = 'NVDA')
plt.plot(df['CSCO_Shift_Cum_Rtn'].values, label = 'CSCO_Shift')
plt.legend()
plt.show()
```

Shifting time series data will result in empty rows in our dataframe. Here we have used **dropna()** to drop the empty rows to tidy up the dataframe. Next we calculate the cumulative returns from the daily returns for both Nvidia and Cisco, and then plotted these returns. You can see that Nvidia's price rally has been more aggressive than Cisco's.

## Sampling

We may wish to perform sampling on our time series data if it is more granular than our requirements (e.g. obtaining week-end or month-end prices from daily prices data). We can use **resample** whilst specifying the desired time period as an argument to perform this operation.


```
# set index before sampling
nvda_prices.set_index('Date', inplace = True)

# get week end price
nvda_prices_week = nvda_prices['NVDA_Close'].resample('W').last()

# get month end price
nvda_prices_mth = nvda_prices['NVDA_Close'].resample('M').last()

```


## Creating Date Ranges

If we wish to analyse a specific date range in our time series data, we can use various methods to filter down our dataset.

This first example shows how to filter time series data to a specific date range, if the date column is set as the index of the dataframe.

```
# if date column is index

start_date = '2024-01-01'
end_date = '2024-02-28'

price_range = nvda_prices.loc[start_date: end_date]
```
This second example shows how to filter time series data to a specific date range if the date column is a regular column in the dataframe.

```
# if date column is not index
nvda_prices = nvda_prices.reset_index()

# filter df using date column
price_range = nvda_prices[(nvda_prices['Date'] >= start_date) & (nvda_prices['Date'] <= end_date)]
```