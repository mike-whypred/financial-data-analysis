# DataFrames

## What are they
A DataFrame is a two-dimensional, size-mutable, and potentially heterogeneous tabular data structure with labeled axes (rows and columns). Think of it as a table in a database or an Excel spreadsheet. DataFrames are a key data structure in the pandas library, which is widely used for data manipulation and analysis in Python.

In this lesson we will use [cleaned ETF datasets](https://raw.githubusercontent.com/mike-whypred/financial-data-analysis/main/data/asx_etp_202401_small.csv) as our input.

To load the data we can utilize `read_csv` from `pandas` library. We will print top 5 rows using `head` function.

```py
import pandas as pd

df = pd.read_csv("asx_etp_202401_clean.csv")
df.head(5)

```
![top 5 sceenshot](../Financial%20Data%20Analysis/asset/Dataframes/top5.png)

## Selecting and Filtering
Selecting and filtering data in a DataFrame allows you to access specific rows and columns based on conditions.

```python
import pandas as pd

# Load data from a CSV file
df = pd.read_csv("asx_etp_202401_clean.csv")

# Select a single column
df['ticker']

# Filter based on a condition
df[df['sector'] == 'Equity - Australia']

# Filter using query
min_fum = 4000
df.query('sector == "Equity - Australia" and fum > @min_fum')

# To select rows, we can use loc, iloc, and slice

df.loc[0]
df.iloc[0]
df[0:5]

```
## Slicing and Indexing
Slicing and indexing help you access specific parts of the DataFrame using row and column indices.

```py
# Select rows by index
df.iloc[0:5]  # First 5 rows

# Select rows and columns by index
df.iloc[0:5, 0:3]  # First 5 rows and first 3 columns

# Select rows and columns by labels
df.loc[0:5, ['ticker', 'sector']]
```

## Sorting

Sorting allows you to arrange the data in a DataFrame based on the values in one or more columns.

```python
# Sort by a single column
df_sorted = df.sort_values(by='fum', ascending=False)

# Sort by multiple columns
df_sorted = df.sort_values(by=['sector', 'fum'], ascending=[True, False])
```

## Rename Columns
Renaming columns helps you change the column names to more meaningful or standardized names.

```py
# Rename columns
df_renamed = df.rename(columns={'fum': 'Funds Under Management', 'mer': 'Management Expense Ratio'})
```

## Reset Index
Resetting the index reassigns the row labels to a default integer index, which can be useful after filtering or sorting.

```py
# Reset index
df_reset = df.reset_index(drop=True)
```

## Copying
Copying a DataFrame creates a new DataFrame object with the same data, which can be useful to avoid modifying the original data.

```py
# Copy DataFrame
df_copy = df.copy()
```

This documentation provides a basic overview of DataFrames and common operations you can perform on them using the pandas library in Python. The examples use a sample dataset similar to the one provided in the attached file, which contains financial data of various ETFs (Exchange-Traded Funds)