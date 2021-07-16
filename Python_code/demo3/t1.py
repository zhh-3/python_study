# -*- codeing = utf-8 -*-
# @Time : 2020/11/21 13:56
# @Author : zhaha
# @File : t1.py
# @Software : PyCharm


def tt():
    print("Hello world"[1])
    print("Hello world"[-1])
    print("Hello world"[2:4])
    print("Hello world"[5:-2])
    print("Hello world"[6:-3], end="%")

def jie(n):
    k = n
    i = 1
    s = 1
    while i <= k:
        s *= i
        i = i+1
    return s


s = jie(100)
print(s)