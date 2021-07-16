# -*- codeing = utf-8 -*-
# @Time : 2020/10/27 0:47
# @Author : zhaha
# @File : get_IP.py
# @Software : PyCharm

import requests
url = "http://api.wandoudl.com/api/ip?app_key=a274cb277bc2e89410deeee3e4b30598&pack=0&num=20&xy=1&type=2&lb=\r\n&mr=2&"
header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0"
        }
def get_ip():
    data = requests.get(url, headers=header).json()['data']
    proxies = []
    for ip_data in data:
        proxy = {}
        ip = ip_data["ip"] + ":" + str(ip_data["port"])
        proxy['http'] = ip
        proxy['https'] = ip
        proxies.append(proxy)
    return proxies

