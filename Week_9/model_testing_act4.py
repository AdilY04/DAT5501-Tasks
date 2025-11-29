"""
Activity 4:
For your best model, what are the parameter values and covariance matrix?
What are the uncertainties in your parameter values?
Can you find a better model, for example, exponential?

"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#cleaning the data - it has all different countries, i just want gdp of uk from 1922-2012 according to above instruction
df = pd.read_csv('Week_9/gdp-per-capita-maddison-project-database.csv', sep=',')
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

future_years = np.arange(2013,2023)
actual_future_values = df_uk['GDP per capita'][(df_uk['Year']>=2013)&(df_uk['Year']<=2022)].values

all_forecasts = {}
for i in range(1,10):
    p = all_fits[i]
    y_pred = p(future_years)
    all_forecasts[i] = y_pred

#just have to turn forecasted values into np array so they can be plotted together
forecast_arrays = np.array(list(all_forecasts.values()))

chi2_per_dof = {} 
bic = {}           
N_obs = len(future_years)

for degree in range(1, 10):
    y_pred = all_forecasts[degree] 
    residuals = (y_pred - actual_future_values) ** 2
    chi2 = np.sum(residuals)        
    
    N_params = degree + 1           # number of parameters in polynomial, did get some help from AI here onwards. Code can be explained.
    nu = N_obs - N_params           
    
    chi2_per_dof[degree] = chi2 / nu   
    
    bic[degree] = chi2 + N_params * np.log(N_obs)  

degrees = list(range(1, 10))

"""
plt.figure(figsize=(10,6))
plt.plot(degrees, [chi2_per_dof[d] for d in degrees], marker='o', label='Chi² / DoF')
plt.plot(degrees, [bic[d] for d in degrees], marker='s', label='BIC')
plt.xlabel('Polynomial Degree')
plt.ylabel('Metric Value')
plt.title('Model Comparison: χ²/DoF vs BIC')
plt.xticks(degrees)
plt.legend()
plt.grid(True)
plt.show()
"""

#polynomial 4 does look the best - low x2 and bic

#so we need to derive poly order 4 and get the parameter values and covariance matrix - then find uncertainties.

coffs, cov = np.polyfit(x,y, deg=4, cov=True)
print("Coefficients:", coeffs)
print("Covariance matrix:\n", cov)