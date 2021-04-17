#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 13:53:55 2021

@author: thalitaramires
"""

#3) Cash:
#Problem: https://cs50.harvard.edu/x/2021/psets/6/cash/

quarters = 0.25
dimes = 0.10
nickels = 0.05
pennies = 0.01   
   
def cashBack01():
    cashBack = float(input("how much change is owed?"))
    if cashBack <= 0:
        print("\n Please pay attention and try again! \n")
        return cashBack01()
    else:
        return cashBack
    
cashBack = cashBack01()

count = 0
if cashBack % quarters == 0.0:
    print(int(cashBack / quarters))
else:
    div_quarters = int(cashBack / quarters)
    q = round(div_quarters,2)
    count += q
    mod_quarters = cashBack % quarters
    qm = round(mod_quarters, 2)
    if qm % dimes == 0.0:
        print(count + int(qm / dimes))
    else:    
        div_dimes = int(qm / dimes)
        d = round(div_dimes,2)
        count += d
        mod_dimes = qm % dimes
        dm = round(mod_dimes, 2)
        if dm % nickels == 0.0:
            print(count + int(dm / nickels))
        else:
            div_nickels = int(dm / nickels)
            n = round(div_nickels,2)
            count += n
            mod_nickels = dm % nickels
            nm = round(mod_nickels,2)
            if nm % pennies == 0.0:
                print(count + int(nm / pennies))
            else:
                print(count + int(nm / pennies))    
