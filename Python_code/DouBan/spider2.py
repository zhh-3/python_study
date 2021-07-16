# -*- codeing = utf-8 -*-
# @Time : 2020/9/29 23:08
# @Author : zhaha
# @File : spider2.py
# @Software : PyCharm


import urllib.request
import urllib.error
from bs4 import BeautifulSoup
import re
import xlwt


findLink = re.compile(r'<a data-promid="(.*)" href="(.*)" target="_blank">')
findmax = re.compile(r'curPage=(\d*)" title="末页"></a>')
# 爬取指定一个界面数据
def askURL(url):
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
    return html


def getUrl(baseurl):
    data = []
    max = getMax(baseurl)
    for i in range(0, max+1):
        url = baseurl + str(i)
        html = askURL(url)
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all("h3"):
            item = str(item)
            link = re.findall(findLink, item)
            if len(link) > 0:
                InfoUrl = link[0][1]

                data.append(InfoUrl)
    return data


def getMax(url):
    Max = 0
    html = askURL(url)
    soup = BeautifulSoup(html, "html.parser")
    item = soup.find_all("a", class_="last")
    s = re.findall(findmax, str(item))[0]
    Max = int(s)
    return Max


def savaData(data):
    print("save.....")
    f = open("test.txt", "w")
    for item in data:
        f.write(item+"\n")
    f.close()


def main():
    url = "https://www.liepin.com/zhaopin/?key=java&curPage="
    data = getUrl(url)
    savaData(data)


if __name__ == "__main__":
    main()
