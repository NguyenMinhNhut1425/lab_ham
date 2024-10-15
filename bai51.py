# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 19:06:41 2024

@author: MINH NHUT
"""

def kiem_tra():
    n = input("Nhập giá trị: ")
    if n.replace('.', '',1).replace('-', '',1).isdigit():
        n = float(n)
    if -89 <= n <= 90:
        return n
    print("Không hợp lệ")
    return kiem_tra()
print(kiem_tra())