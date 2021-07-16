# -*- codeing = utf-8 -*-
# @Time : 2021/3/10 16:47
# @Author : zhaha
# @File : no_5.py
# @Software : PyCharm

list1 = []
list2 = []
Num = int(input("请输入数据表数据数量:"))
for i in range(0, Num):
    i = int(input("index:"))
    j = int(input("value:"))
    print()
    list1.append(i)
    list2.append(j)

print("数据表为：")
print("key:value")
for i in range(0, Num):
    print(str(list1[i])+"  : "+str(list2[i]))

print("\n处理后数据表为：")
dic = {}
keys = []
for i in range(0, Num):
    x = {list1[i]: list2[i]}
    if list1[i] not in keys:
        dic.update(x)
        keys.append(list1[i])
    else:
        dic[list1[i]] = dic[list1[i]]+list2[i]

keys = sorted(keys)
print("key:value")
for i in range(0, len(dic)):
    print(str(keys[i])+"  : "+str(dic[keys[i]]))