import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import operator

def count_occurrences(items: list) -> dict:
    occurrences = {}
    for item in items:
        if item in occurrences:  # if the key exists
            occurrences[item] += 1
        else:  # if we have to add a new key
            occurrences[item] = 1
    return occurrences

def print_occurrences(occurrences: dict) -> None:
    for k, v in occurrences.items():
        print('{}: {}'.format(k, v))


data=pd.read_csv('Inpatient_Prospective_Payment_System.csv')
df = pd.DataFrame(data)

# avg_covered_charges = df['Average Covered Charges']
# avg_covered_charges_mean = avg_covered_charges.mean()

# count the number of procedures per state
states = df['Provider State']
state_occurrences = count_occurrences(states)
sorted(state_occurrences.items(), key=lambda x:x[1]) # sort in ascending order
# print_occurrences(state_occurrences)

# count the number of procedures
operations = df['DRG Definition']
operation_occurrences = count_occurrences(operations)
sorted(operation_occurrences.items(),key=lambda x:x[1])
operation_series = pd.Series(operation_occurrences)
print(operation_series)

# #calculate the average covered charges / state

state_series = pd.Series(state_occurrences)
# print(series) # a series is a smart list
max_occurrences = max(state_occurrences.items(),key=operator.itemgetter(1))[0]
# print(max_occurrences) # California has most operations

# dataframe is like a matrix a dict of series
operations_greater_than_1500 = []
operations_greater_than_1500 = operation_series.values > 1500
print(operations_greater_than_1500)