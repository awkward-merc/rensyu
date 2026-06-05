# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 21:16:54 2026

@author: awk77
"""

lst=[1, 2, 3]
print(f'{lst},要素数：{len(lst)}')

print('------')

lst.append(4)
print(f'{lst},要素数：{len(lst)}')

print('------')

lst.append([5,6])
print(f'{lst},要素数：{len(lst)}')

