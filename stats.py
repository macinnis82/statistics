# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 08:48:11 2015

@author: Administrator
"""

import pandas as pd
from scipy import stats

data = '''Region,Alcohol,Tobacco
North,6.47,4.03
Yorkshire,6.13,3.76
Northeast,6.19,3.77
East Midlands,4.89,3.34
West Midlands,5.63,3.47
East Anglia,4.52,2.92
Southeast,5.89,3.20
Southwest,4.79,2.71
Wales,5.27,3.53
Scotland,6.08,4.51
Northern Ireland,4.02,4.56'''

data = data.splitlines()

data = [i.split(',') for i in data]

column_names = data[0]
data_rows = data[1::]
df = pd.DataFrame(data_rows, columns=column_names)

 # Convert the columns to floats
df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

 # Calc Mean, Median and Mode for Alcohol & Tobacco
a_mean = df['Alcohol'].mean()
t_mean = df['Tobacco'].mean()

a_median = df['Alcohol'].median()
t_median = df['Tobacco'].median()

a_mode = stats.mode(df['Alcohol'])
t_mode = stats.mode(df['Tobacco'])
 
print "The mean of Alcohol and Tobacco are %.2f, %.2f" % (a_mean, t_mean)
print "The median of Alcohol and Tobacco are %.2f, %.2f" % (a_median, t_median)
print "The mode of Alcohol and Tobacco are %.2f, %.2f" % (float(a_mode[0]), float(t_mode[0]))

 # Calc the Range, Variance and Standard Deviation for Alcohol & Tobacco
a_range = max(df['Alcohol']) - min(df['Alcohol'])
t_range = max(df['Tobacco']) - min(df['Tobacco'])

a_variance = df['Alcohol'].var()
t_variance = df['Tobacco'].var()

a_std = df['Alcohol'].std()
t_std = df['Tobacco'].std()

print "The range of Alcohol and Tobacco are %.2f, %.2f" % (a_range, t_range)
print "The variance of Alcohol and Tobacco are %.2f, %.2f" % (a_variance, t_variance)
print "The standard deviation of Alcohol and Tobacco are %.2f, %.2f" % (a_std, t_std)