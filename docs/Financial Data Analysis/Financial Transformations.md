# Financial Transformations

When working with time series data, it may to be necessary to transform the data. For example, if the time series data exhibits highly seasonal behaviour we may wish to smooth it out using moving averages in order to identify longer term trends. 

In other cases, we may have multiple time series in a dataframe and wish to perform operations across rows (e.g. calculating portfolio returns from individual stocks).

## Getting Started

In your Python IDE (whether it is Collab, Jupyter Notebook or Spyder), first let's import the required libraries for this module.

```
### import libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime, timedelta
import math
```


## Import Data

In this module, we will be using historical share price data of Nvidia and Microsoft from the **yfinance** library.

```
# define list of tickers
ticker_list = ['NVDA', 'MSFT'] 
ticker_list.sort() # sort tickers in alphabetical order

# join tickers in single string to feed into API
tickers_join = ' '.join(ticker_list)

```

The **yfinance** library returns price data for a list of tickers in alphabetical order, regardless of the order of the tickers in our list. In order to avoid confusion, we will sort our list of tickers.

```
# define start and end dates
start = datetime(2020,1,1)
end = datetime.now()

# initialise tickers object
data = yf.download(tickers_join, start = start, end = end, interval = "1d")

# get price data out
data_filter = data.filter(regex = 'Adj Close')

```

We only need the Adjusted Close price data for the stocks, so we can use **regex** to filter the dataframe for just these columns.


```
# rename column headers to get rid of multi-level column headers
data_filter.columns = ticker_list

# reset index to date index is a regular column
data_filter = data_filter.reset_index()

### calculate price returns

data_filter[['MSFT_Daily_Rtn', 'NVDA_Daily_Rtn', ]] = data_filter[['MSFT', 'NVDA']].pct_change()
```

Finally we can rename the columns of our filtered dataframe, and calculate the daily returns based on the daily share prices.


## Row-Wise Calculations

In this simple example, let's assume we have a portfolio of 2 stocks, that maintains a 50% allocation to each stock on a daily basis. With this simplistic assumption, we can then easily calculate the daily portfolio return.


```
# assume 50/50 allocation to 2 stocks
# calculate return of the stock portfolio

data_filter['Portfolio_Rtn'] =  0.5 * data_filter['MSFT_Daily_Rtn'] + 0.5 * data_filter['NVDA_Daily_Rtn']

```

We can also perform other row-wise calculations, such as calculating the ratio of one stock's daily returns relative to another.

```
# calculate ratio of NVDA return to MSFT return

data_filter['Ratio'] = data_filter['NVDA_Daily_Rtn'] / data_filter['MSFT_Daily_Rtn']
```



## Rolling Calculations

The following are examples of rolling calculations that can be performed on time series data.

### Cumulative Returns

```
# cumulative returns

data_filter['NVDA_Cum_Rtn'] = (1 + data_filter['NVDA_Daily_Rtn']).cumprod() - 1

```

### Moving Averages

```
# get 50d and 200d MAs

data_filter['NVDA_Rolling_50d'] = data_filter['NVDA'].rolling(window = 50).mean()
data_filter['NVDA_Rolling_200d'] = data_filter['NVDA'].rolling(window = 200).mean()
```

### Rolling Standard Deviation

```
# 12-month rolling std dev annualised

n = 252
data_filter['NDVA_std_dev'] = data_filter['NVDA_Daily_Rtn'].rolling(window = n).std() * math.sqrt(252)
```

### Rolling Correlation

```
# correlation
data_filter['Correl'] = data_filter['NVDA_Daily_Rtn'].rolling(window = n).corr(data_filter['MSFT_Daily_Rtn'])
```



## Indexing Returns

Indexing returns is useful for comparing multiple time series e.g. comparing the cumulative returns of various stocks, by setting a common starting point and value.

```
### indexing returns

data_filter['NVDA_Indexed_Cum_Rtn'] = (1 + data_filter['NVDA_Daily_Rtn']).cumprod() * 100

data_filter['NVDA_Indexed_Cum_Rtn'].iloc[0] = 100 # set starting value to 100

data_filter['MSFT_Indexed_Cum_Rtn'] = (1 + data_filter['MSFT_Daily_Rtn']).cumprod() * 100

data_filter['MSFT_Indexed_Cum_Rtn'].iloc[0] = 100 # set starting value to 100

```



