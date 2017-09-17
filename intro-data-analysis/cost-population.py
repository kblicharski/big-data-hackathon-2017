import pandas as pd
import numpy as np

data = pd.read_csv(
    "Data/Inpatient_Prospective_Payment_System__IPPS__Provider_Summary_for_the_Top_100_Diagnosis-Related_Groups__DRG__-_FY2011.csv")
df = pd.DataFrame(data)

df2 = df.loc[:, ['Provider State', 'DRG Definition', ' Average Total Payments ', ' Average Covered Charges ', 'Average Medicare Payments']]


def readfile(file: str) -> list:
    with open(file) as f:
        contents = f.readlines()
        output_eh = [item.strip() for item in contents]
        output_list = [item.replace(",","") for item in output_eh]
    return output_list

state_content = readfile('Data/state.txt')


def count_occurrences(items: list) -> dict:
    occurrences = {}
    for item in items:
        if item in occurrences:  # if the key exists
            occurrences[item] += 1
        else:  # if we have to add a new key
            occurrences[item] = 1
    return occurrences

state_content = readfile('Data/state.txt')
pop_content = readfile('Data/state_population.txt')

state_pop = dict(zip(state_content, pop_content))
#state_pop = [list(a) for a in zip(state_content, pop_content)]

operations = df2['DRG Definition']
operation_occurrences = count_occurrences(operations)
sorted_operations = sorted(operation_occurrences.items(), key=lambda x: x[1])

drg_defs = df2['DRG Definition']
avg_costs = df2[' Average Total Payments ']

state_op_cost = {}
for state in state_content:
    state_op_cost[state] = {}
    pop = state_pop[state]

    for index, operation in drg_defs.items():
        if operation in state_op_cost[state].values():
            cost_inter = avg_costs[index].replace(",","")
            cost_end = cost_inter[1:]
            state_op_cost[state][operation] += cost_end/pop
        else:
            cost_inter = avg_costs[index].replace(",", "")
            cost_end = cost_inter[1:]
            state_op_cost[state][operation] = float(cost_end) / float(pop)

