# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 19:03:40 2024

@author: MINH NHUT
"""

def kiem_tra(n):
    if n<0 and n % 2 != 0:
        return -1
    elif n > 0 and n % 2 == 0:
        return 1
    return 0
print(kiem_tra(3))
print(kiem_tra(-3))