# DAT5501: Weekly Tasks

## Overview
This repository contains tasks completed over 10 weeks of DAT5501, covering topics such as data manipulation, visualisation, statistical analysis, and supervised machine learning. Each week includes the dataset used, the code implemented, and the results obtained.

---

## Week 1: Linear Fit and CI Integration
**Code Files:** `adils_function.py`, `test_suite.py`  
**Dataset:** Small synthetic sales dataset  

**Summary:**  
- Created a function `fitLINE` to plot monthly sales data and overlay a linear best-fit line.  
- Wrote a test suite to ensure that input arrays are valid `numpy` arrays.  
- Integrated CircleCI for continuous integration and automated testing. Logic working but not implemented properly. Looking to implement on next project.

---

## Week 2: Compound Interest and Calendar Generator
**Code Files:** `compound_interest.py`, `solution.py`  
**Dataset:** None  

**Summary:**  
- Implemented a compound interest function to calculate year-by-year growth and estimate doubling time using the Rule of 72.  
- Created a small calendar generator script that outputs a formatted month layout given start day and number of days.  

---

## Week 5: Financial Data Analysis and Date Calculations
**Code Files:** `asset_prices.py`, `duration_calendar.py`, `us_election.py`  
**Datasets:** `historical_data_GOOG.csv`, `US-2016-primary.csv`, `random_dates.csv`  

**Summary:**  
- Cleaned and transformed stock market data (GOOG) to numerical types for analysis.  
- Plotted stock prices over time and daily percentage changes; calculated standard deviation of returns.  
- Developed a date difference calculator and loaded CSV of dates to compute days elapsed since each date.  
- Illustrated US election data by plotting a histogram of vote fractions for a candidate.  

---

## Week 8: Sorting Performance Analysis
**Code File:** `dp_sorting.py`  
**Dataset:** `historical_data_GOOG2.csv`  

**Summary:**  
- Calculated daily stock price changes and measured time taken to sort top N changes for varying N.  
- Visualised algorithm performance as a function of data size using line plots (related to the concept of big O notation).

---

## Week 9: Polynomial Regression Forecasting
**Code Files:** `model_testing_act2.py`, `model_testing_act3.py`, `model_testing_act4.py`  
**Dataset:** `gdp-per-capita-maddison-project-database.csv`  

**Summary:**  
- Filtered UK GDP per capita data (1922–2012) and fitted polynomials of order 1–9.  
- Forecasted GDP for 2013–2022 and compared predictions with actual values.  
- Calculated χ² per degree of freedom and Bayesian Information Criterion (BIC) for model comparison.  
- Identified polynomial order 4 as best model; extracted parameter values, covariance matrix, and uncertainties.  

---

## Week 10: Supervised ML – Decision Tree
**Code File:** `ml_decision_tree.py`  
**Dataset:** `data.csv` (regarding student dropout and academic success, UCI ML Repository)  

**Summary:**   
- Implemented a `DecisionTreeClassifier` from `scikit-learn` with constraints on depth, leaf nodes, and minimum samples.  
- Trained the model on all features excluding `Target` and visualised the tree.  

---

## General Notes
- Libraries commonly used: `numpy`, `pandas`, `matplotlib`, `scikit-learn`.  
- Was great to emulate statistical concepts within real work specific scenarios.

