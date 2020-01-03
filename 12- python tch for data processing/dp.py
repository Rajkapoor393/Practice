# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 19:13:43 2020

@author: Raj
"""

import pandas as pd
import numpy as np
import matplotlib as plt
# %matplotlib inline

# Reading the dataset in a dataframe using pandas
#df = pd.read_csv("C:\Users\Raj\Downloads\loan prediction\train_ctrUa4K.csv")
df = pd.read_csv("train_ctrUa4K.csv", index_col="Loan_ID")



'''
12 Useful Pandas Techniques in Python for Data Manipulation
'''

data = pd.read_csv("train_ctrUa4K.csv", index_col="Loan_ID")

#1 – Boolean Indexing

#What do you do, if you want to filter values of a column based on conditions
# from another set of columns? For instance, we want a list of all females who
# are not graduate and got a loan. Boolean indexing can help here:
    
df.loc[(df["Gender"]=="Female") & (df["Education"]=="Not Graduate")
 & (df["Loan_Status"]=="Y"), ["Gender","Education","Loan_Status"]]


data.loc[(data["Gender"]=="Female") & (data["Education"]=="Not Graduate")
 & (data["Loan_Status"]=="Y"), ["Gender","Education","Loan_Status"]]

#2 – Apply Function
'''
It is one of the commonly used functions for playing with data and creating new variables.
Apply returns some value after passing each row/column of a data frame with some function.
The function can be both default or user-defined. For instance, here it can be used to find
 the #missing values in each row and column.
'''
#Create a new function:
def num_missing(x):
  return sum(x.isnull())

#Applying per column:
print( "Missing values per column:")
print (data.apply(num_missing, axis=0)) #axis=0 defines that function is to be applied on each column

#Applying per row:
print ("\nMissing values per row:")
print (data.apply(num_missing, axis=1).head()) #axis=1 defines that function is to be applied on each row



