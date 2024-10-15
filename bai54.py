# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 13:55:59 2024

@author: MINH NHUT
"""

def fibonacy(n):
    ds_fib = [0, 1]
    a = 0
    b = 1
    for i in range(n - 2):
        c = a + b
        ds_fib.append(c)
        a, b = b, c
    return ds_fib
print(fibonacy(10))