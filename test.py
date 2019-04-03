# -*- coding: utf-8 -*-
"""

@author: Raj
"""

print("My name is raj kapoor gupta")

str = input("Enter your full name ")
print("My full name is ", str)


#private protected and public

class Challange():
    def __init__(self):
        self.__pri=("I am a private")
        self._pro=("I am a protected")
        self.pub=("I am a public")
        
ob= Challange()
print(ob.pub)
print(ob._pro)
#print(ob.__pri)

#random number 

import random

num = random.randrange(0,100,20)
print(num)

#numpy

import numpy as np

#a = np.array([[1,2,3],[4,5,6],[7,8,9]])
#a = np.arange(0,100)
a = np.linspace(0,100,20)
print(a)

#restructurnig of numpy array

a = np.zeros(8)
print(a)

a = a.reshape(2,4)
print(a)

#creating a data frame
import numpy
import pandas

listx = [{'a':2,'b':4},{'a':1,'b':3},{'a':6,'b':8}]

series1= pandas.Series([40,50,60], index =['math','physics','Chemistry'])
series2= pandas.Series([40,50,60], index =['math','physics','Chemistry'])

table = pandas.DataFrame({'ram':series1,'shyam':series2})
print(table)

#addition and deletion of nuw column in dataframe
series1= pandas.Series([40,50,60], index =['math','physics','Chemistry'])
series2= pandas.Series([40,50,60], index =['math','physics','Chemistry'])
series3= pandas.Series([40,50,60,75], index =['math','physics','Chemistry','nepali'])
series4= pandas.Series([40,50,60,85], index =['math','physics','Chemistry','English'])

table = pandas.DataFrame({'ram':series1,'shyam':series2,'hari':series3,'sita':series4})
#print(table)
ram_series= table.pop('ram')
print(ram_series)

#loading csv data into dataframes 

table.to_csv('pandas_data.csv')

#matplot

import matplotlib.pyplot as plt

plt.plot([1,2,10,5,20])
plt.show()

y_values = [10,20,30,40,50,60]

print([i**2 for i in y_values])

plt.plot([i**2 for i in y_values], y_values)
plt.show()


x = numpy.arange(5)
plt.plot(x,x, label= 'linear')
plt.plot(x,x*x, label= 'square')
plt.plot(x,x*x*x, label= 'cube')

plt.grid(True)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Polynomial Graph')
plt.legend()
plt.show()

