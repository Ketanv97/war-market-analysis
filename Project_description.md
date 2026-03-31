# War Impact on Stock Markets

## Disclaimer



This project is intended for educational and analytical purposes only. The findings presented are based on historical data analysis and demonstrate correlations between oil prices, stock market indices, and sector performance during the 2026 Middle East conflict.  



Important: 

- The analysis shows trends and correlations, **not causation**.  

- Stock market movements are influenced by multiple factors, including global economic conditions, investor sentiment, currency fluctuations, and sector-specific events.  

- This project **does not constitute financial advice**, and users should not make investment decisions solely based on these results.



## Project Overview

This project analyzes how the ongoing Middle East conflict in 2026 impacts global and Indian stock markets, oil prices, and specific sectors. The goal is to explore how geopolitical events affect financial markets and identify which industries are most sensitive to these shocks.



## Key Objectives

- Examine the relationship between oil prices and stock market indices (Nifty 50, S&P 500).  

- Identify sector-wise winners and losers during the conflict.  

- Measure market volatility and daily returns during the war period.  

- Provide business insights for investors and analysts.



## Tools & Libraries Used

Python – Main programming language  

Pandas – Data manipulation  

NumPy – Numerical computations  

Matplotlib & Seaborn – Data visualization  

yfinance – Download historical stock and commodity data  



## Data Sources

  - Yahoo Finance via `yfinance` library:  

  - Crude Oil (CL=F)  

  - Nifty 50 (^NSEI)  

  - S&P 500 (^GSPC)  

  - Sector stocks: Reliance (RELIANCE.NS), Indigo (INDIGO.NS), ITC (ITC.NS)



## Project Steps

1. Data Collection: Downloaded historical prices for oil, stock indices, and sector stocks.  

2. Data Cleaning: Forward-filled missing values and removed remaining nulls.  

3. Exploratory Data Analysis (EDA):  

   - Plotted normalized stock and oil prices to visualize trends  

   - Calculated correlation between oil prices and stock indices  

   - Computed daily returns and volatility  

4. Focused Analysis: Zoomed into the war period (Jan 2026 onward) to highlight market impact.  

5. Sector Analysis: Compared sectoral performance to identify winners and losers.  



## Key Insights

- Oil prices surged sharply during the conflict → significant market decline.  

- Indian and global stock markets showed strong negative correlation with oil prices.  

- Worst-hit sectors: Aviation, FMCG, Logistics.  

- Beneficiaries: Oil & Gas companies, Defense.  

- Market volatility increased significantly during the war period.  

- Indicates potential stagflation risk (high inflation + low growth).