#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 21:58:19 2021

@author: thalitaramires
"""

#2) Mario:
#Problem: https://cs50.harvard.edu/x/2021/psets/6/mario/more/

def mario01():
    
    num = int(input("Digit a positive integer between 1 and 8: \n"))
    
    if num <1 or num > 8:
        print("\n Please, pay attention and try again! \n")
        return(mario01())
    else:
        return num
 
res = mario01()
print('\n')
print('The result is:')
print(res)

def mario():
    
    for i in range(res + 1):
        res1 = ((res - i) * ' ') + (i * '#') + (' ' + ' ') + (i * '#')
        res2 = str(res1)
        print(res2)
    
mario() 
