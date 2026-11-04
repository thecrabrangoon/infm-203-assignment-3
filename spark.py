'''
input format:
    dictionary
    keys:
        user id - list of strings - unique ID for user
        page - list of strings - webpage the user visited
        duration - list of ints - time spent on page (in seconds)
    steps:
        load data into pandas dataframe
        calculate total time spent per user
        find most visited page using group-by operation
        compute average time spent per page
        output results based on format in assignment rubric

Assumptions:
    - When counting visits per page, we consider each visit a unique countable instance regardless of which user is visiting the page and if they have visited the page previously
'''

import pandas as pd
from tabulate import tabulate

data = {
    'UserID': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'C'],
    'Page': ['Home', 'About', 'Home', 'Contact', 'Home', 'About', 'Home', 'About'],
    'Duration': [30, 40, 25, 35, 20, 15, 50, 45]
}

df = pd.DataFrame(data)

time_per_user = df.groupby(['UserID'], sort=True)[['Duration']].sum().sort_values(by='UserID').rename(columns={'Duration': 'Total Duration in Seconds'})
grouped_per_page = df.groupby(['Page'])[['Duration']]
time_per_page = grouped_per_page.mean().sort_values(by='Duration').rename(columns={'Duration': 'Average Time in Seconds'})
most_visited_page = grouped_per_page.count().sort_values(by='Duration', ascending=False).rename(columns={'Duration': 'Number of Visits'}).head(1)

print("Total Time Spent Per User:")
print(tabulate(time_per_user, headers='keys', tablefmt='psql'))
print("\n")
print("Most Visited Page:")
print(tabulate(most_visited_page, headers='keys', tablefmt='psql'))
print("\n")
print("Average Time Spent Per Page:")
print(tabulate(time_per_page, headers='keys', tablefmt='psql', floatfmt='.2f'))



