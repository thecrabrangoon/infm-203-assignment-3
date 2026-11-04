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
