"""spark module -- Spark simulation using pandas library.

Implements a simple simulation of Spark data processing for user data of a website. Each data entry has a unique User ID, the page the user visited, and how long in seconds they spent on the page.

Functions:
spark_simulation() -- public function, runs spark simulation by performing calculations and outputting to console
_report_time_spent_per_user() -- Calculate and output time spent per user on the website.
_report_most_visited_page() -- Calculate and output the most visited page on the website.
_report_avg_time_per_page() -- Calculate and output the average time in seconds each page of the website was visited.
"""

import pandas as pd
from tabulate import tabulate



def _report_time_spent_per_user(dataframe):
    """Calculate and output time spent per user on the website.

    Transforms data via groupby() operation.

    Arguments:
    dataframe -- required, pandas DataFrame object containing user, page, and duration data.

    Output:
    ASCII table format of time spent per user in seconds, sorted in ascending order by UserID.
    """
    time_per_user = dataframe.groupby(['UserID'], sort=True)[['Duration']].sum().rename(columns={'Duration': 'Total Duration in Seconds'})

    print("Total Time Spent Per User:")
    print(tabulate(time_per_user, headers='keys', tablefmt='psql'))
    print("\n")

def _report_most_visited_page(dataframe):
    """Calculate and output the most visited page on the website.

    Transforms data via groupby() operation. Counts the visits per page, sorts descending by number of visits, then displays only the top row (which has the highest number of visits).

    Arguments:
    dataframe -- required, pandas DataFrame object containing user, page, and duration data.

    Output:
    ASCII table format of the website page with the highest number of visits.
    """
    most_visited_page = dataframe.groupby(['Page'])[['Duration']].count().sort_values(by='Duration', ascending=False).rename(columns={'Duration': 'Number of Visits'}).head(1)
    
    print("Most Visited Page:")
    print(tabulate(most_visited_page, headers='keys', tablefmt='psql'))
    print("\n")

def _report_avg_time_per_page(dataframe):
    """Calculate and output the average time in seconds each page of the website was visited.

    Transforms data via groupby() operation. Calculates the mean of the duration data to find the average, then sorts the rows by average time spent ascending.

    Arguments:
    dataframe -- required, pandas DataFrame object containing user, page, and duration data.

    Output:
    ASCII table format of the average time spent visiting per page in seconds. Truncates the value to 2 decimal places.
    """
    # Transformation: Calculate the average time in seconds spent on each page of the website
    # Sorts the data by the average time spent ascending
    time_per_page = dataframe.groupby(['Page'])[['Duration']].mean().sort_values(by='Duration').rename(columns={'Duration': 'Average Time in Seconds'})

    print("Average Time Spent Per Page:")
    print(tabulate(time_per_page, headers='keys', tablefmt='psql', floatfmt='.2f'))
    print("\n")

def spark_simulation(data):
    """Spark simluation for user visits.

    Arguments:
    data -- required, input data in form of dictionary, with keys of UserID, Page, and Duration, all mapped to lists of data entries
    """
    # Load input data into a DataFrame
    df = pd.DataFrame(data)

    _report_time_spent_per_user(df)

    _report_most_visited_page(df)

    _report_avg_time_per_page(df)



