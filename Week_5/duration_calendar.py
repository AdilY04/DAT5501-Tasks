"""
Coding activity: duration calculator
Write a code to take a date input from the user and calculate how many days until today
Unit testing: build a test-suite to validate your calculation
Code extension: Load the dates from the random_dates.csv file on QM+
Write a function to calculate how many days in the past each date in the CSV
"""

import pandas as pd
from datetime import date, datetime
import os

def days_difference():
    today = date.today()
    user_input = input("Enter your desired date in format 'YYYY-MM-DD': ")
    user_date = datetime.strptime(user_input, '%Y-%m-%d').date() 
    print(today - user_date)

def days_list():
    today = date.today()
    dates_list = pd.read_csv('Week_5/random_dates.csv', header=None, dtype=str)
    for d in dates_list[0]:
        parsed_date = datetime.strptime(d, '%Y-%m-%d').date() #just for understanding, this is making each csv entry a date
        print(today - parsed_date)


days_list()
