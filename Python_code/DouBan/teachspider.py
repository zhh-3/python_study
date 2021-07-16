# -*- codeing = utf-8 -*-
# @Time : 2020/9/30 10:54
# @Author : zhaha
# @File : teachspider.py
# @Software : PyCharm


import requests
from bs4 import BeautifulSoup
import xlwt

areas = {"北京": "010", "上海": "020", "广州": "050020", "深圳": "050090", "天津": "030", "苏州": "060080", "重庆": "040", "南京": "060020", "杭州": "070020", "大连": "210040", "成都": "280020", "武汉": "170020"}
job = ["数据挖掘", "图像算法工程师", "java后端", "互联网产品经理"]
keys = []
values = []
header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4252.0 Safari/537.36"
    }
for item in areas.keys():
    keys.append(item)

for item in areas.values():
    values.append(item)

for i in range(0, len(job)):
    excel = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = excel.add_sheet(job[i], cell_overwrite_ok=True)
    for j in range(0, len(keys)):
        sheet.write(0, j, keys[j])
        url = "https://www.liepin.com/zhaopin/?key="
        url = url + job[i] + "&dqs=" + values[j]
        page = requests.get(url=url, headers=header)
        soup = BeautifulSoup(page.text, "html.parser")
        soup = soup.find_all("h3")
        k = 1
        for item in soup:
            if item.has_attr("title"):
                # 抽取链接内容
                href = item.find_all("a")[0]["href"]
                start = "https://www.liepin.com"
                if href.startswith(start):
                    sheet.write(k, j, href)
                else:
                    href = start + href
                    sheet.write(k, j, href)
                k += 1
    excel.save(job[i]+".xls")
    print(job[i]+"已经保存")
print("数据保存完毕")