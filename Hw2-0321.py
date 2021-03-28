# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 23:07:39 2021

20210321 Hw2
2. 由系統產生 7個整數數字(亂數1-100)，
   (1) 要"遞增"印出來(重複沒關係) 例如：[10,7,6,100,90,5,17]
   (2) 由使用者輸一個值，去找尋串列中的值，用2分法顯示找尋過程 (2分搜尋法)

@author: user
"""

import random

number = []
 
for i in range (7):

    num = random.randint(1, 100)          
    number.append(num)
    
number.sort()
print(number)


n = int(input("請輸入一個值 (2分法顯示找尋過程): "))

while True:
   mid  = len(number) // 2
   
   if number[mid] > n:
       del number[mid:]

   elif number[mid] < n:
       del number[:mid]
       
   else:
       print("找到了")
       break
   print(number)



