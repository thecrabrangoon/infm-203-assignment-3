'''
Assumptions:
    - When counting visits per page, we consider each visit a unique countable instance regardless of which user is visiting the page and if they have visited the page previously
'''

import pandas as pd
from tabulate import tabulate



def calculate_time_spent_per_user(dataframe):
    # Transformation: Calculate total time in seconds spent on the website per user
    # Sorts the data by UserID ascending alphabetically
    time_per_user = dataframe.groupby(['UserID'], sort=True)[['Duration']].sum().rename(columns={'Duration': 'Total Duration in Seconds'})

    print("Total Time Spent Per User:")
    print(tabulate(time_per_user, headers='keys', tablefmt='psql'))
    print("\n")

def find_most_visited_page(dataframe):
    # Transformation: Find the most visited page on the website
    # Sorts the data by the number of visits ascending, then displays only the most visited row
    most_visited_page = dataframe.groupby(['Page'])[['Duration']].count().sort_values(by='Duration', ascending=False).rename(columns={'Duration': 'Number of Visits'}).head(1)
    
    print("Most Visited Page:")
    print(tabulate(most_visited_page, headers='keys', tablefmt='psql'))
    print("\n")

def calculate_avg_time_per_page(dataframe):
    # Transformation: Calculate the average time in seconds spent on each page of the website
    # Sorts the data by the average time spent ascending
    time_per_page = dataframe.groupby(['Page'])[['Duration']].mean().sort_values(by='Duration').rename(columns={'Duration': 'Average Time in Seconds'})

    print("Average Time Spent Per Page:")
    print(tabulate(time_per_page, headers='keys', tablefmt='psql', floatfmt='.2f'))
    print("\n")

def spark_simulation(data):
    # Load input data into a DataFrame
    df = pd.DataFrame(data)

    # Calculate and output time spent per user
    report_time_spent_per_user(df)

    # Calculate and output the most visited page
    report_most_visited_page(df)

    # Calculate and output the average time spent visiting each page
    report_avg_time_per_page(df)

