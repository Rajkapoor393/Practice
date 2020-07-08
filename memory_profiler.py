# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 19:42:54 2020

@author: Raj
"""

@profile
def append_lst():
   lst= []
    for i in range(1000000):
        lst.append(i)
        
append_lst()