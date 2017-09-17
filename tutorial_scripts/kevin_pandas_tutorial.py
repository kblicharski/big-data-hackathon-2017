import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Source
# https://pandas.pydata.org/pandas-docs/stable/10min.html

####################
# Creating Objects #
####################
# Series Objects
# Create by passing a list of values
s = pd.Series([1,3,5,np.nan,6,8])
# print(s)

# DataFrame Objects
# Some sample data
dates = pd.date_range('20130101', periods=6)
# print(dates)

# Create by passing a numpy array with labeled columns
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
print(df)

# Create by passing a dict of objects
df2 = pd.DataFrame({
    'A': 1., 
    'B': pd.Timestamp('20130102'),
    'C': pd.Series(1,index=list(range(4)),dtype='float32'),
    'D': np.array([3] * 4,dtype='int32'),
    'E': pd.Categorical(["test","train","test","train"]),
    'F': 'foo'
})
# print(df2)
# print(df2.dtypes)

################
# Viewing Data #
################
# Top rows of the frame
# print(df.head())

# bottom rows of the frame
# print(df.tail(3))

# print(df.index)

# print(df.columns)

# print(df.values)

# Statistic summary of the data
# print(df.describe())

# Transpose
# print(df.T)

# Sort by axis
# print(df.sort_index(axis=1, ascending=False))

# Sort by values
# print(df.sort_values(by='B'))

###########
# Getting #
###########

# A single column
# print(df['A'])

# Multiple
# print(df[0:3])

# Cross-section by label
# print(df.loc[dates[0]])

# Selection on multiple axes
# Slicing columns
# print(df.loc[:, ['A', 'B']])

# Also slicing rows
# Endpoints are included!
# print(df.loc['20130102':'20130104', ['A', 'B']])

# Dimension reduction
a = '20130102'
print(df.loc[:, ['A', 'B']])

# Scalar values
# print(df.loc[dates[0], 'A'])
# For faster scalar access
# print(df)
# print(df.at[dates[0], 'A'])

# Selection by position
# Will select the values in row 3
# print(df.iloc[3])

# Integer slices
# Will select the values in rows 4 and 5 and cols 1 and 2
# print(df.iloc[3:5, 0:2])



