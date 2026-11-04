# INFM-203 Assignment 3: Spark Python Simulation

## Overview

Simple Spark simulation using the pandas library to process data about users visiting a website.

## Getting started

The Spark simulation can be run via main.py, or through your own python file using the spark module.

Please make sure to install the pandas and tabulate libraries.

### Using main.py

main.py is set up to run the Spark simulation.

1. Open main.py, and edit the `data` dictionary to include your desired input data.
2. Install the necessary dependencies:
```
python -m venv venv
source ./venv/bin/activate
python -m pip install -r requirements.txt
```
3. Run `python main.py`

### Calling the spark module

If you'd like to call the spark module directly, you can import the spark_simulation() function and pass your input data yourself to the function.

