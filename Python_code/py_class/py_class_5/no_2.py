# -*- codeing = utf-8 -*-
# @Time : 2021/4/5 14:50
# @Author : zhaha
# @File : no_2.py
# @Software : PyCharm


f1 = open("E:/hillbillies.txt", 'r')
f2 = open("E:/hillbillie.txt", 'w')
while True:
    line = f1.readline()
    if not line:
        break
    line = ("-" + line).upper()
    f2.write(line)
f1.close()
f2.close()