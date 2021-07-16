# -*- codeing = utf-8 -*-
# @Time : 2021/4/13 19:34
# @Author : zhaha
# @File : no_4.py
# @Software : PyCharm


import json
class employee(object):
    def __init__(self, pid, pname, price):
        self.pid = pid
        self.pname = pname
        self.price = price


employee1 = employee("p001", "测试商品1", 299)
employee2 = employee("p002", "测试商品2", 499)
lists = [employee1, employee2]
with open("E:\\employee2.json", "w") as file:
    li = []
    for list in lists:
        dic = {}
        dic['pid'] = list.pid
        dic['pname'] = list.pname
        dic['price'] = list.price
        li.append(dic)
    json.dump(li, file)
file.close()

with open("E:\\employee2.json", "r") as file:
    dics = json.load(file)
    for i in dics:
        print(i)
    file.close()