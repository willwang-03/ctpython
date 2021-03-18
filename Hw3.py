# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 14:06:42 2021

@author: user
"""

import random

ans = random.randint(1, 100)
guess = 0
max = 100
min = 1
count = 0

while ans != guess:
    print('輸入',min,'~',max,'之間整數猜數')
    guess = int (input())
    count += 1
     
    if guess == ans:     
        print('猜對了')   
    
    elif count == 5:
        print('猜錯達5次,挑戰失敗!')
        break
    
    if guess > ans:
        print('猜小一點')
        max = guess -1
        
    if guess < ans:
        print('猜大一點')
        min = guess +1

  