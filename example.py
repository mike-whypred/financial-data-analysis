import pandas as pd

# Create a sample DataFrame
data = {
    'Date': pd.date_range(start='2023-01-01', periods=10, freq='D'),
    'Stock_A': [150, 152, 153, 149, 148, 151, 150, 152, 154, 156],
    'Stock_B': [100, 102, 103, 101, 99, 98, 97, 99, 100, 102]
}
df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Calculate daily returns for each stock
df['Return_A'] = df['Stock_A'].pct_change()
df['Return_B'] = df['Stock_B'].pct_change()

# Calculate the mean return for each stock
mean_return_a = df['Return_A'].mean()
mean_return_b = df['Return_B'].mean()

# Display the DataFrame with daily returns
print("\nDataFrame with Daily Returns:")
print(df)

# Display the mean returns
print("\nMean Return for Stock_A:", mean_return_a)
print("Mean Return for Stock_B:", mean_return_b)

# Filter the DataFrame for days where both stocks had positive returns
positive_returns_df = df[(df['Return_A'] > 0) & (df['Return_B'] > 0)]

# Display the filtered DataFrame
print("\nDays with Positive Returns for Both Stocks:")
print(positive_returns_df)
