# -*- codeing = utf-8 -*-
# @Time : 2020/10/9 23:51
# @Author : zhaha
# @File : tyu.py
# @Software : PyCharm

import re
import requests
import random
from bs4 import BeautifulSoup

# findmax = re.compile(r'curPage=(\d*)" title="末页"></a>')
# headers ={
# "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4252.0 Safari/537.36"
# }
# ip = {'HTTP': '218.204.153.156:8080'}
# url = "https://www.liepin.com/zhaopin/?key=数据挖掘&dqs=010"
# Max = 0
# html = requests.get(url=url, headers=headers, proxies=ip)
# print(html.text)
# soup = BeautifulSoup(html.text, "html.parser")
# item = soup.find_all("a", class_="last")
# print(item)
# s = re.findall(findmax, str(item))[0]
# Max = int(s)
# print(s)

import requests
import random

# url0 = "http://api.xiequ.cn/VAD/GetIp.aspx?act=get&num=100&time=30&plat=0&re=0&type=0&so=1&ow=1&spl=1&addr=&db=1"
# header = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0"
#     }
# data = requests.get(url0, headers=header).json()['data']
# proxies = []
# for ip_data in data:
#     proxy = {}
#     ip = ip_data["IP"] + ":" + str(ip_data["Port"])
#     proxy['http'] = "http://" + ip
#     proxy['https'] = "https://" + ip
#     proxies.append(proxy)
#
# print(proxies[3])
# url = "http://httpbin.org/ip"
# html = requests.get(url, headers=header, proxies=proxies[3], timeout=2)
# print(html.text)

b = "北京"
i = 3
print(b*i)
a = b*i
print(a)