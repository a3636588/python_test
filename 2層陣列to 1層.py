# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 01:52:45 2020

@author: 皮小皮
"""

data1=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]
data2=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(0,3):
    for j in range(0,5):
        print("%4d" %data1[i][j],end="")
    print()
    
    
for i in range(0,3):
    for j in range(0,5):
        x= i + j*3
        data2[x] = data1[i][j]
        
        
for i in range(0,15):
        

    print("%4d" %data2[i],end="")