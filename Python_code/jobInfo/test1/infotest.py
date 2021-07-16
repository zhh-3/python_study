# -*- codeing = utf-8 -*-
# @Time : 2020/10/4 15:25
# @Author : zhaha
# @File : infotest.py
# @Software : PyCharm


import requests
from bs4 import BeautifulSoup
import re

def save_demands(demands, f):
    try:
        for demand in demands:
            f.write(demand+'\n')
    except Exception as result:
        print(result)


findjobre = re.compile(r"任职要求：<br/>(.*)")

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4252.0 Safari/537.36"
}

urls = ["https://www.liepin.com/job/1932329977.shtml", "https://www.liepin.com/job/1931874135.shtml",
        "https://www.liepin.com/job/1931662759.shtml", "https://www.liepin.com/job/1931093053.shtml",
        "https://www.liepin.com/job/1928883669.shtml", "https://www.liepin.com/job/1926447589.shtml",
        "https://www.liepin.com/job/1926029887.shtml", "https://www.liepin.com/job/1924942301.shtml",
        "https://www.liepin.com/job/1922886351.shtml", "https://www.liepin.com/a/22580545.shtml",
        "https://www.liepin.com/a/22574621.shtml", "https://www.liepin.com/a/22562203.shtml",
        "https://www.liepin.com/a/22548183.shtml", "https://www.liepin.com/a/22502351.shtml",
        "https://www.liepin.com/a/22377681.shtml", "https://www.liepin.com/a/22262579.shtml",
        "https://www.liepin.com/a/21976941.shtml", "https://www.liepin.com/a/21922941.shtml",
        "https://www.liepin.com/a/21882031.shtml"]

for url in urls:
    page = requests.get(url=url, headers=header)
    soup = BeautifulSoup(page.text, "html.parser")
    item = soup.select("div .content.content-word")[0]
    item = str(item)
    print(item)
    item = re.findall(findjobre, item)
    k = len(item)
    if k > 0:
        item = item[0].replace("\r", '')
        items = item.split("<br/>")
        f = open('demand.txt', 'a')
        save_demands(items, f)
        f.close()
    else:
        print("无")
