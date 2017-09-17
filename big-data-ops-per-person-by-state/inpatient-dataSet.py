import pandas as pd
import numpy as np
from operator import truediv
import matplotlib.pyplot as plt

data = pd.read_csv(
    "Data/Inpatient_Prospective_Payment_System__IPPS__Provider_Summary_for_the_Top_100_Diagnosis-Related_Groups__DRG__-_FY2011.csv")
df = pd.DataFrame(data)


def readfile(file: str) -> list:
    with open(file) as f:
        contents = f.readlines()
        output_eh = [item.strip() for item in contents]
        output_list = [item.replace(",", "") for item in output_eh]
    return output_list


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


df2 = df.loc[:, ['Provider State', 'DRG Definition', 'Provider Zip Code', ' Average Total Payments ']]

state_content = readfile('Data/state.txt')
pop_content = readfile('Data/state_population.txt')

# Change pop_content into a list of integers


state_pop_dict = zip(state_content, pop_content)

states = df['Provider State']
state_occurrences = count_occurrences(states)
sorted_states = sorted(state_occurrences.items(), key=lambda x: x[1])

operations = df['DRG Definition']
operation_occurrences = count_occurrences(operations)
sorted_operations = sorted(operation_occurrences.items(), key=lambda x: x[1])

print(df2.values)
state_and_operation_data = df2.groupby(['Provider State', 'DRG Definition']).size().reset_index().rename(
    columns={0: 'count'})

# print(state_and_operation_data)


total_operations_per_state = df2.groupby(['Provider State']).size().reset_index().rename(
    columns={0: 'count'})
print(total_operations_per_state)
ops_per_state = total_operations_per_state['count']

pop = np.array(pop_content, dtype=np.float)
ops = np.array(ops_per_state, dtype=np.float)
ops_per_person = ops / pop

state_ops_person_dict = zip(state_content, ops_per_person)

for item in state_ops_person_dict:
    print(item)
# for item in ops_list:
#     print(item)
