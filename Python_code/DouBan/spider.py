# -*- codeing = utf-8 -*-
# @Time : 2020/9/28 21:20
# @Author : zhaha
# @File : spider.py
# @Software : PyCharm

from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式
import xlwt  # 进行excel操作
import urllib.request  # 指定url，获取网页数据
import urllib.error
import sqlite3  # 对数据库进行操作

# 各种正则表达式规则
findLink = re.compile(r'<a href="(.*?)">')
findImgSrc = re.compile(r'<img alt=".*src="(.*?)"', re.S)  # re.s表示让换行符包含在其中
findTitle = re.compile(r'<span class="title">(.*)</span>')
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
findJudge = re.compile(r'<span>(\d*)人评价</span>')
findInq = re.compile(r'<span class="inq">(.*)</span>')
findDb = re.compile(r'<p class="">(.*?)</p>', re.S)


# 爬取指定一个界面数据
def askURL(url):
    # 模拟浏览器，豆瓣拒绝爬虫
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4252.0 Safari/537.36"
    }
    req = urllib.request.Request(url=url, headers=header)
    html = ""
    try:
        respond = urllib.request.urlopen(req)
        html = respond.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


# 爬取网页
def getData(baseurl):
    Datalist = []
    for i in range(0, 10):
        url = baseurl + str(i * 10)
        html = askURL(url)

        #   逐一解析页面
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_="item"):
            data = []
            item = str(item)

            # 链接获取
            link = re.findall(findLink, item)[0]
            data.append(link)

            # 图片链接的获取
            ImgSrc = re.findall(findImgSrc, item)[0]
            data.append(ImgSrc)

            # 获取片名
            title = re.findall(findTitle, item)
            data.append(title[0])
            if len(title) == 2:
                data.append(title[1].replace("/", "").strip())
            else:
                data.append("")  # 留空

            # 评分
            rating = re.findall(findRating, item)[0]
            data.append(rating)

            # 评价人数
            judge = re.findall(findJudge, item)[0]
            data.append(judge)

            # 概况
            inq = re.findall(findInq, item)
            if len(inq) != 0:
                inq = inq[0].replace("。", "")
                data.append(inq)

            #  简介
            db = re.findall(findDb, item)[0]
            db = re.sub('<br(\s+)?/>(\s+)?', " ", db)
            db = re.sub("/", " ", db)
            data.append(db.strip())

            Datalist.append(data)
    for item in Datalist:
        print(item)
    return Datalist


# 保存数据
def saveData(path, datalist):
    excel = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = excel.add_sheet("豆瓣Top250", cell_overwrite_ok=True)
    col = ("电影链接", "图片链接", "中文名", "外文名", "评分", "评价人数", "概况", "相关信息")
    for i in range(8):
        sheet.write(0, i, col[i])
    for i in range(250):
        print("正在保存第%d条数据" % (i + 1))
        data = datalist[i]
        for j in range(0, 8):
            sheet.write(i + 1, j, data[j])
    excel.save(path)


def main():
    baseurl = "https://movie.douban.com/top250?start="
    #   1.爬取网页
    #   2.解析数据
    datalist = getData(baseurl)
    #     3.保存数据
    path = ".\\Top250.xls"
    saveData(path, datalist)


if __name__ == "__main__":
    # 调用函数
    main()
