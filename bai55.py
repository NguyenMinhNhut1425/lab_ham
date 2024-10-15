# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 18:31:21 2024

@author: MINH NHUT
"""

def chu_vi_hcn(dai,rong):
    return (dai+rong)*2

def dien_tich_hcn(dai,rong):
    return dai*rong
def ve_hcn(dai,rong):
    hinh = ""
    for i in range(dai):
        hinh += "* "*rong + "\n"
    return hinh

if __name__=="__main__":
    print(chu_vi_hcn(5, 4))
    print(dien_tich_hcn(7, 3))
    print(ve_hcn(6, 4))