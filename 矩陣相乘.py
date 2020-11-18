# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 02:39:38 2020

@author: 皮小皮
"""


a=[[1,2,3],[4,5,6]]
b=[[1,0,1],[1,1,0],[0,1,1]]
c=[[0,0,0],[0,0,0]]

for row in range(0,2):
    for column in range(0,3):
        for k in range(0,3):
            c[row][column] = c[row][column]+a[row][k] * b[k][column]
            
            
            
for row in range(0,2):
    for column in range(0,3):
        print("%4d" %c[row][column] ,end="")
    print()