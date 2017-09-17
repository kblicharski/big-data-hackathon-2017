import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv(
    "Data/Inpatient_Prospective_Payment_System__IPPS__Provider_Summary_for_the_Top_100_Diagnosis-Related_Groups__DRG__-_FY2011.csv")
df = pd.DataFrame(data)


def readfile(file: str) -> list:
    with open(file) as f:
        contents = f.readlines()
        output_list = [item.strip() for item in contents]
    return output_list


state_content = readfile('Data/state.txt')
pop_content = readfile('Data/state_population.txt')

state_pop_dict = zip(state_content, pop_content)

for item in state_pop_dict:
    print(item)


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


states = df['Provider State']
state_occurrences = count_occurrences(states)
sorted_states = sorted(state_occurrences.items(), key=lambda x: x[1])

operations = df['DRG Definition']
operation_occurrences = count_occurrences(operations)
sorted_operations = sorted(operation_occurrences.items(), key=lambda x: x[1])


