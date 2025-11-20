'''
Plot a histogram of the fraction of votes for a particular candidate in each state
Extra: Compare vote fraction for two candidates
'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('Week_5/US-2016-primary.csv', sep=';')
#print(df.head(3))

#check trump's fraction in every state so need to filter trump out
candidate_df = df[df['candidate'] == 'Donald Trump']
candidate_df['votes_percentage'] = df['fraction_votes']*100
#print(candidate_df.head(3))
plt.hist(candidate_df['votes_percentage'], bins=100)
plt.xlabel("Vote percentage")
plt.ylabel("Number of states")
plt.title("Vote distribution for Donald Trump")
plt.show()