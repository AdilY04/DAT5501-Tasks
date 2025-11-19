"""
Coding activity: asset prices
- Clean dataset as necessary
- Plot closing price vs. date
- Extra: calculate daily percentage change, plot vs. date
- Extra extra: calculate standard deviation of percent daily changes
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt

df = pd.read_csv('historical_data_GOOG.csv')
#print(df.head())
#we see from the head that we will need to sort the formatting - will need to utilise datetime format + remove any $ signs + ensure float
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')
df['Close/Last'] = df['Close/Last'].str.replace('$','').astype(float)
df['Open'] = df['Open'].str.replace('$','').astype(float)
df['High'] = df['High'].str.replace('$','').astype(float)
df['Low'] = df['Low'].str.replace('$','').astype(float)

#data clean at this point

plt.plot(df['Date'], df['Close/Last'])
plt.show()

#need to do the extra stuff