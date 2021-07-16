# -*- codeing = utf-8 -*-
# @Time : 2020/10/9 15:48
# @Author : zhaha
# @File : Main.py
# @Software : PyCharm

import requests
from bs4 import BeautifulSoup
from main import demands
from main import get_IP
from main import get_Header
from main import rinse
from main import cloud
import random

areas = {"北京": "010", "上海": "020", "广州": "050020", "深圳": "050090", "武汉": "170020",  "苏州": "060080", "重庆": "040", "南京": "060020", "杭州": "070020", "大连": "210040", "成都": "280020"}
jobs = ["数据挖掘", "图像算法工程师", "java后端", "互联网产品经理"]
# 公司
# &compTag=
# compTag = {"中国500强": "155", "互联网300强": "182", "制造业500强": "186", "独角兽": "130", "上市公司": "156"}
# 薪资
# &salary=10%2415
keys = []
values = []
can_use_ip = []
fail_demand_result = []
fail_list_result = []
headers = get_Header.get_header()
can_use_ip = get_IP.get_ip()

for item in areas.keys():
    keys.append(item)

for item in areas.values():
    values.append(item)


# 解析界面信息（https://www.liepin.com/zhaopin/?key=数据挖掘&dqs=010），捕获详细界面URL，保存详细信息
def geturl(url, job, f):
    global can_use_ip

    header = random.choice(headers)
    try:
        if len(can_use_ip) > 0:
            proxy = random.choice(can_use_ip)
        else:
            can_use_ip = get_IP.get_ip()
            proxy = random.choice(can_use_ip)
        can_use_ip.remove(proxy)
        page = requests.get(url=url, headers=header, proxies=proxy, timeout=3)
        soup = BeautifulSoup(page.text, "html.parser")
        soup = soup.find_all("h3")
        for item in soup:
            if item.has_attr("title"):
                # 抽取链接内容
                # 代理IP
                if len(can_use_ip) > 0:
                    proxy = random.choice(can_use_ip)
                else:
                    can_use_ip = get_IP.get_ip()
                    proxy = random.choice(can_use_ip)
                can_use_ip.remove(proxy)
                href = item.find_all("a")[0]["href"]
                start = "https://www.liepin.com"
                if href.startswith(start):
                    pass
                else:
                    href = start + href
                print(href+":"+str(proxy))
                # 通过详情界面url捕获职位要求
                result = demands.save_info(job, href, proxy)
                if result:
                    f.write(href + '\n')
                else:
                    fail_demand_result.append(href)
        return True
    except Exception as e:
        print("访问列表页失败")
        print(e)
        return False


def main():
    global can_use_ip
    print("可选择的工作有:")
    print(jobs)
    job = input("请输入你想要查找的工作:")
    print("可选择的地区有：")
    print(keys)
    # key = input("请输入您选择的地区:")
    f = open(job + "要求详情链接.txt", "a")

    # 设置url
    url0 = "https://www.liepin.com/zhaopin/?key=" + job
    # url0 = url0 + job + "&dqs=" + areas[key]

    for j in range(0, 5):
        f.write(keys[j]+'\n')
        url1 = url0 + "&dqs=" + values[j] + "&curPage="
        # url0 = url0 + "&curPage="

        # 遍历一个地方的5页列表,获取url
        for i in range(0, 5):
            url = url1 + str(i)
            print("正在爬取", job, ":", keys[j], "第%d页" % i)
            # 保存数据
            flag = geturl(url, job, f)
            if not flag:
                fail_list_result.append(url)

        # 处理未爬取成功的列表页
        while len(fail_list_result) != 0:
            for url in fail_list_result:
                print("重新爬取列表页:"+url)
                flag = geturl(url, job, f)
                if flag:
                    fail_list_result.remove(url)
        # 处理一个地区未爬取成功的网页
        while len(fail_demand_result) != 0:
            for url in fail_demand_result:
                if len(can_use_ip) > 0:
                    proxy = random.choice(can_use_ip)
                else:
                    can_use_ip = get_IP.get_ip()
                    proxy = random.choice(can_use_ip)
                can_use_ip.remove(proxy)
                result = demands.save_info(job, url, proxy)
                if result:
                    f.write(url+"\n")
                    fail_demand_result.remove(url)
            print("还剩%d未爬取" % len(fail_demand_result))
    f.close()

    # 数据处理
    cloud.make_cloud(job)  # 生成词云,保存数据清洗的结果


# 入口
if __name__ == "__main__":
    # 调用函数
    main()