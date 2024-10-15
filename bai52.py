# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 18:13:08 2024

@author: MINH NHUT
"""

#a
def can_bac(n,x):
    return n**(1/x)
#b
def so_dao(n):
    return str(n)[::-1]
#c
import math
def chinh_phuong(n):
    x = int(math.sqrt(n))
    return x**2 == n if n >1 else 0

#d
def nguyen_to(n):
    dem = 0
    if n <= 2 or n % 2 == 0:
        dem = 1
    else:
        for i in range(2, n):
            if n % i == 0:
                dem += 1
    return dem == 0

#e
def tich_le(n):
    tich = 1
    m = 0
    while n > 0:
        m = n % 10
        if m % 2 != 0:
            tich *= m
        n = n // 10
    return tich

#f
def tong_nguyen_to(n):
    tong = 0
    m = 0
    so_nguyen_to = [True] * n 
    so_nguyen_to[0] = so_nguyen_to[1] = False 
    for i in range(2, int(math.sqrt(n)) + 1):
        if so_nguyen_to[i] == True:
            for j in range(i * i, n, i):
                so_nguyen_to[j] = False
    so_nguyen_to[2] = False
    for i in so_nguyen_to:
        m += 1
        if i == True:
            tong += m-1
    return tong
#def tong_nguyen_to(n):
#tong = 0
#for i in range(1, n):
#    if nguyen_to(i):
#        tong += i
#return tong

#g
print(tong_nguyen_to(11))
def tong_chinh_phuong(n):
    tong = 0
    for i in range(1, n):
        if chinh_phuong(i):
            tong += i
    return tong
#h
def tong_uoc_duong(n):
    tong = 0
    for i in range(1, n+1):
        if n % i ==0:
            tong += i
    return tong

if __name__ == "__main__":
    print(can_bac(4, 2))
    print(so_dao(1234567890))
    print(chinh_phuong(9))
    print(nguyen_to(10))
    print(tich_le(1234253))
    print(tong_nguyen_to(11))
    print(tong_chinh_phuong(23))
    print(tong_uoc_duong(42))