# -*- codeing = utf-8 -*-
# @Time : 2021/3/17 19:43
# @Author : zhaha
# @File : no2.py
# @Software : PyCharm


def make_car(manufacturer, model, **other):
    dic = dict()
    dic["manufacturer"] = manufacturer
    dic["model"] = model
    dic.update(other)
    return dic


car = make_car('sub', 'outback', color = "black", tow = True)
print(car)