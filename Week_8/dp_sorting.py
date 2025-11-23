import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import time 

df = pd.read_csv('Week_8/historical_data_GOOG2.csv')

df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')
df['Close/Last'] = df['Close/Last'].str.replace('$','').astype(float)
df['Open'] = df['Open'].str.replace('$','').astype(float)
df['High'] = df['High'].str.replace('$','').astype(float)
df['Low'] = df['Low'].str.replace('$','').astype(float)

df['Daily Change'] = df['Close/Last'].diff()



algo_times = []
our_i = []

for i in range(7,366):
    start = time.time()
    sortdf = df.sort_values(by='Daily Change', ascending=False).head(i)
    end = time.time()
    time_taken = end - start
    algo_times.append(time_taken)
    our_i.append(i)

plt.plot(our_i, algo_times)
plt.xlabel("N")
plt.ylabel("Time taken (s)")
plt.title("Respective n vs time taken")
plt.show()