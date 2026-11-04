"""main module

Call main() to run Spark simluation implemented in spark module.

Input data is stored in dictionary data, with the following keys:
    UserID -- list of unique User IDs
    Page -- list of strings with names of website page user visited
    Duration -- list of ints, number of seconds user visited a given page

Data in the data dictionary is collated by the same index in the lists stored at each key. For example, the first data entry is found at data['UserID'][0], data['Page'][0], data['Duration'][0]
"""

from spark import spark_simulation

data = {
    'UserID': ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'C'],
    'Page': ['Home', 'About', 'Home', 'Contact', 'Home', 'About', 'Home', 'About'],
    'Duration': [30, 40, 25, 35, 20, 15, 50, 45]
}

def main():
    spark_simulation(data)

if __name__ == "__main__":
    main()
