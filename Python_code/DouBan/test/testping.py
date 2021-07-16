# -*- codeing = utf-8 -*-
# @Time : 2020/9/29 23:22
# @Author : zhaha
# @File : testping.py
# @Software : PyCharm


import urllib.request
import urllib.error
from bs4 import BeautifulSoup
import re
import xlwt

findLink = re.compile(r'<a data-promid="(.*)" href="(.*)" target="_blank">')
url = "https://www.liepin.com/zhaopin/?key=java"

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
for item in soup.find_all("h3"):
    item = str(item)
    # print(item)
    link = re.findall(findLink, item)
    if len(link) > 0:
        print(link[0][1])
