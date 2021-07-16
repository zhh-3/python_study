# -*- codeing = utf-8 -*-
# @Time : 2021/3/2 22:29
# @Author : zhaha
# @File : change_cases.py
# @Software : PyCharm


name = input("姓名:")
print(name.lower())
print(name.upper())
c = name[0]
if c.islower():
    c = c.upper()
print(c+name[1:])