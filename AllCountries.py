# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 12:03:45 2019

@author: Raj
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset = pd.read_csv('AllCountries.csv')

#print(dataset)
print(dataset.head(5))
print(dataset.describe())

#print countries name with size >2000(*1000)square km
selected_data = dataset.loc[:,['Country','LandArea']]
for i in selected_data.itertuples():
    if i[2]>2000:
        print(i)

#Scatter plot between GDP and BirthRate

selected_data1 = dataset.loc[:,['Country','GDP','BirthRate']]

x = np.array(selected_data1['GDP'])
y = np.array(selected_data1['BirthRate'])

plt.scatter(x,y)
plt.xlim(0,2000)
plt.xlabel('GDP')
plt.ylabel('BirthRate')
plt.show()

#sorted country based on gdp

selected_data2 = dataset.loc[:,['Country','GDP']]

sorted_data = selected_data2.sort_index(by='GDP', ascending ='Fales')

selected_sorted_data = sorted_data.iloc[:10]

plt.pie(selected_sorted_data['GDP'], labels=selected_sorted_data['Country'])
plt.show()

