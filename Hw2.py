# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 17:24:54 2021

@author: user
"""

start = int(input('初始值:'))
end = int(input('終止值:'))

print('4的倍數有:',end=" ")
for i in range(start,end+1):
    if i % 4 == 0:
        print(i,end=' ')
        
print()        
print('質數有:',end=" ")

for j in range(start,end+1):
    count = 0
    for k in range(2,j):
        if j % k == 0:
            count += 1
    if count == 0 and j != 1:
        print(j,end=' ')

    
print()
print('程式執行完畢')    
