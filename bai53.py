# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 19:35:09 2024

@author: MINH NHUT
"""

def ham1(n):
    tong = 0
    for i in range(1, n+1):
        tong += i
    return tong

def ham2(n):
    tong = 0
    for i in range(1, n+1):
        tong += i**2
    return tong

def ham3(n):
    tong = 0
    for i in range(1, n+1):
        tong += 1/n
    return tong

def ham4(n):
    tong = 0
    giai_thua = 1
    for i in range(1, n+1):
        giai_thua *= i
        tong += giai_thua
    return tong

def ham5(n):
    tich = 1
    for i in range(1, n+1):
        tich *= i
        
if __name__=="__main__":
    print(ham1(3))
    print(ham2(3))
    print(ham3(3))
    print(ham4(3))
    print(ham5(3))