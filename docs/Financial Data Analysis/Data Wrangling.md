# Data Wrangling

Data wrangling serves an important role in the initial stages of data analysis. Raw data obtained from a source may often contain inconsistencies, such as missing values, various formats or errors. Data wrangling addresses these issues by transforming the raw data into a well-structured and standardised format.

## Getting Started

In your Python IDE (whether it is Collab, Jupyter Notebook or Spyder), first let's import the required libraries for this module.

``` 
### import libraries

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from sklearn.preprocessing import MinMaxScaler
```

Next, save the CSV file that we will be using for this module in your desired folder directory. We can then import the data from the CSV file, by using **pd.read_csv** and specifying the file path:

``` 
### import data

path = r'paste\your\folder\directory\here'
file = 'asx_etp_202401.csv'

file_path = os.path.join(path, file)

data = pd.read_csv(file_path)
```

## Initial Data Inspection

Before carrying out data wrangling, we can use various techniques to inspect the raw data to get a sense for the nature of the data, as well as any issues (either related to the data itself, or formatting) which we need to issue.


```
# get dataframe info
data.info()
```
We can use **data.info()** to get information on the dataframe, e.g. the number of rows and columns, the type of data contained in each column, and number of non-null values (non-empty cells) in each column.


```
# head of dataframe
data.head()
```
We can use **data.head()** to see the first 5 rows of our dataframe in the console of our IDE. This is a convenient way to quickly take a look at the data.


```
# dimensions of dataframe
data.shape
```

We can use **data.shape** to determine the dimensions of the dataframe (i.e. the number of rows and columns).


## Check for Missing Values

It is useful to also check for null or missing values in dataframes. Null values may cause distorted analysis (e.g. if you are comparing averages across columns) - so it is important to be aware of them in a dataset so that you can address them (either by filling the empty cells with a value, or dropping the row that contains the empty cell).

```
### check for missing values

for col in data.columns:
    print(col, data[col].isnull().any())
```

We can use **data[col].isnull().any()** to check for the presence of any null values. We can combine this with a for loop to iteratively check each column in the dataframe.


## Dropping Duplicate Values 

Raw datasets may also contain duplicate values in columns which we may not want when carrying out analysis. In this instance, let's drop any duplicate values in the 'ticker' column, whilst keeping the first instance of a ticker.

```
### drop duplicates/filtered duplicates

# check if duplicates in ticker column
data['ticker'].duplicated().any()


# drop duplicates in the ticker column, keeping first occurrence
data_no_duplicates = data.drop_duplicates(subset = 'ticker', keep = 'first')
``` 

Using **duplicated().any()** will check for any duplicate values in a dataframe and return True if that is the case. If you want your dataframe to only contain unique values, you can use **drop_duplicates** to remove any duplicate values. If you only want to remove duplicate values in specific columns, you can use the **subset** argument to specify the columns.

## Dropping Nulls

Raw datasets may also contain empty cells in columns. You can drop all rows containing empty cells using **dropna**().

```
### dropping nulls

columns = ['mer']

data = data.dropna(subset = columns)
```

In this case, we only want to drop nulls in the 'mer' column, so we have specified this in the **subset** argument.

You can also address null values or empty cells by using **fillna** which copies down the value from the cell above.

## Standardising Column Formats

Inconsistent data formatting within a dataset can cause issues when trying to perform analysis. We can use various Python techniques to address inconsistent formats.

### Removing Commas

In Python, columns containing numbers with commas are treated as strings, meaning we cannot perform calculations on these columns. In our dataset, this is the case for various columns such as 'fum',  'transacted_value', 'transacted_volume' and 'no_of_trades'.

```
# get rid of commas ','

for col in data.columns:
    try:
        data[col] = data[col].str.replace(',', '')
        print(f'Successfully transformed column {col}')
    except:
        pass
        print(f'Could not perform transformation in column {col}')

``` 

Here we have used **str.replace** to replace any occurrences of commas with an empty string. As there are multiple columns containing numbers with commas, we have used a for loop to iterate through the columns in the dataframe.

Using **str.replace** will return an error for columns that do not contain occurrences of commas, so we also include a **try..except..pass** construct in our for loop - if an error is returned then the for loop will move onto the next column.

### Removing Dashes

The 'inflow_outflow' column in our dataset also contains various cells with lots of whitespace and a dash ('-') symbol. This is problematic as Python does not recognise these as zero values.


```
# get rid of dash '-'

data['inflow_outflow'] = data['inflow_outflow'].str.strip().replace({'-': '0'})
```

We can combine **strip()** with **replace()** to remove the extra whitespace and replace the dash with a 0.

### Converting Columns to Float

After performing these transformations, the numbers in our dataset are still in string format. We can now convert these numbers into float format which will enable us to properly analyse the data in Python.

```
for col in data.columns:
    try:
        data[col] = data[col].astype(float)
        print(f'Successfully transformed column {col}')
    except:
        pass
        print(f'Could not perform transformation in column {col}')
```

Our raw dataset also contains columns with percentages. Python does not recognise these values as float format - we will need to remove the percentage signs and convert these values into decimals before being able to convert them into float format.


```
for col in data.columns:
    try:
        data[col] = data[col].str.rstrip('%').astype(float) / 100
        print(f'Successfully transformed column {col}')
    except:
        pass
        print(f'Could not perform transformation in column {col}')
```

## Summary Statistics

We can use the **describe** function on our dataframe in order to generate a table with summary statistics on numerical columns, such as min, mean, max, standard deviation and quartiles.

```
# describe function
summary_stats = data.describe()
```

## Normalisation

If a dataframe contains columns with data on different scales, it may be difficult to observe patterns across columns. We can use normalisation to transform our data into a common range.

```
# normalise the dataframe
scaler = MinMaxScaler()

# create copy of dataframe for normalising
data_norm = data.copy()

# iterate through columns, normalise values if possible
for col in data_norm.columns:
    try:
        data_norm[col] = scaler.fit_transform(data_norm[[col]])
        print(f'Successfully normalised column {col}')
    except:
        pass
        print(f'Could not normalise column {col}')
```

You can see in our normalised dataframe, the values in each column now range between 0 and 1.








