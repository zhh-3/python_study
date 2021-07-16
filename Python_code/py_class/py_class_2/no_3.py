# -*- codeing = utf-8 -*-
# @Time : 2021/3/10 16:31
# @Author : zhaha
# @File : no_3.py
# @Software : PyCharm
import random

N = int(input("数量："))
list = []
for i in range(0, N):
    n = random.randint(1, 1000)
    if n not in list:
        list.append(n)
list2 = sorted(list)
print(list2)