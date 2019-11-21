# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 22:29:59 2019

@author: Raj
"""
"""
Python set-2 variable, expression condition and functions

"""

#for increment and decreament operation

for i in range(0,5):
    print(i)
    

# Variable in python

a=4
A=5
print(a)
print(A)

# Expression in python

c= a*A
d= A+a
print(c)
print(d)

# Condition in python
x = 3
y = 9

if y%x == 0:
    print("y divisible by x")
elif y + 1 == 10:
    print ("Increment in y produces 10")
else:
    print("You are in else statement")
# Function in python

def checkDivisiblity(a,b):
    if b%a==0:
        print("y is divisible by x")
    else:
        print("y is not divisible by x")

checkDivisiblity(3,9)

