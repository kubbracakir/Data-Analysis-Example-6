import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("/Users/mac/Desktop/Python/src/datascience/gold.csv")

# Descriptive statistics
print(df.describe())

# Trim float numbers
df = df.round(2)
df.dtypes
# Change time column to Datetime format
df['time'] = pd.to_datetime(df['time'])
df2023 = df[df['time'].dt.year==2023]

# Time series plot of closing price for year 2023
plt.plot(df2023["time"], df2023["close"])
plt.xlabel("Time")
plt.ylabel("Closing Price")
plt.title("Gold Price Time Series (year 2023)")
plt.show()

plt.hist(df2023["close"])
plt.xlabel("Closing Price")
plt.ylabel("Frequency")
plt.title("Distribution of Closing Prices")
plt.show()

# Correlation matrix
correlation = df2023.corr()
print(correlation)