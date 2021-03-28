# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 16:52:25 2021

20210321 Hw1
1. 由系統亂數產生 1-49 之間六個，不重複的整數，請排序"遞增"印出
   random
   count

@author: user
"""
import random

result = []
count = 0

while True:
    
    num = int (random.randint(1, 49))
    
    if count == 6:
        break
    
    if result.count(num) == 0:
        result.append(num)
        count += 1
    
result.sort()
print(result)

print('程式執行完畢')    
        
