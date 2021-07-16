# -*- codeing = utf-8 -*-
# @Time : 2021/3/15 10:06
# @Author : zhaha
# @File : no1_1.py
# @Software : PyCharm


# def mymap(interable,op,value):
#     if op not in "+-*/":
#         print("erro")
#     def nested(item):
#         return eval(repr(item)+op+repr((value)))
#     return map(nested, interable)
#
# lists = list(mymap(range(5),'+',5))
# li = list(mymap(range(5),'-',5))
# print(lists)
# print(li)

def f2(n,i):
    ca = dict()

    def f(n, i):
        if n == i or i == 0:
            return 1
        elif (n,i) not in ca:
            ca[(n,i)] = f(n-1,i)+f(n-1,i-1)
        return ca[(n, i)]

    return f(n, i)

print(f2(5,4))