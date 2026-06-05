# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 20:42:05 2026

@author: awk77
"""

x=None
list_x = [None,"None",1, "文字列",""]

for x in list_x:
	print(f'xの値：{x}')

	result = x is None
	print(f'結果：{result}')
	if result:
		print(f'変数が None であるか：{result}')

	print('------')
