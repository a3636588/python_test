# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 01:39:11 2020

@author: 皮小皮
"""

Sum = [0,0,0,0] 
student = [[65,85,78,75,69],[66,55,52,92,47],[75,99,63,73,86],[77,88,99,91,100]]

for i in range (0,4):
    Sum[i]=0

for i in range (0,4):
    for j in range (0,5):
        Sum[i] = Sum[i]+student[i][j]   # 0+65 65+85 85 +78 ..
for i in range (0,4):
    
    print("%d 位平均=" %(i+1),Sum[i]/5)
        