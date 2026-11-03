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
'''

import pandas as pd

data = {
    'UserID': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'C'],
    'Page': ['Home', 'About', 'Home', 'Contact', 'Home', 'About', 'Home', 'About'],
    'Duration': [30, 40, 25, 35, 20, 15, 50, 45]
}

df = pd.DataFrame(data)

time_per_user = df.groupby(['UserID'])[['Duration']].sum()
time_per_page = df.groupby(['Page'])[['Duration']].sum()

print(time_per_user)
print(time_per_page)

