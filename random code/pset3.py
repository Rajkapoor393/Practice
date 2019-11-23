# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 23:17:34 2019

@author: Raj
"""

"""
Python | Set 3 (Strings, Lists, Tuples, Iterations)

"""
# Strings in python

a ="Be the hardest worker of the room"
print(a)

# List in python

L = [1, 'a', 'string', 1+2]
print(L)
L.append(6)
print(L)
L.pop()
print(L)
print(L[1])
print(L[2])

# Tuples in python

Tuple = (1, 'a', 'string', 'hello')
print(Tuple)
print(Tuple[0])
print(Tuple[2])

#Iterations in python

#Example1: iteration by while loop for a condition
i=0
while (i<10):
    i =i+1
    print(i)
    
#example 2: iteration by for loop on string

s = "Hello World"

for i in s:
    print(i)

# Example 3: iteration by for loop on list

L= [1,2,3,'string', 'Hello']
for i in L:
    print(i)
    
#Example 4: iteration by for loop on range
for i in range(1,10):
    
    print(i)