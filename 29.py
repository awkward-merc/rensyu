# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 18:07:25 2026

@author: awk77
"""
x=10
y=20

result = x>15 and y>15
print(f'resultの値：{result}')
print('------')

result = x<=15 and y>=15
print(f'resultの値：{result}')
print('------')

result = x<=15 and y<=15
print(f'resultの値：{result}')
print('------')

result = x>=15 and y>=15
print(f'resultの値：{result}')
print('------')



result = x>15 or y>15
print(f'resultの値：{result}')
print('------')

result = x<=15 or y>=15
print(f'resultの値：{result}')
print('------')

result = x<=15 or y<=15
print(f'resultの値：{result}')
print('------')

result = x>=15 or y>=15
print(f'resultの値：{result}')
print('------')
