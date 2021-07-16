# -*- codeing = utf-8 -*-
# @Time : 2020/9/30 19:39
# @Author : zhaha
# @File : task.py
# @Software : PyCharm


import requests
from bs4 import BeautifulSoup
# import config
areas = {"北京": "010", "上海": "020", "广州": "050020", "深圳": "050090", "天津": "030", "苏州": "060080", "重庆": "040", "南京": "060020", "杭州": "070020", "大连": "210040", "成都": "280020", "武汉": "170020"}
job = ["数据挖掘", "图像算法工程师", "java后端", "互联网产品经理"]
url = "https://www.liepin.com/zhaopin/?key="
print("可选择的职位有")
print(job)
jobname = input("你选择的职业是:")
print("可选择的地区有：")
print(areas.keys())
area = input("你选择的地区是：")
dbq = areas.get(area)

if dbq == None:
    print("无次地区")
else:
    url = url + jobname + "&dqs=" + dbq
    page = requests.get(url=url)
    soup = BeautifulSoup(page.text, "html.parser")
    soup = soup.find_all("h3")
    f = open(jobname+"links.txt", "w")

    for i in soup:
        if i.has_attr("title"):
            # 抽取链接内容
            href = i.find_all("a")[0]["href"]
            start = "https://www.liepin.com"
            if href.startswith(start):
                f.write(href+"\n")
            else:
                href = start + href
                f.write(href + "\n")

    f.close()