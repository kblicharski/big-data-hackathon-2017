import pandas as pd
import csv
import operator

data = pd.read_csv(
    "Data/Inpatient_Prospective_Payment_System__IPPS__Provider_Summary_for_the_Top_100_Diagnosis-Related_Groups__DRG__-_FY2011.csv")
df = pd.DataFrame(data)

df2 = df.loc[:, ['Provider State', 'DRG Definition', ' Average Total Payments ', ' Average Covered Charges ', 'Average Medicare Payments']]


def readfile(file: str) -> list:  # Read in file, strip, and return list of stripped lines
    with open(file) as f:
        contents = f.readlines()
        output_eh = [item.strip() for item in contents]
        output_list = [item.replace(",", "") for item in output_eh]
    return output_list

state_content = readfile('Data/state.txt')


def count_occurrences(items: list) -> dict:  # Count number of occurrences of an item in a list and put into dict
    occurrences = {}
    for item in items:
        if item in occurrences:  # if the key exists
            occurrences[item] += 1
        else:  # if we have to add a new key
            occurrences[item] = 1
    return occurrences


def convert_dicts_to_csv(dict_of_lists, filename):
    # Apparently don't need this but don't want to risk it yet
    # dictionary_of_dictionaries_formatted = json.dumps(dictionary_of_dictionaries, sort_keys=True, indent=4, separators=(',', '\t'))

    with open('Data/' + filename + '.csv', 'w') as csv_file:
        csvwriter = csv.writer(csv_file, delimiter='\t')
        csvwriter.writerow(["State,ExpensiveProcedure,MaxCost,CheapestProcedure,MinCost"])
        for individual_states in dict_of_lists:
            expensive_procedure = dict_of_lists[individual_states][0][0]
            val_expensive = dict_of_lists[individual_states][0][1]
            cheap_procedure = dict_of_lists[individual_states][1][0]
            val_cheap = dict_of_lists[individual_states][1][1]

            csvwriter.writerow([individual_states, ",", expensive_procedure, ",", val_expensive,",",cheap_procedure, ",", val_cheap])


# Find population of cases per state and put into dict
state_content = readfile('Data/state.txt')
pop_content = readfile('Data/state_population.txt')
state_pop = dict(zip(state_content, pop_content))

# Isolate procedures column and find number of procedures for each
operations = df2['DRG Definition']
operation_occurrences = count_occurrences(operations)
sorted_operations = sorted(operation_occurrences.items(), key=lambda x: x[1])

# Isolate Procedures/Average Payment/Medicare Payment for specific procedure columns (will use indexes)
drg_defs = df2['DRG Definition']
avg_costs = df2[' Average Total Payments ']
med_costs = df2['Average Medicare Payments']

# Create dict of dicts to store:
# {State: {Procedure: Avg Cost per person of state for this specific procedure}}
state_op_cost = {}
for state in state_content:
    state_op_cost[state] = {}
    pop = state_pop[state]

    # Strip commas and create sub dicts of {Procedure: AvgCostPerPersonInState}
    for index, operation in drg_defs.items():
        operation = operation.replace(",", "")

        cost_inter = avg_costs[index].replace(",", "")
        cost_end = cost_inter[1:]

        if operation in state_op_cost[state].values():
            state_op_cost[state][operation] += float(cost_end)/float(pop)
        else:
            state_op_cost[state][operation] = float(cost_end) / float(pop)

state_op_cost_med = {}
for state in state_content:
    state_op_cost_med[state] = {}
    pop = state_pop[state]

    for index, operation in drg_defs.items():
        operation = operation.replace(",", "")

        med_inter = med_costs[index].replace(",", "")
        med_end = med_inter[1:]

        if operation in state_op_cost_med[state].values():
            state_op_cost_med[state][operation] += float(med_end) / float(pop)
        else:
            state_op_cost_med[state][operation] = float(med_end) / float(pop)

maxmin_state_op_cost = {}
maxmin_state_op_cost_med = {}
for state in state_content:
    maxmin_state_op_cost[state] = [[], []]
    max_key = max(state_op_cost[state].items(), key=operator.itemgetter(1))[0]
    min_key = min(state_op_cost[state].items(), key=operator.itemgetter(1))[0]
    max_val = state_op_cost[state][max_key]
    maxmin_state_op_cost[state][0] = [max_key, state_op_cost[state][max_key]]
    maxmin_state_op_cost[state][1] = [min_key, state_op_cost[state][min_key]]

    maxmin_state_op_cost_med[state] = [[], []]
    max_med = max(state_op_cost_med[state].items(), key=operator.itemgetter(1))[0]
    min_med = min(state_op_cost_med[state].items(), key=operator.itemgetter(1))[0]
    maxmin_state_op_cost_med[state][0] = [max_med, state_op_cost_med[state][max_med]]
    maxmin_state_op_cost_med[state][1] = [min_med, state_op_cost_med[state][min_med]]

convert_dicts_to_csv(maxmin_state_op_cost, 'avg_total_cost_operation')
convert_dicts_to_csv(maxmin_state_op_cost_med, 'avg_Medicare_cost_operation')