import pandas as pd 
import numpy as np
import yfinance as yf 
import matplotlib.pyplot as plt 
import seaborn as sns

print("setup complete")

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

tickers = {
    "Oil": "CL=F",
    "Nifty": "^NSEI",
    "SP500": "^GSPC"
}

# Download data
data = yf.download(list(tickers.values()), start="2024-01-01")
print(data)

# Keep closing prices
data = data["Close"]

# Rename columns
data.columns = tickers.keys()

print(data.head())

# Clean data
data = data.ffill() 
data = data.dropna()

print("\nCleaned Data:")
print(data.head())

# Normalize data
normalized = data / data.iloc[0] * 100
print(normalized.head())

'''# Plot
plt.figure(figsize=(10,5))
plt.plot(normalized)
plt.title("Oil vs Stock Market")
plt.legend(normalized.columns)
plt.show()'''

'''#Heat map correlation
correlation = data.corr()
print("\nCorrelation:\n", correlation)
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()'''

'''# Returns (Market Movement)
returns = data.pct_change().dropna()
print(returns.head())
returns.plot(figsize=(10,5), title="Daily Returns")
plt.show()'''

'''#Focus on War Period
recent = data.loc["2026-01-01":]
recent_norm = recent / recent.iloc[0] * 100
recent_norm.plot(figsize=(10,5), title="War Period Impact")
plt.show()'''

# Sector Analysis

sector_tickers = {
    "Reliance": "RELIANCE.NS",
    "Indigo": "INDIGO.NS",
    "ITC": "ITC.NS"
}

sector_data = yf.download(list(sector_tickers.values()), start="2025-01-01")["Close"]
sector_data.columns = sector_tickers.keys()
sector_norm = sector_data / sector_data.iloc[0] * 100
sector_norm.plot(figsize=(10,5), title="Sector Performance")
plt.show()

