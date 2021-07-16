# -*- codeing = utf-8 -*-
# @Time : 2020/9/30 9:53
# @Author : zhaha
# @File : testmax.py
# @Software : PyCharm


import urllib.request
import urllib.error
from bs4 import BeautifulSoup
import re

url = "https://www.liepin.com/zhaopin/?key=java&curPage="
findmax = re.compile(r'curPage=(\d*)" title="末页"></a>')
# 模拟浏览器，豆瓣拒绝爬虫
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4252.0 Safari/537.36"
}
req = urllib.request.Request(url=url, headers=header)
html = ""
try:
    respond = urllib.request.urlopen(req)
    html = respond.read().decode("utf-8")
except urllib.error.URLError as e:
    if hasattr(e, "code"):
        print(e.code)
    if hasattr(e, "reason"):
        print(e.reason)

soup = BeautifulSoup(html, "html.parser")
item = soup.find_all("a", class_="last")
s = re.findall(findmax, str(item))[0]
max = int(s)
print(max)
# print(s[len(s)-1])

