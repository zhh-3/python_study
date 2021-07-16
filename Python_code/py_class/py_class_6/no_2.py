# -*- codeing = utf-8 -*-
# @Time : 2021/4/18 0:10
# @Author : zhaha
# @File : no_2.py
# @Software : PyCharm


import matplotlib.pyplot as plt
import random

def walk():
    lists = []
    for i in range(2000):
        t = random.randint(0, 1)
        if t == 0:
            t = -1
        lists.append(t)
    return lists

def cumsum(lists):
    sum = 0
    lists2 = []
    for list in lists:
        sum += list/2
        lists2.append(sum)
    return lists2


list = walk()
list2 = cumsum(list)
x = []
print("正向最远距离："+str(max(list2)))
print("反向最远距离："+str(min(list2)))

i = 1
j = 1
for dis in list2:
    x.append(j)
    if dis >= 15 or dis <= -15:
        print("第"+str(i)+"次离原点距离超过15米,是第"+str(j)+"步")
        i += 1
    j += 1
if i == 1:
    print("酒鬼最远也没走到15米")

plt.plot(x, list2)
plt.show()