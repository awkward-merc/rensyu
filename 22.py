# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 21:19:57 2026

@author: awk77
"""

lst = [1, 2, 3]
lst.remove(2)
print(lst)

print('------')

lst.append(4)
lst.append(4)
print(lst)

print('------')

lst.remove(4)
print(lst)

print('------')

# lst.remove(5) #一致するものがないのでエラー
print(lst)

print('------')

# lst.remove([4,5]) #これもエラー
print(lst)

print('------')

lst.remove(4.0) #これは同一判定
print(lst)
