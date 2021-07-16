# -*- codeing = utf-8 -*-
# @Time : 2020/9/28 23:41
# @Author : zhaha
# @File : testBs4.py
# @Software : PyCharm

import urllib.request
import re
from bs4 import BeautifulSoup

respond = urllib.request.urlopen("http://www.baidu.com")
html = respond.read().decode("utf-8")

bs = BeautifulSoup(html, "html.parser")
# 第一个该标签
# print(bs.a)
# print(bs.head)
# print(bs.a.attrs) # attrs是所有键值对是标签a里面的

# find_all()搜索
# t_list = bs.find_all("head")

# 正则表达式搜索
# t_list = bs.find_all(re.compile("s_top"))
# for item in t_list:
#     print(item)


# t_list = bs.find_all(id="head_wrapper")
# print(type(t_list))
# for item in t_list:
#     print(item)

# t_list = bs.find_all("a", limit=3)

# t_list = bs.select("title")  # 标签
# t_list = bs.select("#head")  # id
# t_list = bs.select("p[class='lh']")  # 属性
t_list = bs.select("head > title")
# t_list = bs.select("#u1 ~ #s_top_wrap")  # 兄弟节点

print(t_list)
# for item in t_list:
#     print(item)