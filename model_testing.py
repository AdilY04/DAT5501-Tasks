"""
Activity 2:
Sab-sample all but the past 10 years of your data
Fit your sub-sample with polynomials from order 1 (a line) to 9
Forecast each polynomial 10 years into the future
How do they compare with reality?

Activity 3:
For each polynomial, calculate the x2 per degree of freedom and the BIC
→ Plot the x2 per degree of freedom and the BIC as a function of the polynomial order
How does the BIC compare to the x2 per degree of freedom?
Which model is the best?
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

#cleaning the data - it has all different countries, i just want gdp of uk from 1922-2012 according to above instruction
df = pd.read_csv('gdp-per-capita-maddison-project-database.csv', sep=',')
df_uk = df[df['Entity'] == "United Kingdom"]
filtered_df = df_uk[(df_uk['Year']>=1922)&(df_uk['Year']<=2012)]

x = filtered_df['Year'].values
y = filtered_df['GDP per capita'].values

all_coeffs = {}
all_fits = {}
for i in range(1,10):
    coeffs = np.polyfit(x,y,i)
    p = np.poly1d(coeffs)
    all_coeffs[i] = coeffs
    all_fits[i] = p