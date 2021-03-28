# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 01:53:05 2021

20210321 Hw3
3. 由使用者輸入獲利金額，顯示獎金金額 (分層獎金計算)
   (1) 含10萬以內，獎金10%
   (2) 10萬-20萬 (低於10萬獎金10%，剩餘的獎金7%) -> 14萬 (10萬*10% + 4萬*7%)
   (3) 20萬-40萬 (低於10萬獎金10%，+10萬7%，剩餘的獎金3%) -> 39萬 (10萬*10% + 10萬*7% + 19萬*3%)

"""
bonus = 0
money = int(input("請輸入獲利金額: "))

if money < 100000:
    bonus = money*0.1
    print('獎金: ',(int(bonus)))

elif money >= 100000 and money < 200000:
    m1 = money-100000
    bonus = 10000*0.1+m1*0.07
    print('獎金: ',(int(bonus)))

elif money >= 200000 and money <= 400000:
    m2 = money-200000
    bonus = 10000*0.1+10000*0.07+m2*0.03
    print('獎金: ',(int(bonus)))
        
    
    

