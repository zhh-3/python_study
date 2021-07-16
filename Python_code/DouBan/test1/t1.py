# -*- codeing = utf-8 -*-
# @Time : 2020/9/28 21:26
# @Author : zhaha
# @File : t1.py
# @Software : PyCharm

# def add(a, b):
#     return a+b
#
#
# def mer(a):
#     i = 1
#     s = 1
#     if a > 0:
#         while i <= a:
#             s = s*i
#             i += 1
#     else:
#         s = -1
#         print("输入错误!")
#     return s

import requests

url = "https://www.liepin.com/job/1925020667.shtml"


print(requests.get(url,proxies={'HTTPS': '175.42.122.99:9999', 'HTTP': '175.42.122.99:9999'}).text)