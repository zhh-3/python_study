# -*- codeing = utf-8 -*-
# @Time : 2021/3/2 22:07
# @Author : zhaha
# @File : No_3.py
# @Software : PyCharm


anum = input("一个整数：")
a = int(anum)
flag = True
if a < 0:
    a = -a
    flag = False
b = a
c = b % 10
b = int(a/10)
num = c
list = []
list.append(c)
while b > 0:
    c = b % 10
    b = int(b/10)
    if c not in list:
        list.append(c)
        num = num*10+c
if not flag:
    num = -num
print(num)