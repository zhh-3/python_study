# -*- codeing = utf-8 -*-
# @Time : 2020/10/9 15:49
# @Author : zhaha
# @File : demands.py
# @Software : PyCharm

import requests
from bs4 import BeautifulSoup
import re
import random

from main import get_Header

find_demands = re.compile(r"任职要求<br/>(\d.*)")
headers = get_Header.get_header()

def save_info(job, url, proxy):
    header = random.choice(headers)
    try:
        page = requests.get(url=url, headers=header, proxies=proxy, timeout=3)
        soup = BeautifulSoup(page.text, "html.parser")
        item = soup.select("div .job-item.main-message.job-description > div")
        if len(item) == 0:
            item = soup.select("div .job-main.job-description.main-message > div")
        if len(item) == 0:
            print("保存详情失败，被拒绝访问")
        else:
            item = str(item).replace("：", "").replace("岗位要求", "任职要求").replace("任职资格", "任职要求").replace("职位要求", "任职要求")
            item = re.findall(find_demands, item)
            if len(item) > 0:
                item = item[0].replace("\r", '')
                items = item.split("<br/>")
                f = open(job+'demands.txt', 'a')
                try:
                    for demand in items:
                        if len(demand) > 0:
                            f.write(demand+'\n')
                except Exception as result:
                    print(result)
                f.close()
        return True
    except Exception as e:
        print(e)
        return False