# -*- codeing = utf-8 -*-
# @Time : 2020/9/30 19:15
# @Author : zhaha
# @File : getarea.py
# @Software : PyCharm


import requests
from bs4 import BeautifulSoup
import re

finddbq = re.compile("")

url = "https://www.liepin.com/zhaopin/?key=java"

html = requests.get(url=url).text
soup = BeautifulSoup(html, "html.parser")
items = soup.find_all("dd")
for item in items:
    print(item)
    # href = item.find_all("a")[0]
    # print(href)