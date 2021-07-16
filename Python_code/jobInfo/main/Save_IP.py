# -*- codeing = utf-8 -*-
# @Time : 2020/10/9 23:00
# @Author : zhaha
# @File : Save_IP.py
# @Software : PyCharm


# 免费的不好用
"""
import requests
import parsel
import time

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4252.0 Safari/537.36"
}


def check_ip(proxies_list, f):
    can_use = []
    for proxy in proxies_list:
        try:
            respond = requests.get("https://baidu.com", headers=header, proxies=proxy, timeout=2)
            if respond.status_code == 200:
                can_use.append(proxy)
                ip = str(proxy)
                f.write(ip + "\n")
                print("当前ip:", proxy, "测试通过")
        except Exception as e:
            print(e)
    return can_use


proxies_list = []
for i in range(1, 10):
    print("===============正在爬取第{}页ip================".format(i))
    url = 'https://www.kuaidaili.com/free/inha/'
    url = url + str(i) + '/'
    responds = requests.get(url, headers=header)
    data = responds.text
    html = parsel.Selector(data)
    lists = html.xpath('//table/tbody/tr')

    for tr in lists:
        dict_proxies = {}
        http_type = tr.xpath('./td[4]/text()').extract_first().lower()
        http_ip = tr.xpath('./td[1]/text()').extract_first()
        http_port = tr.xpath('./td[2]/text()').extract_first()
        ip = http_ip + ":" + http_port
        dict_proxies[http_type] = "http://" + ip
        # dict_proxies[http_type+"s"] = "https://" + ip
        print(dict_proxies)
        proxies_list.append(dict_proxies)
        time.sleep(0.5)

f = open("IP.txt", "w")
can_use = check_ip(proxies_list, f)
print("代理IP数量为", len(can_use))
f.close()
"""