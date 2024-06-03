# What are they

A DataFrame is a powerful data structure commonly used in data analysis and manipulation, especially within the Python programming language. It is part of the pandas library, which is widely used in the data science community.

## Key Characteristics of a DataFrame:

 - Tabular Structure: A DataFrame is similar to a table in a database or an Excel spreadsheet. It consists of rows and columns, where each column can contain data of different types (integers, floats, strings, etc.).
 - Labeled Axes: DataFrames have labeled axes (rows and columns), which makes it easy to refer to specific data points using labels. The row labels are known as the index, and the column labels are simply referred to as columns.
 - Data Alignment: DataFrames automatically align data based on the labels in the axes. This makes operations like addition and subtraction straightforward and intuitive.
 - Flexible Data Manipulation: You can easily perform a variety of data manipulations on DataFrames, including filtering, aggregation, reshaping, and merging. Pandas provides a wide array of methods for handling these tasks efficiently.

![data frame sceenshot](../Financial%20Data%20Analysis/asset/Dataframes/1.png)

We can leverage function from `pandas` package `read_csv` and print top 5 rows by using `head` function.

```
import pandas as pd

df = pd.read_csv("asx_etp_202401.csv")
df.head(5)

```
![top 5 sceenshot](../Financial%20Data%20Analysis/asset/Dataframes/top5.png)

We can leverage function from `pandas` package `read_csv` and print top 5 rows by using `head` function.

```
import pandas as pd

df = pd.read_csv("asx_etp_202401.csv")
df.head(5)

```

![top 5 sceenshot](../Financial%20Data%20Analysis/asset/Dataframes/top5.png)

## Data types in dataframe

In order for us to be aware of the types of data that we are handling, we could use function `dtypes`

```
df.dtypes
```

In pandas, the object data type is a general-purpose data type that can hold any kind of Python object. This is the most flexible data type in pandas, but it comes with some trade-offs in terms of performance and memory usage compared to more specific data types like int64, float64, or bool.

To continue to the next section, we want to make sure that we are working with the right data type to ensure smooth dataframe operation. 

```
df['fum'] = df['fum'].str.replace(',', '')
df['fum'] = pd.to_numeric(df['fum'], errors = 'coerce')

```

## Selecting and filterings

There are many ways to select and filter dataframe. 

### Selecting columns

Let's start with selecting a subset of data that we want from the dataframe. From the dataset, let's grab the top 5 ticker. Further, we can also access multiple columns by passing a list. Let's grab top 5 tickers and their respective name

```
df['ticker'].head(5)
df[['ticker','name']].head(5)
```
### Selecting rows

To select rows, we can use loc, iloc, and slice

```
df.loc[0]
df.iloc[0]
df[0:5]
```

### Filtering

We will discuss the three most common ways filter dataframes.

1. Query

Similar to syntax in SQL or function FILTER in Excel, we can use `query` function from `pandas`. 

Let's do two different examples. First example, we will sector to only include "Equity - Australia".
Second, we will filter the result to have FUM more than 4b.

```
df.query('sector == "Equity - Australia"')

min_fum = 4000
df.query('sector == "Equity - Australia" and fum > @min_fum')
```

2. Dataframe way

3. loc function

There are many ways to select and filter dataframe. We will discuss the three most common ways to select and filter dataframe

Slicing/indexing

Sorting

Rename columns

Reset index

Copying