# -*- codeing = utf-8 -*-
# @Time : 2020/9/28 22:26
# @Author : zhaha
# @File : testUrllib.py
# @Software : PyCharm

import urllib.request
import requests

# respond = urllib.request.urlopen("http://www.baidu.com")
# print(respond.read().decode("utf-8"))


# 超时处理
# try:
#     respond = urllib.request.urlopen("http://httpbin.org/get", timeout=3)
#     print(respond.read().decode("utf-8"))
# except urllib.error.URLError as result:
#     print("超时了")


# respond = urllib.request.urlopen("http://www.baidu.com")
# print(respond.status)
# print(respond.getheaders())

# url = "http://httpbin.org/post"
# data = bytes(urllib.parse.urlencode({"name": "zhh"}), encoding="utf-8")
# header = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4252.0 Safari/537.36"
# }
# req = urllib.request.Request(url=url, data=data, headers=header, method="POST")
# respond = urllib.request.urlopen(req)
# print(respond.read().decode("utf-8"))

url = "http://douban.com"
# 修改键值对，模拟浏览器浏览
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4252.0 Safari/537.36"
}
# 封装
req = urllib.request.Request(url=url, headers=header)
respond = urllib.request.urlopen(req)
print(respond.read().decode("utf-8"))