# -*- codeing = utf-8 -*-
# @Time : 2020/10/10 0:06
# @Author : zhaha
# @File : get_IP.py
# @Software : PyCharm

import requests
url = "http://api.xiequ.cn/VAD/GetIp.aspx?act=get&num=20&time=30&plat=0&re=0&type=2&so=1&ow=1&spl=1&addr=&db=1"
header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0"
    }
def get_ip():
    data = requests.get(url, headers=header).json()['data']
    proxies = []
    for ip_data in data:
        proxy = {}
        ip = ip_data["IP"] + ":" + str(ip_data["Port"])
        proxy['http'] = ip
        proxy['https'] = ip
        proxies.append(proxy)
    return proxies
