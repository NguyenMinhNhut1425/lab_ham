# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 18:36:12 2024

@author: MINH NHUT
"""

import math
def tinh(*args, **kwargs):
    hinh = kwargs.get('hinh')
    pheptinh = kwargs.get('tinh')
    if hinh == 'vuong':
        canh = args[0]
        return 4* canh if pheptinh == 'cv' else canh**2
    
    elif hinh == 'chu_nhat':
        dai = args[0]
        rong = args[1]
        return 2 * (dai + rong) if pheptinh == 'cv' else dai*rong
    
    elif hinh == 'tron':
        bk = args[0]
        return 2*math.pi * bk if pheptinh == 'cv' else math.pi* (bk**2)
    
    else:
        return 'Hinh khong hop le'
    
if __name__=="__main__":
    print(tinh(10, hinh='vuong', tinh='cv'))
    print(tinh(50, hinh='vuong', tinh='dt'))
    print(tinh(18, hinh='tron', tinh='cv'))
    print(tinh(20, 30, hinh='chu_nhat', tinh='cv'))
