# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 18:29:22 2026

@author: a-ks798
"""

# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(a-ks798)s
"""

x=5
for i in range(0,10):

	if i == x:
		print(f'ループのスキップ条件に合致。continue')
		continue
	
	print(f'i={i},x={x}')
