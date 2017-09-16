import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
style.use('ggplot')


# How to create a DataFrame?
web_stats = {'Day': [1, 2, 3, 4, 5, 6],
             'Visitors': [43, 53, 34, 45, 64, 34],
             'Bounce_Rate': [65, 72, 62, 64, 54, 66]}
df = pd.DataFrame(web_stats)

# How to visualize the data?
'''
print(df)
print(df.head())
print(df.tail())
print(df.tail(2))
'''

# How do we set the index?
# new_df = df.set_index('Day')
# print(new_df)
df.set_index('Day', inplace=True)

# How do we access a column?
# print(df['Visitors'])

# How do we access multiple columns?
print(df[['Bounce_Rate', 'Visitors']])

# How do we turn a column of values into a list?
print(df['Visitors'].tolist())

# What about multiple columns (a 2d array)?
print(np.array(df[['Bounce_Rate', 'Visitors']]))

df2 = pd.DataFrame(np.array(df[['Bounce_Rate', 'Visitors']]))
print(df2)

