# -*- codeing = utf-8 -*-
# @Time : 2020/10/13 17:22
# @Author : zhaha
# @File : jiebaTest.py
# @Software : PyCharm


import jieba

stopword = ['的', '及', "或", "和", "，", "；", "了解", "熟悉", "等", "/", "至少", "具备", "能", "有", "为佳", "优先", "、", "可以"
            , "如", "强烈", "对", "一定", "。", "优化", "具有", "善于", "乐于", ":", "好", "较", "强"]
jieba.suggest_freq("大数据", True)
jieba.suggest_freq("后端", True)
try:
    f = open("../main/java后端demands.txt", "r")
    try:
        while True:
            contents = f.readline()
            if len(contents) == 0:
                break
            # s = "1. 本科及以上学历，计算机或相关专业，良好的编码和设计能力；"
            demands = contents[2:].split()[0]
            des = jieba.cut(demands, cut_all=False)
            final = []
            for de in des:
                if de not in stopword:
                    final.append(de)
            print(final)
    finally:
        f.close()
        print("文件已关闭")
except Exception as e:
    print(e)

