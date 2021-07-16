# -*- codeing = utf-8 -*-
# @Time : 2020/10/15 21:48
# @Author : zhaha
# @File : cloud.py
# @Software : PyCharm


import jieba

stopword = [' ', '/', '的', '及', "或", "和", "，", "；", "了解", "熟悉", "等", "/", "至少", "具备", "能", "有", "为佳", "优先", "、", "可以"
            , "如", "强烈", "对", "一定", "。", "优化", "具有", "善于", "乐于", ":", "好", "较", "强"]
s = "7. 具有 Spring Cloud / Eureka / Consul / Hadoop / HBase / Spark / Storm 等经验者优先；"
demands = s[2:]
tag_filter = ['n']
des = jieba.lcut(demands, cut_all=False)
sentence = des
jieba.analyse.extract_tags(sentence, topK=20, withWeight=True)
for de in des:
    if de not in stopword:
        print(de, end='2')